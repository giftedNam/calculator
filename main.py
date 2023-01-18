# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)

from PyQt5.QtGui import QIcon

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1=QPushButton('Message',self) # 버튼 1
        self.btn1.clicked.connect(self.activateMessage)

        self.btn2=QPushButton('Clear',self) # 버튼 2: 내역 지우기
        self.btn2.clicked.connect(self.clearMessage)

        hbox=QHBoxLayout() # 수평박스 레이아웃을 추가하고 버튼 1, 2 추가
        hbox.addStretch(1) # 공백
        hbox.addWidget(self.btn1) # 버튼 1 배치
        hbox.addWidget(self.btn2) # 버튼 2 배치

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        #vbox.addWidget(self.btn1)
        vbox.addLayout(hbox) # btn1 위치에 hbox를 배치
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def activateMessage(self):
        #QMessageBox.information(self,"information","Button clicked!")
        self.te1.appendPlainText("Button Clicked!")

    def clearMessage(self):
        self.te1.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
