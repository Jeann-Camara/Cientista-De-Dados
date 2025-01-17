########################################## Medidas de Posi��o Relativa ##########################################

# Definindo a pasta de trabalho
setwd("C:/Users/d001110/Desktop/R - Estat�stica - Medidas de Posi��o Relativa")
getwd()


# Carregando o dataset
carros <- read.csv("carros.csv")

# Resumo dos dados
head(carros)
str(carros)

# Medidas de Tend�ncia Central
summary(carros$ano)
summary(carros[c('preco', 'kilometragem')])


## Explorando vari�veis num�ricas
mean(carros$preco)
median(carros$preco)
quantile(carros$preco)
quantile(carros$preco, probs = c(0.01, 0.99))
quantile(carros$preco, seq(from = 0, to = 1, by = 0.20))
IQR(carros$preco) # Diferen�a entre 3� Quartil e 1� Quartil
range(carros$preco)
summary(carros$preco)
diff(range(carros$preco))
