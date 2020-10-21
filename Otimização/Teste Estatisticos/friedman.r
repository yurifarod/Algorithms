data <- read.delim("~/dados/data-hc.txt", header=FALSE, comment.char="#")

v1 <- c(data$V1)
v2 <- c(data$V2)
v3 <- c(data$V3)
v4 <- c(data$V4)
v5 <- c(data$V5)
v6 <- c(data$V5)

AR1 <-cbind(v1,v2,v3,v4,v5,v6)
friedman.test(AR1)
require('pgirmess')
friedmanmc(AR1)
