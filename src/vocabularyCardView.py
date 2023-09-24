
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent  



class VocabularyCardView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('vocabularyCard.png'))
        self.setObjectName("Vocabulary Card")
        self.resize(1500, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(1500, 750))
        self.setMaximumSize(QtCore.QSize(3000, 1500))
        self.gridLayout_8 = QtWidgets.QGridLayout(self)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.showHideBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showHideBtn.sizePolicy().hasHeightForWidth())
        self.showHideBtn.setSizePolicy(sizePolicy)
        self.showHideBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.showHideBtn.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.showHideBtn.setFont(font)
        self.showHideBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.showHideBtn.setObjectName("showHideBtn")
        self.gridLayout_10.addWidget(self.showHideBtn, 1, 0, 1, 1)
        self.alwaysShowBox = QtWidgets.QCheckBox(self)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.alwaysShowBox.setFont(font)
        self.alwaysShowBox.setStyleSheet("")
        self.alwaysShowBox.setObjectName("alwaysShowBox")
        self.gridLayout_10.addWidget(self.alwaysShowBox, 2, 0, 1, 1)
        self.previousBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousBtn.sizePolicy().hasHeightForWidth())
        self.previousBtn.setSizePolicy(sizePolicy)
        self.previousBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.previousBtn.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.previousBtn.setFont(font)
        self.previousBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.previousBtn.setObjectName("previousBtn")
        self.gridLayout_7.addWidget(self.previousBtn, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 4, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        self.nextBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.nextBtn.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.nextBtn.setFont(font)
        self.nextBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout_7.addWidget(self.nextBtn, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 1, 1, 1)
        
        self.gridLayout_7.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 6, 0, 1, 1)
        self.vocabularyLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vocabularyLbl.sizePolicy().hasHeightForWidth())
        self.vocabularyLbl.setSizePolicy(sizePolicy)
        self.vocabularyLbl.setMinimumSize(QtCore.QSize(0, 140))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.vocabularyLbl.setFont(font)
        self.vocabularyLbl.setObjectName("vocabularyLbl")
        self.gridLayout_4.addWidget(self.vocabularyLbl, 2, 0, 1, 1)
        self.definitionLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.definitionLbl.sizePolicy().hasHeightForWidth())
        sizePolicy.setRetainSizeWhenHidden(True);
        self.definitionLbl.setSizePolicy(sizePolicy)
        self.definitionLbl.setMinimumSize(QtCore.QSize(0, 140))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.definitionLbl.setFont(font)
        self.definitionLbl.setObjectName("definitionLbl")
        self.gridLayout_4.addWidget(self.definitionLbl, 3, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.rememberBox = QtWidgets.QCheckBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rememberBox.sizePolicy().hasHeightForWidth())
        self.rememberBox.setSizePolicy(sizePolicy)
        self.rememberBox.setMinimumSize(QtCore.QSize(0, 40))
        self.rememberBox.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.rememberBox.setFont(font)
        self.rememberBox.setObjectName("rememberBox")
        self.gridLayout_5.addWidget(self.rememberBox, 0, 2, 1, 1)
        self.star2Box = QtWidgets.QCheckBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star2Box.sizePolicy().hasHeightForWidth())
        self.star2Box.setSizePolicy(sizePolicy)
        self.star2Box.setMinimumSize(QtCore.QSize(0, 40))
        self.star2Box.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.star2Box.setFont(font)
        self.star2Box.setObjectName("star2Box")
        self.gridLayout_5.addWidget(self.star2Box, 0, 1, 1, 1)
        self.shuffleBox = QtWidgets.QCheckBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shuffleBox.sizePolicy().hasHeightForWidth())
        self.shuffleBox.setSizePolicy(sizePolicy)
        self.shuffleBox.setMinimumSize(QtCore.QSize(0, 40))
        self.shuffleBox.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.shuffleBox.setFont(font)
        self.shuffleBox.setObjectName("shuffleBox")
        self.gridLayout_5.addWidget(self.shuffleBox, 0, 3, 1, 1)
        self.star1Box = QtWidgets.QCheckBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star1Box.sizePolicy().hasHeightForWidth())
        self.star1Box.setSizePolicy(sizePolicy)
        self.star1Box.setMinimumSize(QtCore.QSize(0, 40))
        self.star1Box.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.star1Box.setFont(font)
        self.star1Box.setObjectName("star1Box")
        self.gridLayout_5.addWidget(self.star1Box, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.goTB = QtWidgets.QLineEdit(self)
        self.goTB.setAlignment(QtCore.Qt.AlignCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goTB.sizePolicy().hasHeightForWidth())
        self.goTB.setSizePolicy(sizePolicy)
        self.goTB.setMinimumSize(QtCore.QSize(70, 50))
        self.goTB.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.goTB.setFont(font)
        self.goTB.setStyleSheet("QLineEdit {\n"
"            border: 2px solid #cccccc;\n"
"            border-radius: 15px; /* Adjust the border-radius to make the QLineEdit more rounded */\n"
"        }")
        self.goTB.setObjectName("goTB")
        self.gridLayout_9.addWidget(self.goTB, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(0, 50, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 0, 2, 1, 1)
        self.numLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numLbl.sizePolicy().hasHeightForWidth())
        self.numLbl.setSizePolicy(sizePolicy)
        self.numLbl.setMinimumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        font.setItalic(False)
        self.numLbl.setFont(font)
        self.numLbl.setObjectName("numLbl")
        self.gridLayout_9.addWidget(self.numLbl, 0, 1, 1, 1)
        self.goBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goBtn.sizePolicy().hasHeightForWidth())
        self.goBtn.setSizePolicy(sizePolicy)
        self.goBtn.setMinimumSize(QtCore.QSize(40, 50))
        self.goBtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.goBtn.setFont(font)
        self.goBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #28a745; /* Success color */\n"
"            border: 2px solid #28a745; /* Success color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #28a745; /* Success color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #1c7430; /* Darker success color on pressed */\n"
"            border: 2px solid #1c7430; /* Darker success color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #b0b0b0; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.goBtn.setObjectName("goBtn")
        self.gridLayout_9.addWidget(self.goBtn, 0, 5, 1, 1)
        self.goLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goLbl.sizePolicy().hasHeightForWidth())
        self.goLbl.setSizePolicy(sizePolicy)
        self.goLbl.setMinimumSize(QtCore.QSize(0, 50))
        self.goLbl.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.goLbl.setFont(font)
        self.goLbl.setObjectName("goLbl")
        self.gridLayout_9.addWidget(self.goLbl, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem4, 5, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.searchTB = QtWidgets.QLineEdit(self)
        self.searchTB.setAlignment(QtCore.Qt.AlignCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchTB.sizePolicy().hasHeightForWidth())
        self.searchTB.setSizePolicy(sizePolicy)
        self.searchTB.setMinimumSize(QtCore.QSize(0, 50))
        self.searchTB.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.searchTB.setFont(font)
        self.searchTB.setStyleSheet("QLineEdit {\n"
"            border: 2px solid #cccccc;\n"
"            border-radius: 15px; /* Adjust the border-radius to make the QLineEdit more rounded */\n"
"        }")
        self.searchTB.setObjectName("searchTB")
        self.gridLayout_6.addWidget(self.searchTB, 0, 1, 1, 1)
        self.searchLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLbl.sizePolicy().hasHeightForWidth())
        self.searchLbl.setSizePolicy(sizePolicy)
        self.searchLbl.setMinimumSize(QtCore.QSize(190, 50))
        self.searchLbl.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.searchLbl.setFont(font)
        self.searchLbl.setObjectName("searchLbl")
        self.gridLayout_6.addWidget(self.searchLbl, 0, 0, 1, 1)
        self.searchBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setMinimumSize(QtCore.QSize(150, 50))
        self.searchBtn.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.searchBtn.setFont(font)
        self.searchBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #28a745; /* Success color */\n"
"            border: 2px solid #28a745; /* Success color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #28a745; /* Success color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #1c7430; /* Darker success color on pressed */\n"
"            border: 2px solid #1c7430; /* Darker success color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #b0b0b0; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.searchBtn.setObjectName("searchBtn")
        self.gridLayout_6.addWidget(self.searchBtn, 0, 2, 1, 1)
        self.resetBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetBtn.sizePolicy().hasHeightForWidth())
        self.resetBtn.setSizePolicy(sizePolicy)
        self.resetBtn.setMinimumSize(QtCore.QSize(150, 50))
        self.resetBtn.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.resetBtn.setFont(font)
        self.resetBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #28a745; /* Success color */\n"
"            border: 2px solid #28a745; /* Success color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #28a745; /* Success color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #1c7430; /* Darker success color on pressed */\n"
"            border: 2px solid #1c7430; /* Darker success color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #b0b0b0; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.resetBtn.setObjectName("resetBtn")
        self.gridLayout_6.addWidget(self.resetBtn, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.line_2 = QtWidgets.QFrame(self)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.star1sRBtn = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star1sRBtn.sizePolicy().hasHeightForWidth())
        self.star1sRBtn.setSizePolicy(sizePolicy)
        self.star1sRBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.star1sRBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.star1sRBtn.setFont(font)
        self.star1sRBtn.setObjectName("star1sRBtn")
        self.gridLayout.addWidget(self.star1sRBtn, 1, 0, 1, 1)
        self.cambridgeBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cambridgeBtn.sizePolicy().hasHeightForWidth())
        self.cambridgeBtn.setSizePolicy(sizePolicy)
        self.cambridgeBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.cambridgeBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.cambridgeBtn.setFont(font)
        self.cambridgeBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.cambridgeBtn.setObjectName("cambridgeBtn")
        self.gridLayout.addWidget(self.cambridgeBtn, 4, 0, 1, 1)
        self.loadOrCreateBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadOrCreateBtn.sizePolicy().hasHeightForWidth())
        self.loadOrCreateBtn.setSizePolicy(sizePolicy)
        self.loadOrCreateBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.loadOrCreateBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.loadOrCreateBtn.setFont(font)
        self.loadOrCreateBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.loadOrCreateBtn.setObjectName("loadOrCreateBtn")
        self.gridLayout.addWidget(self.loadOrCreateBtn, 9, 0, 1, 1)
        self.sequentialRBtn = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sequentialRBtn.sizePolicy().hasHeightForWidth())
        self.sequentialRBtn.setSizePolicy(sizePolicy)
        self.sequentialRBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.sequentialRBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.sequentialRBtn.setFont(font)
        self.sequentialRBtn.setObjectName("sequentialRBtn")
        self.gridLayout.addWidget(self.sequentialRBtn, 0, 0, 1, 1)
        self.nonRememberRBtn = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nonRememberRBtn.sizePolicy().hasHeightForWidth())
        self.nonRememberRBtn.setSizePolicy(sizePolicy)
        self.nonRememberRBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.nonRememberRBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.nonRememberRBtn.setFont(font)
        self.nonRememberRBtn.setObjectName("nonRememberRBtn")
        self.gridLayout.addWidget(self.nonRememberRBtn, 3, 0, 1, 1)
        self.copyBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyBtn.sizePolicy().hasHeightForWidth())
        self.copyBtn.setSizePolicy(sizePolicy)
        self.copyBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.copyBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.copyBtn.setFont(font)
        self.copyBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.copyBtn.setObjectName("copyBtn")
        self.gridLayout.addWidget(self.copyBtn, 6, 0, 1, 1)
        self.editAllBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editAllBtn.sizePolicy().hasHeightForWidth())
        self.editAllBtn.setSizePolicy(sizePolicy)
        self.editAllBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.editAllBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.editAllBtn.setFont(font)
        self.editAllBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.editAllBtn.setObjectName("editAllBtn")
        self.gridLayout.addWidget(self.editAllBtn, 8, 0, 1, 1)
        self.star2sRBtn = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star2sRBtn.sizePolicy().hasHeightForWidth())
        self.star2sRBtn.setSizePolicy(sizePolicy)
        self.star2sRBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.star2sRBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.star2sRBtn.setFont(font)
        self.star2sRBtn.setObjectName("star2sRBtn")
        self.gridLayout.addWidget(self.star2sRBtn, 2, 0, 1, 1)
        self.pronounciationBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pronounciationBtn.sizePolicy().hasHeightForWidth())
        self.pronounciationBtn.setSizePolicy(sizePolicy)
        self.pronounciationBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.pronounciationBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.pronounciationBtn.setFont(font)
        self.pronounciationBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.pronounciationBtn.setObjectName("pronounciationBtn")
        self.gridLayout.addWidget(self.pronounciationBtn, 5, 0, 1, 1)
        self.editThisBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editThisBtn.sizePolicy().hasHeightForWidth())
        self.editThisBtn.setSizePolicy(sizePolicy)
        self.editThisBtn.setMinimumSize(QtCore.QSize(60, 0))
        self.editThisBtn.setMaximumSize(QtCore.QSize(460, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(20)
        self.editThisBtn.setFont(font)
        self.editThisBtn.setStyleSheet("QPushButton {\n"
"            background-color: transparent;\n"
"            color: #17a2b8; /* Info color */\n"
"            border: 2px solid #17a2b8; /* Info color for the border */\n"
"            border-radius: 5px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #17a2b8; /* Info color on hover */\n"
"            color: #ffffff; /* White text color on hover */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #138496; /* Darker info color on pressed */\n"
"            border: 2px solid #138496; /* Darker info color for the border on pressed */\n"
"        }\n"
"        QPushButton:disabled {\n"
"            background-color: transparent; /* Transparent background when disabled */\n"
"            color: #9BA4B5; /* Lighter text color when disabled */\n"
"            border: 2px solid #b0b0b0; /* Lighter border color when disabled */\n"
"        }")
        self.editThisBtn.setObjectName("editThisBtn")
        self.gridLayout.addWidget(self.editThisBtn, 7, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.goTB.setValidator(QtGui.QIntValidator())
        self.showHideBtn.clicked.connect(self.showHideDefinition)
        self.goTB.returnPressed.connect(self.goBtn.click)
        self.searchTB.returnPressed.connect(self.searchBtn.click)
        self.show()
        self.setWindowTitle("vocabulary Card")
        self.goLbl.setText("Go:")
        self.numLbl.setText("number")
        self.searchBtn.setText("Search")
        self.searchLbl.setText("Search")
        self.resetBtn.setText("Reset")
        self.goBtn.setText("Go")
        self.vocabularyLbl.setText("(Empty)")
        self.definitionLbl.setText("(empty)")
        self.sequentialRBtn.setText("Sequential")
        self.star1sRBtn.setText("Star1s")
        self.star2sRBtn.setText("Star2s")
        self.nonRememberRBtn.setText("Non-Remember")
        self.cambridgeBtn.setText("Cambridge")
        self.pronounciationBtn.setText("Pronounciation")
        self.copyBtn.setText("Copy")
        self.editThisBtn.setText("Edit This")
        self.editAllBtn.setText("Edit All")
        self.loadOrCreateBtn.setText("Load/New")
        self.previousBtn.setText("<<")
        self.nextBtn.setText(">>")
        self.star1Box.setText("Star1")
        self.star2Box.setText("Star2")
        self.rememberBox.setText("Remember")
        self.shuffleBox.setText("Shuffle")
        self.showHideBtn.setText("Show / Hide")
        self.alwaysShowBox.setText("Always Show")
        key = QtWidgets.QShortcut(QtGui.QKeySequence("right"),self)
        key.activated.connect(lambda : self.nextBtn.click())
        key = QtWidgets.QShortcut(QtGui.QKeySequence("left"),self)
        key.activated.connect(lambda : self.previousBtn.click())
        key = QtWidgets.QShortcut(QtGui.QKeySequence("1"),self)
        key.activated.connect(lambda : self.star1Box.click())
        key = QtWidgets.QShortcut(QtGui.QKeySequence("2"),self)
        key.activated.connect(lambda : self.star2Box.click())
        key = QtWidgets.QShortcut(QtGui.QKeySequence("r"),self)
        key.activated.connect(lambda : self.star2Box.click())
        key = QtWidgets.QShortcut(QtGui.QKeySequence("p"),self)
        key.activated.connect(lambda : self.pronounciationBtn.click())
        key = QtWidgets.QShortcut(QtGui.QKeySequence(" "),self)
        key.activated.connect(lambda : self.showHideBtn.click())
        key = QtWidgets.QShortcut(QtGui.QKeySequence("a"),self)
        key.activated.connect(lambda : self.alwaysShowBox.click())
        
        
    def showCard(self,card,currentIdx,cardNums):
        if(card==None):
            self.previousBtn.setDisabled(True)
            self.nextBtn.setDisabled(True)
            self.star1Box.setChecked(False)
            self.star1Box.setChecked(False)
            self.star2Box.setChecked(False)
            self.rememberBox.setChecked(False)
            self.shuffleBox.setChecked(False)
            self.star1Box.setDisabled(True)
            self.star2Box.setDisabled(True)
            self.rememberBox.setDisabled(True)
            self.shuffleBox.setDisabled(True)
            self.editThisBtn.setDisabled(True)
            self.goBtn.setDisabled(True)
            self.numLbl.setText("0/0")
            self.vocabularyLbl.setText("(empty)")
            self.definitionLbl.setText("(empty)")
            self.cambridgeBtn.setDisabled(True)
            self.pronounciationBtn.setDisabled(True)
            self.copyBtn.setDisabled(True)
                
        else:  
            self.star1Box.setDisabled(False)
            self.star2Box.setDisabled(False)
            self.rememberBox.setDisabled(False)
            self.shuffleBox.setDisabled(False)
            self.editThisBtn.setDisabled(False)
            self.cambridgeBtn.setDisabled(False)
            self.pronounciationBtn.setDisabled(False)
            self.copyBtn.setDisabled(False)
            self.goBtn.setDisabled(self.goTB.text()=="" or int(self.goTB.text())>cardNums)
            self.previousBtn.setDisabled(currentIdx==1)
            self.nextBtn.setDisabled(currentIdx==cardNums)
            self.numLbl.setText("{}/{}--({})".format(currentIdx,cardNums,card.idx))
            self.vocabularyLbl.setText(card.vocabulary)
            self.definitionLbl.setText(card.definition)
            self.star1Box.setChecked(card.star1)
            self.star2Box.setChecked(card.star2)
            self.rememberBox.setChecked(card.remember)
        if self.alwaysShowBox.isChecked():
            self.definitionLbl.show()
        else:
            self.definitionLbl.hide()
    def showHideDefinition(self):
        if self.definitionLbl.isHidden():
            self.definitionLbl.show()
        else:
            self.definitionLbl.hide()
    def wheelEvent(self,event):
        if event.angleDelta().y()<0:
            self.nextBtn.click()
        else:
            self.previousBtn.click()
    def mousePressEvent(self, event):
        if event.button()==1:
            self.showHideBtn.click()
        if event.button()==QtCore.Qt.MiddleButton:
            self.alwaysShowBox.click()
    def msg(self,title,text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setMinimumSize(800, 600)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.exec_()
    def pronounciate(self):
        self.media_player = QMediaPlayer(self)
        url = QtCore.QUrl.fromLocalFile("pronounciation.mp3")
        media_content = QMediaContent(url)
        self.media_player.setMedia(media_content)
        self.media_player.play()
        self.pronounciationBtn.setDisabled(True)
        self.media_player.stateChanged.connect(self.pronounciated)
    def pronounciated(self):
        self.media_player.setMedia(QMediaContent())
        self.pronounciationBtn.setDisabled(False)
    def prnounceFailed(self):
        self.msg('Error','Check Internet connection or vocabulary spelling')
            

        