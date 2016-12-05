

setwd("C:\Users\jaafar\PycharmProjects\CogSLA\sample")

library(ggplot2)
library(xts)
library(reshape2)

base <-  read.csv("Data/data_demo.csv", sep=";", na.strings = "")

head(myTable)

str(myTable)

myTable$Timestamp <- as.Date(myTable[,1])

str(myTable)

ggplot(myTable,aes(x =Timestamp, y= predict))+ geom_line()

ggplot(myTable,aes(x =Timestamp, y= cpu.wait_perc))+ geom_line()


daycols = c("Timestamp", "cpu.wait_perc", "predict")
for (icol in daycols){
  print(head(base[,icol]))
  cat("\n")
}
