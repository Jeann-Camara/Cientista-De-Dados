class Credito(object):
    
    def __init__(self, conta, tipo, data_cadastro, montante, quantidade_prestacoes):
        self.conta = conta
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.montante = montante
        self.quantidade_prestacoes = quantidade_prestacoes
        self.taxa_juros = (0.1 if self.tipo == "F" else 0.05)
        self.majoracao_taxa_juros = (0.005 if self.tipo == "F" else 0.003)
        self.tarifa = (20 if self.tipo == "F" else 10)
        self.valor_juros_total =(self.montante * (self.taxa_juros + (self.majoracao_taxa_juros*self.quantidade_prestacoes))) + self.tarifa
        self.valor_prestacao = (self.montante + self.valor_juros_total) / self.quantidade_prestacoes
        self.lucro = (self.quantidade_prestacoes * self.valor_prestacao) - self.montante
        
    def credito_conta(self):
        self.conta.deposito(self.montante)
        
        print("Montante = ", self.montante)
        print("Quantidade de Prestações = ", self.quantidade_prestacoes)
        print("Taxa de Juros = ", self.taxa_juros)
        print("Majoração da Taxa de Juros = ", self.majoracao_taxa_juros)
        print("Tarifa = ", self.tarifa)
        print("Valor Total de Juros = ", self.valor_juros_total)
        print("Valor da Prestação = ", self.valor_prestacao)
        print("Lucro do Banco = ", self.lucro)
        
        print("\nTED Banco para Conta = ", self.montante)
        print("Novo Saldo da Conta = ", self.conta.saldo)