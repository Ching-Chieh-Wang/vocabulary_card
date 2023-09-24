from vocabularyCardModel import VocabularyCardModel
from vocabularyCardView import VocabularyCardView
from editThisController import EditThisController
from loadOrCreateController import LoadOrCreateController
from PyQt5 import QtWidgets,QtCore
import os
import sys
import csv
import time
import win32com.client

class VocabularyCardController:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.model=VocabularyCardModel()
        self.view=VocabularyCardView()
        self.view.nextBtn.clicked.connect(self.nextCard)
        self.view.previousBtn.clicked.connect(self.previousCard)
        self.view.goBtn.clicked.connect(self.go)
        self.view.searchBtn.clicked.connect(self.search)
        self.view.resetBtn.clicked.connect(self.reset)
        self.view.sequentialRBtn.clicked.connect(self.sequential)
        self.view.star1sRBtn.clicked.connect(self.star1s)
        self.view.star2sRBtn.clicked.connect(self.star2s)
        self.view.nonRememberRBtn.clicked.connect(self.nonRemember)
        self.view.goTB.textChanged.connect(self.editGoToTB)
        self.view.star1Box.clicked.connect(self.updateCard)
        self.view.star2Box.clicked.connect(self.updateCard)
        self.view.rememberBox.clicked.connect(self.updateCard)
        self.view.shuffleBox.clicked.connect(self.shuffle)
        self.view.cambridgeBtn.clicked.connect(lambda: self.model.cambridge(self.card.vocabulary))
        self.view.pronounciationBtn.clicked.connect(self.pronounciation)
        self.view.copyBtn.clicked.connect(lambda: self.model.copy(self.card.vocabulary))
        self.view.editThisBtn.clicked.connect(self.editThis)
        self.view.editAllBtn.clicked.connect(self.editAll)
        self.view.loadOrCreateBtn.clicked.connect(self.loadOrCreate)
        loadedPath,msg=self.model.loadDefault()
        while loadedPath=="":
            self.view.setDisabled(True)
            loadedPath=self.loadOrCreate()
            self.view.setDisabled(False)
        self.view.setWindowTitle("vocabulary Card:  {}".format(loadedPath.split('/')[-1].split('.db')[0]))
        self.view.sequentialRBtn.click()
        sys.exit(app.exec_())
    def loadOrCreate(self):
        self.loadOrCreateController=LoadOrCreateController(self.model.load)
        if self.loadOrCreateController.path=="":
            return ""
        self.view.setWindowTitle("vocabulary Card:  {}".format(self.loadOrCreateController.path.split('/')[-1].split('.db')[0]))
        self.view.sequentialRBtn.click()
        return self.loadOrCreateController.path
    def show(self):
        self.card=self.model.currentCard()
        self.view.showCard(self.card,self.model.currentIdx,self.model.vocabularyNum())
    def nextCard(self):
        self.model.nextCard()
        self.show()
    def previousCard(self):
        self.model.previousCard()
        self.show()
    def go(self):
        self.model.go(int(self.view.goTB.text()))
        self.show()
    def search(self):
        if self.view.searchTB.text()=="":
            self.reset()
        else:
            if self.view.shuffleBox.isChecked():
                self.view.shuffleBox.click()
            self.model.search(self.view.searchTB.text(),self.view.sequentialRBtn.isChecked(),self.view.star1sRBtn.isChecked(),self.view.star2sRBtn.isChecked(),self.view.nonRememberRBtn.isChecked())
            self.show()
    def editAll(self):
        self.sequential()
        self.view.setEnabled(False)
        self.timer = QtCore.QTimer.singleShot(1000,self.opencsv)
    def opencsv(self):
        with open('vocabulary.csv', mode='w', newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(('vocabulary','Definition','Star1','Star2','Remember'))
            for row in self.model.table:
                writer.writerow(row[1:])
        success=False
        while not success:
            excelApp = win32com.client.Dispatch("Excel.Application")
            excelApp.Visible =True
            excelApp.Workbooks.Open(os.path.join(os.getcwd(),"vocabulary.csv"))
            while True:
                try:
                    if excelApp.Workbooks.Count == 0:
                        break
                except:
                    None
                time.sleep(1)
            excelApp.Quit()
            data=[]
            with open('vocabulary.csv', mode='r',encoding='utf-8-sig') as file:
               reader = csv.reader(file)
               next(reader)  # Skip header if present
               error=False
               for i,row in enumerate(reader):
                   if row[0]=='' or row[1]=='':
                       error=True
                       break
                   data.append((row[0], row[1],row[2]=='1',row[3]=='1',row[4]=='1'))
               if error:
                   self.view.setEnabled(True)
                   self.view.msg("Check Excel Input", "Check Row:"+str(i+2))
                   self.view.setEnabled(False)
               success = not error
        self.model.editAll(data)
        self.view.setEnabled(True)
        self.view.sequentialRBtn.click()
    def editGoToTB(self):
        self.view.goBtn.setDisabled(self.view.goTB.text()=='' or not (0<int(self.view.goTB.text())<=self.model.vocabularyNum()))
    def updateCard(self):
        self.card.edit(vocabulary=self.view.vocabularyLbl.text(),definition=self.view.definitionLbl.text(),star1=self.view.star1Box.isChecked(),star2=self.view.star2Box.isChecked(),remember=self.view.rememberBox.isChecked())
        self.model.editCard(self.card)
    def shuffle(self):
        if self.view.shuffleBox.isChecked():
            self.model.shuffleCard()
        else:
            self.model.cancelShuffleCard()
        self.show()
    def reset(self):
        if self.view.sequentialRBtn.isChecked():
            self.sequential()
        elif self.view.star1sRBtn.isChecked():
            self.view.star1sRBtn.click() 
        elif self.view.star2sRBtn.isChecked():
            self.view.star2sRBtn.click() 
        elif self.view.nonRememberRBtn.isChecked():
            self.view.nonRememberRBtn.click() 
        self.view.searchTB.setText("")
        if self.view.shuffleBox.isChecked():
            self.view.shuffleBox.click()
    def sequential(self):
        if self.view.shuffleBox.isChecked():
            self.view.shuffleBox.click()
        self.model.sequential()
        self.show()
    def star1s(self):
        if self.view.shuffleBox.isChecked():
            self.view.shuffleBox.click()
        self.model.star1s()
        self.show()
    def star2s(self):
        if self.view.shuffleBox.isChecked():
            self.view.shuffleBox.click()
        self.model.star2s()
        self.show()
    def nonRemember(self):
        if self.view.shuffleBox.isChecked():
            self.view.shuffleBox.click()
        self.model.nonRemember()
        self.show()
    def pronounciation(self):
        success=self.model.pronounciation(self.card.vocabulary)
        if not success:
            self.view.prnounceFailed()
        else:
            self.view.pronounciate()
    def editThis(self):
        self.view.setDisabled(True)
        self.editThisController=EditThisController(self.editThisDone,self.cancelOperation,self.card.vocabulary,self.card.definition)
        
    def editThisDone(self,card):
        self.view.vocabularyLbl.setText(card.vocabulary)
        self.view.definitionLbl.setText(card.definition)
        self.updateCard()
        self.updateCardorController=None
        self.view.setDisabled(False)
    def cancelOperation(self):
        self.view.setDisabled(False)

        
            
        