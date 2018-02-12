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

# 网上查找下面代码 assign函数的功能
assign("a",2)
assign("b",3)
assign("c",5)
assign("d",7)
assign("e",11)
assign("f",13)
assign("g",17)
assign("h",19)
assign("i",23)
assign("j",29)
assign("k",31)
assign("l",37)

count1 = 1

for(x in jsondata$data1){
	count1 = count1*get(x)
}

count2 = 1
for(x in jsondata$data2){
	count2 = count2*get(x)
}

print(count1/count2)

# 作业：
# 上面的代码是将data1的数据与data2的数据进行比较。
# 请确认 print(count1/count2) 代表什么意思。
# 确认一下，该代码使用了多少步解决问题。
# 如果按照普通方法，需要用多少步才能解决问题。