import datetime
from banco import *

        
if __name__ == "__main__":
    
    pessoa1 = Pessoa(1,"Jeann Câmara","022.422.833-16", "")
    pessoa2 = Pessoa(2,"Leandro Crispim","000.000.000-00", "")
    conta1 = Conta(1, 1, datetime.datetime.now(), 100)
    conta2 = Conta(2, 2, datetime.datetime.now(), 100000)
    
    print("\nSaldo Conta1 = ", conta1.saldo)
    print("Saldo Conta2 = ", conta2.saldo)
    
    conta1.saque(50)
    print("Saldo Conta1 (saque 50) = ", conta1.saldo)
    
    conta1.deposito(50)
    print("Saldo Conta1 (deposito 50) = ", conta1.saldo)
    
    conta1.transferencia(conta2,50)
    print("\nTranferencia de 50 de Conta1 para Conta2")
    
    print("Saldo Conta1 = ", conta1.saldo)
    print("Saldo Conta2 = ", conta2.saldo)
    
    print("\nConta1 pede crédito de 2000")
    
    credito1 = Credito(conta1,"F", datetime.datetime.now(), 2000, 10)
    
    credito1.credito_conta()