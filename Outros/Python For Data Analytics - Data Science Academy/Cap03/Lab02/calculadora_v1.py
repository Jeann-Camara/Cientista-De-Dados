print("\n*********************************** Calculadora Python ***********************************")
print("\nDigite a operação desejada, exemplo: '1+2+3', ou 'exit' para sair. \n\n-->")

from functools import reduce

def Operacao_Aritmetica(operador, operandos):

    return reduce(lambda x,y:
                         x+y if operador == "+"
                    else x-y if operador == "-"
                    else x*y if operador == "*"
                    else x/y if operador == "/"
                    else 0, operandos
                 )

resultado_operacao = 0
operacao = input()

while not operacao.__contains__("exit"):

    operador = next(filter(lambda termo: not termo.isnumeric(), operacao))

    operandos = operacao.split(operador)

    resultado_operacao = Operacao_Aritmetica(operador, map(int, operandos))

    print(resultado_operacao)

    operacao = str(resultado_operacao) + input()