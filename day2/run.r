library(rjson)
# 加载json格式的操作包

# 创建一个生成文件实际路径的函数
getDataPath <- function(path){
	# 研究一下 paste 这个函数。在百度上搜索这个函数的用法。然后布置作业，就是要求改动这里的代码，来读取datanext.json这个文件，
	print(paste("", path, sep = ""))
	return <- paste("", path, sep = "")
}

# 创建一个读取文件的函数
readJsonFile <- function(path){
	return <- fromJSON(file = getDataPath(path))
}

# 执行读取文件的函数，将data.json格式的文件打开，并且读取里面的股票数据，把数据赋予左边的jsondata变量
jsondata = readJsonFile("datanext.json")

# 把jsondata变量打印出来。
print(jsondata$resultcode)
#print(jsondata$resultcode)
# print(jsondata$reason)
# print(jsondata$result[[1]]$dapandata$name)



