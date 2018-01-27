data <- read.csv("input1.csv")

print("sal <- max(data$salary):")
sal <- max(data$salary)
print(sal)
print("----------------------------")

print("retval <- subset(data, salary == max(salary))")
retval <- subset(data, salary == max(salary))
print(retval)
print("----------------------------")

print("retval <- subset( data, dept == 'IT')")
retval <- subset( data, dept == 'IT')
print(retval)
print("----------------------------")

print("info <- subset(data, salary > 600 & dept == 'IT')")
info <- subset(data, salary > 600 & dept == 'IT')
print(info)
print("----------------------------")

print("retval <- subset(data, as.Date(start_date) > as.Date('2014-01-01'))")
retval <- subset(data, as.Date(start_date) > as.Date('2014-01-01'))
print(retval)
print("----------------------------")