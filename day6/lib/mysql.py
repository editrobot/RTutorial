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
import lib.file
import lib.strType

class mysql_table_data_class(object):
	def __init__(self, name, min="", max="", null_switch = "not null"):
		self.name = name
		self.format = "str"
		self.min = {}
		self.max = {}
		self.null_switch = null_switch
		self.Analysis_min_max(min, max)

	def Analysis_min_max(self, min, max):
		self.min = lib.strType.strType_class(min)
		self.max = lib.strType.strType_class(max)
		if self.min.result["Type"] == "intnum" and \
		self.max.result["Type"] == "intnum":
			self.format = "intnum"
		elif self.min.result["Type"] == "floatnum" and \
		self.max.result["Type"] == "floatnum":
			self.format = "floatnum"
		elif self.min.result["Type"] == "intnum" and \
		self.max.result["Type"] == "floatnum":
			self.format = "floatnum"
		elif self.min.result["Type"] == "floatnum" and \
		self.max.result["Type"] == "intnum":
			self.format = "floatnum"
		elif self.min.result["Type"] == "str" and \
		self.max.result["Type"] == "str" and \
		min == "datetime" and max == "datetime":
			self.format = "datetime"
		elif self.min.result["Type"] == "str" and \
		self.max.result["Type"] == "str" and \
		min == "timestamp" and max == "timestamp":
			self.format = "timestamp"
		elif self.min.result["Type"] == "str" or \
		self.max.result["Type"] == "intnum":
			self.format = "str"
		elif self.min.result["Type"] == "str" or \
		self.max.result["Type"] == "floatnum":
			self.format = "str"
		elif self.min.result["Type"] == "intnum" or \
		self.max.result["Type"] == "str":
			self.format = "str"
		elif self.min.result["Type"] == "floatnum" or \
		self.max.result["Type"] == "str":
			self.format = "str"
	
	def output_intnumsqltablecode(self,format=None):
		if self.min.result["value"] >= -128 and \
		self.max.result["value"] <= 127:
			if format == None:
				return "%s tinyint %s" % (self.name,self.null_switch)
			else:
				return "%s tinyint" % (self.name)
			
		elif self.min.result["value"] >= 0 and \
		self.max.result["value"] <= 255:
			if format == None:
				return "%s tinyint unsigned %s" % (self.name,self.null_switch)
			else:
				return "%s tinyint" % (self.name)

		elif self.min.result["value"] >= -32768 and \
		self.max.result["value"] <= 32767:
			if format == None:
				return "%s SMALLINT %s" % (self.name,self.null_switch)
			else:
				return "%s SMALLINT" % (self.name,self.null_switch)

		elif self.min.result["value"] >= 0 and \
		self.max.result["value"] <= 65535:
			if format == None:
				return "%s SMALLINT unsigned %s" % (self.name,self.null_switch)
			else:
				return "%s SMALLINT" % (self.name)

		elif self.min.result["value"] >= -8388608 and \
		self.max.result["value"] <= 8388607:
			if format == None:
				return "%s MEDIUMINT %s" % (self.name,self.null_switch)
			else:
				return "%s MEDIUMINT" % (self.name)

		elif self.min.result["value"] >= 0 and \
		self.max.result["value"] <= 16777215:
			if format == None:
				return "%s MEDIUMINT unsigned %s" % (self.name,self.null_switch)
			else:
				return "%s MEDIUMINT" % (self.name)

		elif self.min.result["value"] >= -2147483648 and \
		self.max.result["value"] <= 2147483647:
			if format == None:
				return "%s INT %s" % (self.name,self.null_switch)
			else:
				return "%s INT" % (self.name)

		elif self.min.result["value"] >= 0 and \
		self.max.result["value"] <= 4294967295:
			if format == None:
				return "%s INT unsigned %s" % (self.name,self.null_switch)
			else:
				return "%s INT" % (self.name)

		elif self.min.result["value"] >= -9223372036854775808 and \
		self.max.result["value"] <= 9223372036854775807:
			if format == None:
				return "%s BIGINT %s" % (self.name,self.null_switch)
			else:
				return "%s BIGINT" % (self.name)

		elif self.min.result["value"] >= 0 and \
		self.max.result["value"] <= 18446744073709551615:
			if format == None:
				return "%s BIGINT unsigned %s" % (self.name,self.null_switch)
			else:
				return "%s BIGINT" % (self.name)
		else:
			if format == None:
				return "%s BIGINT unsigned %s" % (self.name,self.null_switch)
			else:
				return "%s BIGINT" % (self.name)

	def output_floatnumsqltablecode(self,format=None):
		# 符号
		symbol = "+"
		# 总长度
		length = 0
		# 小数点长度
		Decimal_length = 0
		
		if self.min.method_get_symbol() == "-" or self.max.method_get_symbol() == "-":
			symbol = "-"
		
		if self.min.method_get_number_length() > self.max.method_get_number_length():
			length = self.min.method_get_number_length()
		elif self.min.method_get_number_length() < self.max.method_get_number_length():
			length = self.max.method_get_number_length()
		else:
			length = self.max.method_get_number_length()

		if self.min.status["Decimal_count"] > self.max.status["Decimal_count"]:
			Decimal_length = self.min.status["Decimal_count"]
		elif self.min.status["Decimal_count"] < self.max.status["Decimal_count"]:
			Decimal_length = self.max.status["Decimal_count"]
		else:
			Decimal_length = self.max.status["Decimal_count"]
		
		if symbol == "-" and length <= 65 and Decimal_length <= 65:
			if format == None:
				return "%s decimal(%s,%s) %s" % (self.name,length,Decimal_length,self.null_switch)
			else:
				return "%s decimal(%s,%s)" % (self.name,length,Decimal_length)
		elif symbol == "+" and length <= 65 and Decimal_length <= 65:
			if format == None:
				return "%s decimal(%s,%s) unsigned %s" % (self.name,length,Decimal_length,self.null_switch)
			else:
				return "%s decimal(%s,%s)" % (self.name,length,Decimal_length)
		else:
			if format == None:
				return "%s decimal unsigned %s" % (self.name,self.null_switch)
			else:
				return "%s decimal unsigned" % (self.name)

	def output_datetimesqltablecode(self,format=None):
		if format == None:
			return "%s datetime NOT NULL" % (self.name)
		else:
			return "%s datetime" % (self.name)

	def output_timestampsqltablecode(self,format=None):
		if format == None:
			return "%s timestamp NOT NULL" % (self.name)
		else:
			return "%s timestamp" % (self.name)

	def output_textsqltablecode(self,format=None):
		if self.min.status["Integer"] <= 255 and self.max.status["Integer"] <= 255:
			if format == None:
				return "%s CHAR NULL DEFAULT \"-\"" % (self.name)
			else:
				return "%s CHAR" % (self.name)
		elif self.min.status["Integer"] <= 255 and self.max.status["Integer"] <= 65535:
			if format == None:
				return "%s VARCHAR(255) NULL DEFAULT \"-\"" % (self.name)
			else:
				return "%s VARCHAR(255)" % (self.name)
		elif self.min.status["Integer"] <= 65535 and self.max.status["Integer"] <= 65535:
			if format == None:
				return "%s TEXT NOT NULL" % (self.name)
			else:
				return "%s TEXT" % (self.name)
		elif self.min.status["Integer"] <= 16777215 or self.max.status["Integer"] <= 16777215:
			if format == None:
				return "%s MEDIUMTEXT NOT NULL" % (self.name)
			else:
				return "%s MEDIUMTEXT" % (self.name)
		elif self.min.status["Integer"] <= 4294967295 or self.max.status["Integer"] <= 4294967295:
			if format == None:
				return "%s LONGTEXT NOT NULL" % (self.name)
			else:
				return "%s LONGTEXT" % (self.name)
		else:
			if format == None:
				return "%s LONGTEXT NOT NULL" % (self.name)
			else:
				return "%s LONGTEXT" % (self.name)
	
	def run(self,format=None):
		if self.name == "id":
			if format == None:
				return "id INT UNSIGNED NOT NULL auto_increment PRIMARY KEY"
			else:
				return "id INT UNSIGNED"
		elif self.format == "intnum":
			return self.output_intnumsqltablecode(format)
		elif self.format == "floatnum":
			return self.output_floatnumsqltablecode(format)
		elif self.format == "datetime":
			return self.output_datetimesqltablecode(format)
		elif self.format == "timestamp":
			return self.output_timestampsqltablecode(format)
		else:
			return self.output_textsqltablecode(format)

class mysql_table_format_class(object):
	def __init__(self, Name, Rows_Name_list=[]):
		self.Name = Name
		self.Rows_Name_list = Rows_Name_list
		self.code_list = []

	def creattable(self):
		count = 0
		self.code_list.append("")
		self.code_list.append("DROP TABLE IF EXISTS `%s`;" % (self.Name))
		self.code_list.append("create table %s" % (self.Name))
		self.code_list.append("(")
		for Rows_Name in self.Rows_Name_list:
			if not count == len(self.Rows_Name_list)-1:
				self.code_list.append("	%s," % Rows_Name.run())
			else:
				self.code_list.append("	%s" % Rows_Name.run())
			count += 1
		self.code_list.append(") ENGINE=InnoDB CHARACTER SET = utf8;")
	
	def PROCEDUREcount(self):
		self.code_list.append("")
		self.code_list.append("DROP PROCEDURE IF EXISTS `%scount`;" % (self.Name))
		self.code_list.append("delimiter //")
		self.code_list.append("CREATE PROCEDURE %scount (OUT countresult INT)" % (self.Name))
		self.code_list.append("BEGIN")
		self.code_list.append("SELECT COUNT(*) INTO countresult FROM %s;" % (self.Name))
		self.code_list.append("END //")
		self.code_list.append("delimiter ;")

	def run(self):
		self.creattable()
		self.PROCEDUREcount()
		return "\n".join(self.code_list)

class mysql_class(object):
	def __init__(self):
		self._port = ""
		self.mysql_code_list = []

	@property
	def port(self):
		return self._port
	@port.setter
	def port(self,value):
		self._port = value

	def method_add_db(self,db_name):
		self.mysql_code_list.append("")
		self.mysql_code_list.append("CREATE DATABASE")
		self.mysql_code_list.append("IF NOT EXISTS `%s` CHARACTER" % (db_name))
		self.mysql_code_list.append("SET utf8;")

	def method_use_db(self,db_name):
		self.mysql_code_list.append("")
		self.mysql_code_list.append("USE `%s`;" % (db_name))

	def method_add_db_table(self,table_name,Rows_Name_list=None):
		format_Rows_Name_list = []
		for index in Rows_Name_list:
			format_Rows_Name_list.append(
				lib.mysql.mysql_table_data_class(
				index["keyName"],
				index["min"],
				index["max"])
				)
		self.mysql_code_list.append("")
		tempmysql_var = lib.mysql.mysql_table_format_class(
			table_name,
			format_Rows_Name_list)
		self.mysql_code_list.append(tempmysql_var.run())

	def method_table_convert_utf8(self, table_name):
		self.mysql_code_list.append("")
		self.mysql_code_list.append("alter table %s convert to character set utf8;" % (table_name))

	def method_init(self):
		self.mysql_code_list = []
		
	def method_run(self):
		return "\n".join(self.mysql_code_list)

def TestPlatform():
	print("i am module mysql")

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
	import lib.mysql
	tempmysql_var = lib.mysql.mysql_class()
	tempmysql_var.port = ""
	tempmysql_var.method_add_db()
	tempmysql_var.method_add_db_table()
	tempmysql_var.method_run()
'''
'''
# 用命令行简单调用这个脚本的示例代码
import subprocess
r = subprocess.call(['python', 'lib\\mysql.py', 'mysql_argv'])
print('Exit code:', r)

'''

'''
# 用多命令行多输入调用这个脚本的示例代码
import subprocess
p = subprocess.Popen(['python','lib\mysql.py','mysql_argv'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'call\ntest\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''