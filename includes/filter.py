#!/usr/bin/python
#coding:utf-8
#Filename: filter.py
#Created: 2014-01-02 15:00:21
#Author: Myon, myon.cn@gmail.com
#desc:	筛选图片模块，处理开始按钮点击事件

import re
import sys
import Image
import os
import shutil
reload(sys)
sys.setdefaultencoding( "utf-8" )
#from PyQt4 import QtGui,QtCore
class filterImages():
	def __init__(self,MainWindow):
		#获得路径
		self.workPath=unicode(MainWindow.lbFilePath.text())+os.sep
		self.outputPath=unicode(MainWindow.lbOutputPath.text())+os.sep
		#是否选择宽度高度比例选项
		self.isWidth=MainWindow.cbWidth.isChecked()
		self.isHeight=MainWindow.cbHeight.isChecked()
		self.isRate=MainWindow.cbRate.isChecked()
		#判断大于还是小于,并获取值
		if self.isWidth:
			#获得图片宽度
			self.width=MainWindow.sbWidth.value()
			if MainWindow.rbWidthGt.isChecked():
				self.isWidthType=1
			elif MainWindow.rbWidthEq.isChecked():
				self.isWidthType=0
			else:
				self.isWidthType=-1
		if self.isHeight:
			#获得图片高度
			self.height=MainWindow.sbHeight.value()
			if MainWindow.rbHeightGt.isChecked():
				self.isHeightType=1
			elif MainWindow.rbHeightEq.isChecked():
				self.isHeightType=0
			else:
				self.isHeightType=-1
		if self.isRate:
			#获得比例宽高以及浮动值
			self.r_Width=MainWindow.sbRateWidth.value()
			self.r_Height=MainWindow.sbRateHeight.value()
			self.r_RateValue=MainWindow.sbRateValue.value()
			self.rate=float(self.r_Width)/self.r_Height
	def doFilter(self,MainWindow):
		count=0
		filterCount=0
		for root,dirs,files in os.walk(self.workPath):
			for fn in files:
				count+=1
				cfile=unicode(os.path.join(root,fn))
				#在状态栏显示输出
				MainWindow.statusBar.showMessage(str(filterCount)+"/"+str(count))
				#判断是否是图片类型
				if not re.match(r'.+\.(jpg|gif|png|bmp)$',cfile):
					continue
				#判断文件是否存在
				if not os.path.isfile(cfile):
					continue
				#如果不是图片，抛出异常
				try:
					im=Image.open(cfile)
				except:
					continue
				width=im.size[0]
				height=im.size[1]
				#筛选方法：如果不满足条件就跳出本次循环，没有跳出的就是筛选出来的图片
				if self.isWidth:
					if self.isWidthType==1:
						if self.width>width:
							continue
					elif self.isWidthType==0:
						if self.width!=width:
							continue
					elif self.width<width:
							continue
				if self.isHeight:
					if self.isHeightType==1:
						if self.height>height:
							continue
					elif self.isHeightType==0:
						if self.height!=height:
							continue
					elif self.height<height:
							continue
				if self.isRate:
					#当前图片比例
					rate=float(width)/height
					if not ((self.rate-self.r_RateValue)<rate and (self.rate+self.r_RateValue)>rate):
						continue
				#此处操作满足条件的图片
				#复制文件到输出文件夹
				try:
					shutil.copy(cfile,self.outputPath)
				except:
					continue
				filterCount+=1
				print width,height,cfile
		#回复按钮可点击状态
		MainWindow.btnFileChoose.setEnabled(True)
		MainWindow.btnOutputPath.setEnabled(True)
		MainWindow.btnStart.setEnabled(True)
