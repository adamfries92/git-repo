#!/usr/bin/python3

"""

ZetCode PyQt5 Tutorials

This program creates a quit
button. When we press the button,
the application terminates.

Author: Adam Fries
Last Edited: 04MAY2017

"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Set Font for tooltops
        QToolTip.setFont(QFont('SansSerif',10))

        # Setup main window
        self.setGeometry(0,0,300,300)
        self.setWindowTitle('Closing a Window Example')
        self.setToolTip('This is the main window (QWidget)')

        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('Careful! If you press me, I go poof!')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move((self.width()-qbtn.width())/2,(self.height()-qbtn.height())/2)

        # Show the application to the user
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
