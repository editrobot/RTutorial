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
class(jsondata)
#取出速度
teamspeed<-function(data){
    teamspd<-lapply(data,function(item){print(item$speed)})
    teamspeed<-as.numeric(teamspd)
}
#求方差和标准差
varspeed<-function(data){
    varstart=0
    for(i in 1:length(data)){
        varstart=(data[i]-mean(data))^2+varstart
	}
    varteam=varstart/length(data)
    stdteam=sqrt(varteam)
    return(list(varteam,stdteam))
}
#最终
team1speed<-teamspeed(jsondata$team1)
print(varspeed(team1speed))
team2speed<-teamspeed(jsondata$team2)
print(varspeed(team2speed))


#team1speed<-lapply(jsondata$team1,function(item){print(item$speed)})
#team2speed<-lapply(jsondata$team2,function(item){print(item$speed)})
#team1speed<-as.numeric(team1speed)
#class(team1speed)
#team2speed<-as.numeric(team2speed)
#class(team1speed)
#print(varspeed(team2speed))