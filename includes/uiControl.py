#!/usr/bin/python
#coding:utf-8
#Filename: test.py
#Created: 2014-01-02 02:45:15
#Author: Myon, myon.cn@gmail.com

from PyQt4 import QtGui,QtCore
from mainwindow import Ui_MainWindow
from PyQt4.QtCore import *
from filter import filterImages
 
class Widget(QtGui.QMainWindow, Ui_MainWindow):
	"""QtGui.QWidget和界面设计时选择的类型一致"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self) # Ui_Form.setupUi
		#checkbox连接信号
		self.cbWidth.stateChanged.connect(self.toggleGrpWidth)
		self.cbHeight.stateChanged.connect(self.toggleGrpHeight)
		self.cbRate.stateChanged.connect(self.toggleGrpRate)
		self.center()
		#去除标题栏边框等
		#self.setWindowFlags(Qt.FramelessWindowHint)
	#工作目录按钮点击事件
	@pyqtSignature("")
	def on_btnFileChoose_clicked(self):
		path=QtGui.QFileDialog.getExistingDirectory(None,u'选择要筛选的图片目录')
		if path != "":
			self.lbFilePath.setText(path)
	#输出目录按钮点击事件
	@pyqtSignature("")
	def on_btnOutputPath_clicked(self):
		outputPath=QtGui.QFileDialog.getExistingDirectory(None,u'选择输出目录')
		if outputPath!= "":
			self.lbOutputPath.setText(outputPath)
	
	#开始按钮点击时间
	@pyqtSignature("")
	def on_btnStart_clicked(self):
		if self.lbFilePath.text()==QtCore.QString(u'未选择筛选目录') or QtCore.QString(self.lbOutputPath.text()==u'未选择输出目录'):
			self.statusBar.showMessage(u"目录未选择！")
			return
		self.btnFileChoose.setEnabled(False)
		self.btnOutputPath.setEnabled(False)
		self.btnStart.setEnabled(False)
		#调用筛选图片类处理
		ft=filterImages(self)
		ft.doFilter(self)

	#checkbox状态转变事件
	def toggleGrpWidth(self):
		if self.cbWidth.isChecked():
			self.grpWidth.setEnabled(True)
		else:
			self.grpWidth.setEnabled(False)
	def toggleGrpHeight(self):
		if self.cbHeight.isChecked():
			self.grpHeight.setEnabled(True)
		else:
			self.grpHeight.setEnabled(False)
	def toggleGrpRate(self):
		if self.cbRate.isChecked():
			self.grpRate.setEnabled(True)
		else:
			self.grpRate.setEnabled(False)
	#窗口居中
	def center(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-self.height())/2)
