# RTutorial
this is RTutorial

[day1 csv文件操作](day1 "/day1")

## 其他 ##

json包

    install.packages("rjson")
    library(rjson)
	json_data <- fromJSON(paste(readLines("json.txt"),collapse=""))
	print(json_data)


查询文件"input.csv"的信息

	file.info("input.csv")

获取脚本当前目录

    getwd()

当前目录的文件列表

	dir()
	list.files()

命令行的入口参数列表

	Args <- commandArgs()

当前目录的所有文件和文件夹列表

	dir(path=getwd(),all.files=TRUE)

当前目录的树形列表

	system("tree")