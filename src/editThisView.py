
from PyQt5 import QtCore, QtGui, QtWidgets
from stylesheets import btnDangerStyle,btnSuccessStyle,tBStyle

class EditThisView(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('vocabularyCard.png'))
        font = QtGui.QFont()
        font.setFamily(u"Ink Free")
        font.setPointSize(30)
        self.setWindowTitle("Card Editor")
        self.resize(1020, 540)
        self.volcabularyTB = QtWidgets.QLineEdit(self)
        self.volcabularyTB.setObjectName(u"volcabularyTB")
        self.volcabularyTB.setGeometry(QtCore.QRect(91, 127, 841, 91))
        self.volcabularyTB.setFont(font)
        self.volcabularyTB.setStyleSheet(tBStyle())
        self.definitionTB = QtWidgets.QLineEdit(self)
        self.definitionTB.setObjectName(u"definitionTB")
        self.definitionTB.setFont(font)
        self.definitionTB.setGeometry(QtCore.QRect(91, 316, 841, 91))
        self.definitionTB.setStyleSheet(tBStyle())
        self.volcabularyLbl = QtWidgets.QLabel(self)
        self.volcabularyLbl.setObjectName(u"volcabularyLbl")
        self.volcabularyLbl.setGeometry(QtCore.QRect(91, 71, 611, 50))
        self.volcabularyLbl.setFont(font)
        self.definitionLbl = QtWidgets.QLabel(self)
        self.definitionLbl.setObjectName(u"definitionLbl")
        self.definitionLbl.setGeometry(QtCore.QRect(90, 250, 611, 50))
        self.definitionLbl.setFont(font)
        self.volcabularyLbl.setText("Volcabulary:")
        self.definitionLbl.setText("Definition:")
        self.btnBox = QtWidgets.QDialogButtonBox(self)
        self.btnBox.setObjectName(u"buttonBox")
        self.btnBox.setGeometry(QtCore.QRect(490, 420, 441, 111))
        self.btnBox.setFont(font)
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet(btnSuccessStyle())
        self.btnBox.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet(btnDangerStyle())
        self.volcabularyTB.textChanged.connect(self.checkInputValid)
        self.definitionTB.textChanged.connect(self.checkInputValid)
        self.volcabularyTB.returnPressed.connect(self.btnBox.button(QtWidgets.QDialogButtonBox.Ok).click)
        self.definitionTB.returnPressed.connect(self.btnBox.button(QtWidgets.QDialogButtonBox.Ok).click)
    def closeEvent(self,event):
        self.btnBox.button(QtWidgets.QDialogButtonBox.Cancel).click()
    def checkInputValid(self):
        if not len(self.volcabularyTB.text()) or not len(self.definitionTB.text()):
            self.btnBox.button(QtWidgets.QDialogButtonBox.Ok).hide()
        else :
            self.btnBox.button(QtWidgets.QDialogButtonBox.Ok).show()
