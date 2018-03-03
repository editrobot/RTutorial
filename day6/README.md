
## 数据库工具 ##

双击运行`run.bat`

用记事本打开 **mysqlinit.sql**

看一下生成sql语句的结果

**index.py的代码**

	makedb = lib.mysql.mysql_class()
	makedb.method_add_db("newdb")
	makedb.method_use_db("newdb")

	// sampDBtable 代表数据表的名称
	// keyName 代表数据的键名,
	// min 代表这个值总共能储存的最小值
	// max 代表这个值总共能储存的最大值

	// 特殊情况: keyName = "id" 时，这时，id 就变成了表格的主键

	// "min":"65535..0", 代表最小存放65535 个字符
	// "max":"65535..0" ，代表最大存放65535 个字符

	// "min":"datetime", 存放时间格式
	// "max":"datetime" ，存放时间格式

	// "min":"0.00000000001", 最小值 0.00000000001
	// "max":"516595154151888556" ，最大值 516595154151888556

	// "min":"-999999", 最小值 -999999
	// "max":"999999" ，最大值 999999

	// 请随意修改下面的参数，并双击 运行run.bat ， 用记事本打开 mysqlinit.sql 查看结果。

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

