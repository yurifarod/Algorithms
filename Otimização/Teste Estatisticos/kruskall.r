
#Criação dos vetores com as 20 execuções

#Colocar tudo para cinco colunas

data <- read.delim("~/dados/data-hc.txt", header=FALSE, comment.char="#")

v1 <- c(data$V1)
v2 <- c(data$V2)
v3 <- c(data$V3)
v4 <- c(data$V4)
v5 <- c(data$V5)
v6 <- c(data$V6)

# Boxplot com as métricas
boxplot(v1, v2, v3, v4, v5, v6, names=c("v1","v2","v3","v4", "v5", "v6"), ylab="Quality",col=3)

# Representação do vetor em colunas
#6 algoritmos com 10 execuções
dados<-data.frame(algs<-gl(6,10), data)

#Execução do Kruskal - Se p-value < 0.05, há diferença estatística com nível de significância de 95%. 
kruskal.test(dados)



#Agora é necessário ver a diferença pareada entre os bancos. Você deve instalar o pacote PMCMR: install.packges('PMCMR')
require('PMCMR')
posthoc.kruskal.conover.test(data, algs, "bonferroni")

# A saída será algo semelhante a isso:
# 	1       2       3       4      
# 2 0.0068  -       -       -      
# 3 0.3992  3.0e-06 -       -      
# 4 8.5e-08 0.1177  6.0e-13 -      
# 5 0.9923  0.0282  0.1812  1.0e-06





