#!/usr/bin/python
#coding:utf-8
#Filename: main.py
#Created: 2014-01-03 00:41:26
#Author: Myon, myon.cn@gmail.com

import sys
sys.path.append('includes')
from uiControl import Widget
from PyQt4 import QtGui


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	widget = Widget()
	widget.show()
	sys.exit(app.exec_())
