#!/usr/bin/python3

"""

ZetCode PyQt5 Tutorials

This example shows a tooltip on
a window and a button

author: Adam Fries
last edited: 04MAY2017

"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# Set Font for tooltops
		QToolTip.setFont(QFont('SansSerif',10))

		# Setup main window
		self.setToolTip('This is a <b>QWidget</b> widget')
		self.setGeometry(0,0,300,300)
		self.setWindowTitle('ToolTip Example')

		# Setup button
		btn = QPushButton('Button',self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		print("Button Width: ",btn.width())
		print("Window Width: ",self.width())
		# Center Button on main window
		btn.move((self.width()-btn.width())/2,(self.height()-btn.height())/2)

		# Display the window for user
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
sys.exit(app.exec_())
