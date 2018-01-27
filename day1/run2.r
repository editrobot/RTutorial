data <- read.csv("input1.csv")
#打印最高薪水
print("sal <- max(data$salary)")
sal <- max(data$salary)
print(sal)
print("----------------------------")
#打印薪水等于最高薪水的员工信息
print("retval <- subset(data, salary == max(salary))")
retval <- subset(data, salary == max(salary))
print(retval)
print("----------------------------")
#打印部门等于IT的员工信息
print("retval <- subset( data, dept == 'IT')")
retval <- subset( data, dept == 'IT')
print(retval)
print("----------------------------")
#打印薪水大于600并且部门在IT的员工信息
print("info <- subset(data, salary > 600 & dept == 'IT')")
info <- subset(data, salary > 600 & dept == 'IT')
print(info)
print("----------------------------")
#打印日期大于2014-1-1号的员工信息
print("retval <- subset(data, as.Date(start_date) > as.Date('2014-01-01'))")
retval <- subset(data, as.Date(start_date) > as.Date('2014-01-01'))
print(retval)
print("----------------------------")