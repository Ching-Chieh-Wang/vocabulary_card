from PyQt5 import QtCore, QtWidgets, QtGui
from stylesheets import btnSuccessOutlineStyle
class LoadOrCreateView(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('vocabularyCard.png'))
        self.setWindowTitle("Load or Create Vocabulary Database")
        self.setGeometry(200, 200, 500, 400)
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        self.loadBtn = QtWidgets.QPushButton("Load", self)
        self.loadBtn.setStyleSheet(btnSuccessOutlineStyle())
        self.createBtn = QtWidgets.QPushButton("Create", self)
        self.createBtn.setStyleSheet(btnSuccessOutlineStyle())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadBtn.sizePolicy().hasHeightForWidth())
        self.loadBtn.setSizePolicy(sizePolicy)
        sizePolicy.setHeightForWidth(self.createBtn.sizePolicy().hasHeightForWidth())
        self.createBtn.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.loadBtn.setFont(font)
        self.createBtn.setFont(font)
        
        # Add buttons to the layout
        layout.addWidget(self.loadBtn)
        layout.addWidget(self.createBtn)
        
        # Set the layout for the dialog
        self.setLayout(layout)
    def load(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Vocabulary Database ", "", "Database Files (*.db)",)
        return path
    def create(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Create New Vocabulary Database", "", "Database Files (*.db)")
        return path
    def msg(self,title,text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setMinimumSize(800, 600)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.exec_()


