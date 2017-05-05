#!/usr/bin/python3
# ...

"""
ZetCode PyQt5 Tutorial

In this example, we create a simple
window in PyQt5.

Author: Adam Fries
last edited: 05MAY2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

	app = QApplication(sys.argv)
	w = QWidget()
	w.resize(250,150)
	w.move(300,300)
	w.setWindowTitle('Simple Example')
	w.show()

	sys.exit(app.exec_())
