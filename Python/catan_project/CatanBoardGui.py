# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CatanBoardDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import CatanGuiSupport

class CatanUI(object):
    def setupUi(self, CatanGUI):
        CatanGUI.setObjectName("CatanGUI")
        CatanGUI.resize(949, 766)
        self.centralwidget = QtWidgets.QWidget(CatanGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 651, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gameBoardLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.gameBoardLayout.setContentsMargins(0, 0, 0, 0)
        self.gameBoardLayout.setObjectName("gameBoardLayout")
        self.gameBoardView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.gameBoardView.setObjectName("gameBoardView")
        self.gameBoardLayout.addWidget(self.gameBoardView)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(730, 60, 191, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.buttonsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.statsDisplay = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.statsDisplay.setFont(font)
        self.statsDisplay.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.statsDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.statsDisplay.setObjectName("statsDisplay")
        self.buttonsLayout.addWidget(self.statsDisplay)
        self.genBoardButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.genBoardButton.setObjectName("genBoardButton")
        self.buttonsLayout.addWidget(self.genBoardButton)
        self.playButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.playButton.setObjectName("playButton")
        self.buttonsLayout.addWidget(self.playButton)
        CatanGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CatanGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 21))
        self.menubar.setObjectName("menubar")
        CatanGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CatanGUI)
        self.statusbar.setObjectName("statusbar")
        CatanGUI.setStatusBar(self.statusbar)

        self.retranslateUi(CatanGUI)
        QtCore.QMetaObject.connectSlotsByName(CatanGUI)

    def retranslateUi(self, CatanGUI):
        _translate = QtCore.QCoreApplication.translate
        CatanGUI.setWindowTitle(_translate("CatanGUI", "CatanGUI"))
        self.statsDisplay.setText(_translate("CatanGUI", "CATAN"))
        self.genBoardButton.setText(_translate("CatanGUI", "Generate Board"))
        self.playButton.setText(_translate("CatanGUI", "Play Game"))



if __name__ == "__main__":
    import sys
    sys._excepthook = sys.excepthook
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = exception_hook
    
    app = QtWidgets.QApplication(sys.argv)
    ui = CatanUI()
    CatanGUI = CatanGuiSupport.GUIWindow(ui)
    CatanGUI.show()
    sys.exit(app.exec())
