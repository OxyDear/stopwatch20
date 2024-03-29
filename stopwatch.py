# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'sec.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setMaximumSize(QtCore.QSize(400, 200))
        MainWindow.setStyleSheet("background-color: rgb(22, 22, 22);\n"
                                 "color: rgb(255, 255, 255);")
        self.isPlaying = True
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(140, 30, 118, 24))
        self.timeEdit.setAccessibleDescription("")
        self.timeEdit.setAutoFillBackground(False)
        self.timeEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 121, 131, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "background-color: #FFFFFF;\n"
                                      "border-radius: 10px;"
                                      "color: rgb(0, 0, 0);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(228, 228, 228);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgb(200, 200, 200);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.player = QMediaPlayer()

        self.add_functions()

    def timerLabel(self):
        self.label.setGeometry(QtCore.QRect(0, -10, 400, 200))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("text-align: center;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2.setGeometry(QtCore.QRect(0, 150, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText('Reset')
        self.pushButton_2.setStyleSheet("border-radius: 10px;")
        self.pushButton_3.setGeometry(QtCore.QRect(290, 150, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText('Again')
        self.pushButton_3.setStyleSheet("border-radius: 10px;")

        # self.p = multiprocessing.Process(target=playsound, args=("sounds/buzzer.mp3",))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Useful Stopwatch"))
        self.pushButton.setText(_translate("MainWindow", "Set Time"))
        # self.label.setText(_translate("MainWindow", "0:0"))

    def add_functions(self):
        self.pushButton.clicked.connect(lambda: self.setTime())
        self.pushButton_2.clicked.connect(lambda: self.setReset())
        self.pushButton_3.clicked.connect(lambda: self.setAgain())

    def playAudio(self):
        full_file_path = os.path.join(os.getcwd(), 'buzzer.mp3')
        print(full_file_path)
        url = QtCore.QUrl.fromLocalFile(full_file_path)
        print(url)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(10)
        self.player.play()

    def setAgain(self):
        self.mi = self.timeEdit.time().hour()
        self.se = self.timeEdit.time().minute()
        if len(str(self.mi)) == 1 and len(str(self.se)) == 1:
            label = '0' + str(self.mi) + ':0' + str(self.se)
        elif len(str(self.mi)) == 1:
            label = '0' + str(self.mi) + ':' + str(self.se)
        elif len(str(self.se)) == 1:
            label = str(self.mi) + ':0' + str(self.se)
        else:
            label = str(self.mi) + ':' + str(self.se)
        self.timerLabel()
        self.label.setText(label)

    def setReset(self):
        self.isPlaying = False
        self.player.stop()
        self.label.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.timeEdit.show()
        self.pushButton.show()

    def setTime(self):
        self.isPlaying = True
        self.mi = self.timeEdit.time().hour()
        self.se = self.timeEdit.time().minute()
        self.displayTimer()
        self.timeEdit.hide()
        self.pushButton.hide()
        self.label.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.t = QtCore.QTimer()
        self.t.timeout.connect(lambda: self.displayTimer())
        self.t.start(1000)

    def displayTimer(self):
        if len(str(self.mi)) == 1 and len(str(self.se)) == 1:
            label = '0' + str(self.mi) + ':0' + str(self.se)
        elif len(str(self.mi)) == 1:
            label = '0' + str(self.mi) + ':' + str(self.se)
        elif len(str(self.se)) == 1:
            label = str(self.mi) + ':0' + str(self.se)
        else:
            label = str(self.mi) + ':' + str(self.se)
        if self.mi == 0 and self.se == 0:
            self.label.setText('STOP')
            if self.isPlaying: self.playAudio()
        elif self.se == 0:
            self.se = 59
            self.mi -= 1
            self.label.setText(label)
        else:
            self.se -= 1
            self.label.setText(label)
        self.timerLabel()

    # def setLabel(self, startTime, label='0:0'):
    #     label = str(self.timeEdit.time().hour()) + ':' + str(self.timeEdit.time().minute())
    #     self.timerLabel()
    #     self.label.setText(label)
    #     self.timeEdit.hide()
    #     min = 0
    #     sec = 0
    #     while True:
    #         now = datetime.now()
    #         print((now - startTime).seconds)
    #         if self.timeEdit.time().minute() - (now - startTime).seconds + sec < 0:
    #             min += 1
    #             sec += 60
    #         label = str(self.timeEdit.time().hour() - min) + ':' + str(
    #             self.timeEdit.time().minute() - (now - startTime).seconds + sec)
    #         self.label.setText(label)
    #         self.label.repaint()
    #         print(self.label.text())
    #
    #         if label.split(':') == ['0', '0']:
    #             break


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    timer = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(timer)
    timer.show()
    sys.exit(app.exec_())
