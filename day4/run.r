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