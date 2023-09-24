from editThisView import EditThisView
from vocabularyCardModel import Card
class EditThisController:
    def __init__(self, volcabularyCardAppOKReturn,volcabularyCardAppCancelReturn,volcabulary="",definition=""):
        self.view=EditThisView()
        self.volcabularyCardAppOKReturn=volcabularyCardAppOKReturn
        self.volcabularyCardAppCancelReturn=volcabularyCardAppCancelReturn
        self.view.btnBox.accepted.connect(self.accept)
        self.view.btnBox.rejected.connect(self.reject)
        self.view.volcabularyTB.setText(volcabulary)
        self.view.definitionTB.setText(definition)
        self.card=None
        self.view.show()
        self.view.exec_()
    def accept(self):
        self.card=Card(-1,self.view.volcabularyTB.text(),self.view.definitionTB.text())
        self.view.close()
        self.volcabularyCardAppOKReturn(self.card)
    def reject(self):
        self.view.close()
        self.volcabularyCardAppCancelReturn()
        