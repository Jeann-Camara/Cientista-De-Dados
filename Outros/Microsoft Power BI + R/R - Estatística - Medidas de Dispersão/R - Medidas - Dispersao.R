########################################## Medidas de Dispers�o #################################################


# Definindo a pasta de trabalho
setwd("C:/Users/d001110/Desktop/R - Estat�stica - Medidas de Dispers�o")
getwd()

# Carregando o dataset
vendas <- read.csv("Vendas.csv", fileEncoding = "windows-1252")

# Resumo do dataset
View(vendas)
str(vendas)
summary(vendas$Valor)

# Vari�ncia
var(vendas$Valor)

# Desvio Padr�o
sd(vendas$Valor)

# Coeficiente de Varia��o
sd(vendas$Valor) / mean(vendas$Valor) * 100

