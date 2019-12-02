class Conta(object):
    
    def __init__(self, codigo_conta, codigo_pessoa, data_cadastro, saldo):
        self.codigo_conta = codigo_conta
        self.codigo_pessoa = codigo_pessoa
        self.data_cadastro = data_cadastro
        self.saldo = saldo
    
    def saque(self, valor):
        self.saldo -= valor
        
    def deposito(self, valor):
        self.saldo += valor
        
    def transferencia(self, conta_destino, valor):
        self.saque(valor)
        conta_destino.deposito(valor)