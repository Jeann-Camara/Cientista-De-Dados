########################################## Medidas de Posição Relativa ##########################################

# Definindo a pasta de trabalho
setwd("C:/Users/d001110/Desktop/R - Estatística - Medidas de Posição Relativa")
getwd()


# Carregando o dataset
carros <- read.csv("carros.csv")

# Resumo dos dados
head(carros)
str(carros)

# Medidas de Tendência Central
summary(carros$ano)
summary(carros[c('preco', 'kilometragem')])


## Explorando variáveis numéricas
mean(carros$preco)
median(carros$preco)
quantile(carros$preco)
quantile(carros$preco, probs = c(0.01, 0.99))
quantile(carros$preco, seq(from = 0, to = 1, by = 0.20))
IQR(carros$preco) # Diferença entre 3º Quartil e 1º Quartil
range(carros$preco)
summary(carros$preco)
diff(range(carros$preco))
