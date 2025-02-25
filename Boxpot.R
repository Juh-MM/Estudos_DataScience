#dados
dados <- rnorm(15, mean = 50, sd = 10)
print(dados)
#estatistica
print(summary(dados))
#boxplot
boxplot(dados, main = "Boxplot dos Dados", col = "lightblue")
