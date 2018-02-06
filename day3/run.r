library(rjson)
# 加载json格式的操作包

getDataPath <- function(path){
	return <- paste("data", path, sep = "/")
}

writeJsonFile <- function(path,data){
	cat(toJSON(data), file = getDataPath(path))
}

doc = c(0,1,2,3)
emp.data <- data.frame(
	emp_id = c (1:5), 
	emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
	salary = c(623.3,515.2,611.0,729.0,843.25), 
	start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11",
	"2015-03-27")),
	stringsAsFactors = FALSE
)

writeJsonFile("cache1.txt",doc)
writeJsonFile("cache2.txt",emp.data)