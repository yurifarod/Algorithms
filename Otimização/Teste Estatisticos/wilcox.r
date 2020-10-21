data <- read.delim("~/dados/data-hc-2.txt", header=FALSE, comment.char="#")

v1 <- c(data$V1)
v2 <- c(data$V2)

boxplot(v1,v2)
wilcox.test(v1,v2)

