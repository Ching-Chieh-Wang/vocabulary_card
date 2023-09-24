from loadOrCreateView import LoadOrCreateView
class LoadOrCreateController():
    def __init__(self,modelLoader):
        self.path=""
        self.modelLoader=modelLoader
        self.view=LoadOrCreateView()
        self.view.loadBtn.clicked.connect(self.load)
        self.view.createBtn.clicked.connect(self.create)
        self.view.show()
        self.view.exec_()
    def load(self):
        self.path=self.view.load()
        if self.path=="":
            return
        success,msg=self.modelLoader(self.path)
        if success:
            self.view.close()
        else:
            self.view.msg("Load Vocabulary DB Err",msg)
    def create(self):
        self.path=self.view.create()
        if self.path=="":
            return
        if self.modelLoader(self.path):
            self.view.close()
        
        

    