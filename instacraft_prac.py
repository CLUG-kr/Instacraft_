import sys
import FileBrowser
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

ProjectUI = "_uiFiles/InstaCraftUI.ui"


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = uic.loadUi(ProjectUI, self)

        self.button_1 = self.ui.player1_picture_search
        self.path_1 = ''
        self.path_2 = ''
        self.ui.player1_picture_search.pressed.connect(self.OpenFileBrowser_1)
        self.ui.player2_picture_search.pressed.connect(self.OpenFileBrowser_2)
        #self.Id_1 = self.ui.player1_id()
        #self.Pw_1 = self.ui.player1_pw()
        #self.Id_2 = self.ui.player2_id()
        #self.Pw_2 = self.ui.player2_pw()
        self.ui.player1_pw.setEchoMode(QLineEdit.Password)
        self.ui.player2_pw.setEchoMode(QLineEdit.Password)
        self.player1_insta = ['', '']
        self.player2_insta = ['', '']
        self.ui.player1_login_button.pressed.connect(self.GetId_1)
        self.ui.player2_login_button.pressed.connect(self.GetId_2)
        #self.ui.startbutton.pressed.connect(self.gamemode)
        self.ui.show()

    #@pyqtSlot()
    def OpenFileBrowser_1(self):
        fileBrowser = FileBrowser.FileDialog()
        self.path_1 = fileBrowser.openFileNameDialog()
        self.ui.player1_path.setText(self.path_1)

    def OpenFileBrowser_2(self):
        fileBrowser = FileBrowser.FileDialog()
        self.path_2 = fileBrowser.openFileNameDialog()
        self.ui.player2_path.setText(self.path_2)

    def GetId_1(self):
        self.player1_insta[0] = self.ui.player1_id.text()
        self.player1_insta[1] = self.ui.player1_pw.text()
        print(self.player1_insta[0])
        print(self.player1_insta[1])

    def GetId_2(self):
        self.player2_insta[0] = self.ui.player2_id.text()
        self.player2_insta[1] = self.ui.player2_pw.text()
        print(self.player2_insta[0])
        print(self.player2_insta[1])

    #def Game_Start(self):
        #if


    #def function(self):
       # image_path = 'c:\image_path.jpg'  # path to your image file
        #self.show_frame_in_display(image_path)




if __name__=="__main__":
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    sys.exit(app.exec_())

