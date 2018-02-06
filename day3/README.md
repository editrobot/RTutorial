**R语言生成 Json 格式的文件**

**本章节目标**：将R语言创建的数据，以文件的形式保存下来。直接鼠标双击 `run.bat` ，运行里面的代码。

**代码：**


    library(rjson)
    # 加载json格式的操作包
    
    getDataPath <- function(path){
    	return <- paste("data", path, sep = "/")
    }
    
    writeJsonFile <- function(path,data){
    	cat(toJSON(data), file = getDataPath(path))
    }
    
	# 创建一个队列数据
    doc = c(0,1,2,3)

	# 创建一个数据框
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