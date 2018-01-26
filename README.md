# RTutorial
this is RTutorial

[day1 csv文件操作](day1 "/day1")

## 其他 ##

json包

    install.packages("rjson")
    library(rjson)
	json_data <- fromJSON(paste(readLines("json.txt"),collapse=""))
	print(json_data)

----------

**查询文件"input.csv"的信息**

	file.info("input.csv")

输出结果为数据框格式，可以直接导出为表格：

- **size** 表示文件大小
- **isdir** 判断是否为文件夹
- **mtime** 为修改时间
- **ctime** 为创建时间
- **atime** 为上次打开时间
- **exe** 是否为可执行程序

----------

获取脚本当前目录

    getwd()

----------

当前目录的文件列表

	dir()
	list.files()

命令行的入口参数列表

	Args <- commandArgs()

当前目录的所有文件和文件夹列表

	dir(path=getwd(),all.files=TRUE)

当前目录的树形列表

	system("tree")