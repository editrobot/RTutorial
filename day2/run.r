
library(rjson)

getDataPath <- function(path){
	return <- paste("data", path, sep = "/")
}

readJsonFile <- function(path){
	return <- fromJSON(file = getDataPath(path))
}

jsondata = readJsonFile("data.json")

print(jsondata)