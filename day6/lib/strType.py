#!/usr/bin/env python3
#encoding: utf-8
# -*- coding: utf-8 -*-

__author__ = 'editrobot'

import os
import platform
import random
from datetime import datetime
import subprocess
import time
import sys

class strType_class(object):
	def __init__(self,str=""):
		self.str = str
		
	@property
	def str(self):
		return self._str
	@str.setter
	def str(self,value):
		self.method_status_init()
		self._str = value
		self.method_AnalysisStatus()
		self.method_run()

	def method_status_init(self):
		self._str = ""
		self._str_list = []
		self.status = {
			"str_len":0,
			"symbol":"+",
			"symbol_count":0,
			"Integer":0,
			"Integer_count":0,
			"Decimal_point_count":0,
			"Decimal":0,
			"Decimal_count":0,
			"letter_count":0
		}
		self.result = {
			"Type" : "intnum",
			"value" : 0,
		}
	
	def method_AnalysisStatus(self):
		for word in self.str:
			self._str_list.append(word)
			if word == "+" or word == "-":
				self.status["symbol_count"] += 1
				self.status["symbol"] = word
			elif word == ".":
				self.status["Decimal_point_count"] += 1
			elif word.isdigit() == True and self.status["Decimal_point_count"] == 0:
				self.status["Integer"] = self.status["Integer"]*10 + int(word)
				self.status["Integer_count"] += 1
			elif word.isdigit() == True and self.status["Decimal_point_count"] > 0:
				self.status["Decimal"] = self.status["Decimal"]*10 + int(word)
				self.status["Decimal_count"] += 1
			elif word.isdigit() == False:
				self.status["letter_count"] += 1
		self.status["str_len"] = len(self._str_list)
	
	def method_run(self):
		'''
		不出现预料外的字符
		只有:一个或者零个正负号 以及 一个或者零个句号
		正号或者负号只能在第一个字符
		当正负号不存在时，句号的位置不能出现在坐标0,或者最后一个
		当正负号存在时，句号的位置不能出现在坐标1,或者最后一个
		'''
		
		if self.status["str_len"] == 0:
			self.result["Type"] = "str"
			self.result["value"] = self.str
			return self.result
		
		if not self.status["letter_count"] == 0 or \
		self.status["symbol_count"] > 1 or \
		self.status["Decimal_point_count"] > 1:
			self.result["Type"] = "str"
			self.result["value"] = self.str
			return self.result
		
		if self.status["symbol_count"] == 1 and \
		not self._str_list[0] == self.status["symbol"]:
			self.result["Type"] = "str"
			self.result["value"] = self.str
			return self.result
		
		if self.status["symbol_count"] == 0:
			if self._str_list[0] == "." or \
			self._str_list[self.status["str_len"]-1] == ".":
				self.result["Type"] = "str"
				self.result["value"] = self.str
				return self.result
		
		if self.status["symbol_count"] == 1:
			if self._str_list[1] == "." or \
			self._str_list[self.status["str_len"]-1] == ".":
				self.result["Type"] = "str"
				self.result["value"] = self.str
				return self.result

		if self.status["Decimal_point_count"] == 0:
			self.result["Type"] = "intnum"
			self.result["value"] = self.status["Integer"]
		elif self.status["Decimal_point_count"] == 1:
			self.result["Type"] = "floatnum"
			self.result["value"] = self.status["Integer"] + self.status["Decimal"]/(10 ** self.status["Decimal_count"])

		if self.status["symbol"] == "-":
			self.result["value"] = -self.result["value"]

	def method_get_int(self):
		if self.result["Type"] == "intnum" or  self.result["Type"] == "floatnum":
			return self.status["Integer"]
		else:
			return 0

	def method_get_float(self):
		if self.result["Type"] == "floatnum":
			return self.status["Decimal"]/(10 ** self.status["Decimal_count"])
		else:
			return 0

	def method_get_symbol(self):
		return self.status["symbol"]

	def method_get_number_length(self):
		return self.status["Integer_count"] + self.status["Decimal_count"]
	
	def method_printAllAttributes(self):
		print(self._str)
		print(self._str_list)
		print(self.status)
		print(self.result)

def TestPlatform():
	print("i am module strType")

def test():
	args = sys.argv
	if len(args)==1:
		print('Hello, world!')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')
if __name__=='__main__':
	test()
	startCall = input()
	CallTestPlatform = input()
	if(startCall == "call") and (CallTestPlatform == "test"):
		TestPlatform()

'''
#类的调用方式
	import package_tool.strType
	tempstrType_var = package_tool.strType.strType_class()
	tempstrType_var.str = "151515151515111111111"
	# print(tempstrType_var.method_get_symbol())
	# print(tempstrType_var.method_get_int())
	print("Integer:",tempstrType_var.status["Integer"])
	print("Decimal:",tempstrType_var.status["Decimal"])
	# print(tempstrType_var.method_get_number_length())
	tempstrType_var.method_printAllAttributes()
'''
'''
# 用命令行简单调用这个脚本的示例代码
import subprocess
r = subprocess.call(['python', 'package_tool\\strType.py', 'strType_argv'])
print('Exit code:', r)

'''

'''
# 用多命令行多输入调用这个脚本的示例代码
import subprocess
p = subprocess.Popen(['python','package_tool\strType.py','strType_argv'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'call\ntest\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''