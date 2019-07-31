#from test import *
from InstagramAPI import InstagramAPI
import sys
import FileBrowser
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

import threading
import datetime
import time
import os


ProjectUI = "_uiFiles/InstaCraftUI.ui"



class MainDialog(QDialog):
    end = 1
    # player1_insta = ['', '']
    # player2_insta = ['', '']
    player1_insta_id = ''
    player1_insta_pw = ''
    player2_insta_id = ''
    player2_insta_pw = ''

    # global player1_insta_id
    # global player1_insta_pw
    # global player2_insta_id
    # global player2_insta_pw
    p1_id = player1_insta_id
    p1_pw = player1_insta_pw

    p2_id = player2_insta_id
    p2_pw = player2_insta_pw

    p1_pi = ''
    p2_pi = ''

    path_1 = ''
    path_2 = ''

    p1_api = InstagramAPI(p1_id, p1_pw)
    p2_api = InstagramAPI(p2_id, p2_pw)

    api = InstagramAPI("sample_id", "sample_pw")


    def __init__(self):
        QDialog.__init__(self)
        self.ui = uic.loadUi(ProjectUI, self)

        self.button_1 = self.ui.player1_picture_search

        self.ui.player1_picture_search.pressed.connect(self.OpenFileBrowser_1)
        self.ui.player2_picture_search.pressed.connect(self.OpenFileBrowser_2)

        self.ui.player1_pw.setEchoMode(QLineEdit.Password)
        self.ui.player2_pw.setEchoMode(QLineEdit.Password)

        self.ui.player1_login_button.pressed.connect(self.GetId_1)
        self.ui.player2_login_button.pressed.connect(self.GetId_2)
        self.ui.startbutton.pressed.connect(self.gamemode)

        self.ui.show()

    #@pyqtSlot()
    def OpenFileBrowser_1(self):
        fileBrowser = FileBrowser.FileDialog()
        global path_1
        path_1 = fileBrowser.openFileNameDialog()
        self.ui.player1_path.setText(path_1)
        global p1_pi
        p1_pi= path_1



    def OpenFileBrowser_2(self):
        fileBrowser = FileBrowser.FileDialog()
        global path_2
        path_2 = fileBrowser.openFileNameDialog()
        self.ui.player2_path.setText(path_2)
        global p2_pi
        p2_pi = path_2

    def GetId_1(self):
        # self.player1_insta[0] = self.ui.player1_id.text()
        # self.player1_insta[1] = self.ui.player1_pw.text()
        global player1_insta_id #= self.ui.player1_id.text()
        player1_insta_id = self.ui.player1_id.text()
        global player1_insta_pw# = self.ui.player1_pw.text()
        player1_insta_pw = self.ui.player1_pw.text()
        global p1_id
        global p1_pw
        p1_id = player1_insta_id
        p1_pw = player1_insta_pw
        print(p1_id)
        print(p1_pw)
        global p1_api
        p1_api = InstagramAPI(p1_id, p1_pw)


    def GetId_2(self):
        # self.player2_insta[0] = self.ui.player2_id.text()
        # self.player2_insta[1] = self.ui.player2_pw.text()
        global player2_insta_id# = self.ui.player2_id.text()
        player2_insta_id = self.ui.player2_id.text()
        global player2_insta_pw# = self.ui.player2_pw.text()
        player2_insta_pw = self.ui.player2_pw.text()
        global p2_id
        global p2_pw
        p2_id = player1_insta_id
        p2_pw = player1_insta_pw
        global p2_api
        p2_api = InstagramAPI(p2_id, p2_pw)
        # print(self.player2_insta[0])
        # print(self.player2_insta[1])

    #def Game_Start(self):
        #if


    #def function(self):
       # image_path = 'c:\image_path.jpg'  # path to your image file
        #self.show_frame_in_display(image_path)
    def gamemode(wl):
        # os.system("start")
        p3_sc = 0
        print("ready")
        for i in range(3):
            time.sleep(1)
            print(3 - i)
        time.sleep(1)
        print("start")

        sc1 = []

        now = time.time()
        future = now + 2

        while time.time() < future:
            innum = input()
            sc1.append(innum)

        p1_sc = len(sc1)
        print("stop")

        # print(p1_sc)

        time.sleep(3)

        print("ready")
        for i in range(3):
            time.sleep(1)

            print(3 - i)
        print("start")

        sc2 = []

        now = time.time()
        future = now + 2

        while time.time() < future:
            innum = input()
            sc2.append(innum)

        p2_sc = len(sc2) - p1_sc
        print("stop")
        # print(p2_sc)
        global end
        end = 0
        if (p1_sc > p2_sc):
            print("player1 win")
            print(end)
            return p1_sc
        elif (p1_sc < p2_sc):
            print("player2 win")
            print(end)
            return p2_sc
        else:
            print("draw")
            return p3_sc

    def check_time(curr_minute):
        # dt = datetime.datetime.now()
        gaming = gamemode(1)
        global p1_sc
        global p2_sc
        global p3_sc

        if (gaming == p1_sc):
            global api
            global p1_api
            global p2_api
            global p1_pi
            global p2_pi

            api = p2_api
            # 사진 경로 수정 필요
            photo_path_1 = p1_pi
            # 게시글 내용 수정 필요
            caption = "게임 벌칙으로 사진을 강제 업로드 합니다. - \"Instacraft\""
            api.uploadPhoto(photo=photo_path_1, caption=caption, upload_id=None)
            print("Upload succes!")

        elif (gaming == p2_sc):
            # global api
            # global p1_api
            # global p2_api

            api = p1_api

            # 사진 경로 수정 필요
            photo_path_2 = p2_pi
            # 게시글 내용 수정 필요
            caption = "게임 벌칙으로 사진을 강제 업로드 합니다. - \"Instacraft\""
            api.uploadPhoto(photo=photo_path_2, caption=caption, upload_id=None)
            print("Upload succes!")

        elif (gaming == p3_sc):
            # global api
            # global p1_api
            # global p2_api

            print("draw, don't upload")

        threading.Timer(1, check_time, args=[curr_minute]).start()


    if(end == 0):
        if (api.login()):

            api.getSelfUserFeed()  # get self user feed

            print(api.LastJson)  # print last response JSON

            print("Login succes!")

        else:

            print("Can't login!")
            exit()

        check_time(-1)





if __name__=="__main__":
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    sys.exit(app.exec_())

