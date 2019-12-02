########################################## Medidas de Dispersão #################################################


# Definindo a pasta de trabalho
setwd("C:/Users/d001110/Desktop/R - Estatística - Medidas de Dispersão")
getwd()

# Carregando o dataset
vendas <- read.csv("Vendas.csv", fileEncoding = "windows-1252")

# Resumo do dataset
View(vendas)
str(vendas)
summary(vendas$Valor)

# Variância
var(vendas$Valor)

# Desvio Padrão
sd(vendas$Valor)

# Coeficiente de Variação
sd(vendas$Valor) / mean(vendas$Valor) * 100

