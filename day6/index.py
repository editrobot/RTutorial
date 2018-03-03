#! python3
#encoding: utf-8
# -*- coding: utf-8 -*-


from lib import file
import lib.mysql

if __name__=='__main__':
	makedb = lib.mysql.mysql_class()
	makedb.method_add_db("newdb")
	makedb.method_use_db("newdb")
	makedb.method_add_db_table("sampDBtable",[
		{"keyName":"id","min":"0","max":"18446744073709551615",},
		{"keyName":"Standardmodels","min":"65535..0","max":"65535..0",},
		{"keyName":"accountid","min":"-500.53","max":"999999",},
		{"keyName":"title","min":"255..0","max":"255..0",},
		{"keyName":"titleimg","min":"255..0","max":"9999..0",},
		{"keyName":"srclink","min":"65535..0","max":"65535..0",},
		{"keyName":"creattime","min":"datetime","max":"datetime",},
		{"keyName":"endtime","min":"datetime","max":"datetime",},
		{"keyName":"tag","min":"1..0","max":"1000..0",},
		{"keyName":"integral","min":"-999999","max":"999999",},
		{"keyName":"Latitude","min":"0.00000000001","max":"516595154151888556",},
		{"keyName":"Longitude","min":"0.00000000001","max":"516595154151888556",},
		{"keyName":"logintime","min":"datetime","max":"datetime",},
	])
	makedb.method_add_db_table("wechatappuser",[
		{"keyName":"id","min":"65535..0","max":"65535..0",},
		{"keyName":"session_key","min":"0..0","max":"512..0",},
		{"keyName":"expires_in","min":"0","max":"99999",},
		{"keyName":"openid","min":"0..0","max":"512..0",},
		{"keyName":"serSession","min":"255..0","max":"512..0",},
		{"keyName":"thename","min":"255..0","max":"512..0",},
		{"keyName":"cellphone","min":"255..0","max":"512..0",},
		{"keyName":"telephone","min":"255..0","max":"512..0",},
		{"keyName":"wechat","min":"255..0","max":"512..0",},
		{"keyName":"qq","min":"255..0","max":"512..0",},
		{"keyName":"birthday","min":"datetime","max":"datetime",},
		{"keyName":"idcard","min":"255..0","max":"512..0",},
		{"keyName":"address","min":"255..0","max":"512..0",},
		{"keyName":"sell","min":"8000..0","max":"8000..0",},
		{"keyName":"buy","min":"8000..0","max":"8000..0",},
		{"keyName":"email","min":"1..0","max":"512..0",},
		{"keyName":"url","min":"65535..0","max":"65535..0",},
		{"keyName":"onlinestatus","min":"255..0","max":"512..0",},
	])
	makedb.method_add_db_table("integralhistory",[
		{"keyName":"category","min":"999999..0","max":"999999..0",},
		{"keyName":"FromAccountid","min":"65535..0","max":"65535..0",},
		{"keyName":"Fromintegral","min":"-999999","max":"999999",},
		{"keyName":"ToAccountid","min":"65535..0","max":"65535..0",},
		{"keyName":"Tointegral","min":"-999999","max":"999999",},
		{"keyName":"settlementstate","min":"255..0","max":"255..0",},
		{"keyName":"time","min":"datetime","max":"datetime",},
	])
	file.write_str_file("mysqlinit.sql",makedb.method_run())
