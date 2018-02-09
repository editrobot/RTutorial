## 用R语言亲手实现基础公式 ##

用最低的成本，最少的输入，来推断出最丰富的信息。在真正的商业环境中，当需要越多的输入，意味着越高昂的金钱投入成本以及时间成本。

文件`data/data.json`中的数据，代表，最近有一个马拉松赛跑，有2个队伍进行比赛，team1代表队伍1，team2代表队伍2。

下面的team中，name代表参赛者的名字，age代表年龄，speed代表参赛者的赛跑平均速度，单位是：米/分钟

	{
		"team1":[
			{"name":"A","age":16,"speed":108.6},
			{"name":"B","age":33,"speed":45.24},
			{"name":"C","age":21,"speed":38.6},
			{"name":"D","age":16,"speed":208.6},
			{"name":"E","age":8,"speed":98.8},
			{"name":"F","age":18,"speed":42.4},
			{"name":"G","age":20,"speed":76.8},
			{"name":"H","age":16,"speed":125.7},
			{"name":"I","age":15,"speed":54.6},
			{"name":"J","age":27,"speed":25.6},
			{"name":"K","age":36,"speed":23}
		],
		"team2":[
			{"name":"A","age":16,"speed":58.6},
			{"name":"B","age":33,"speed":66.24},
			{"name":"C","age":21,"speed":42.6},
			{"name":"D","age":36,"speed":208.6},
			{"name":"E","age":8,"speed":68.8},
			{"name":"F","age":18,"speed":72.4},
			{"name":"G","age":20,"speed":76.4},
			{"name":"H","age":16,"speed":55.7},
			{"name":"I","age":15,"speed":154.6},
			{"name":"J","age":27,"speed":65.6},
			{"name":"K","age":36,"speed":23.47}
		],
		"error_code":0
	}


文件`run.r`中的代码

	library(rjson)
	# 加载json格式的操作包
	
	# 创建一个生成文件实际路径的函数
	getDataPath <- function(path){
		return <- paste("data", path, sep = "/")
	}
	
	# 创建一个读取文件的函数
	readJsonFile <- function(path){
		return <- fromJSON(file = getDataPath(path))
	}
	
	jsondata = readJsonFile("data.json")
	
	for ( i in jsondata$team1) {
		print(i)
	}
	
	for ( i in jsondata$team2) {
		print(i)
	}


上面的R样板代码只是简单地将json文件中的数据读取并且打印出来。

假设你是某体育电视台的数据分析员，今天刚好有一场小型的马拉松小队预赛。
![](img/10495H528-0.png)


**问题一：**

电视台工作人员有个需求就是，修改下面的R代码，来取得两个队伍的总体方差，以及标准差。

	for ( i in jsondata$team1) {
		print(i)
	}
	
	for ( i in jsondata$team2) {
		print(i)
	}

**问题二：**

把上面的计算结果保存到data文件夹里。文件名命名为：result.json 。 格式可以随意。