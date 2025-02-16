from .Conta import Conta
from .Saque import Saque

class ContaCorrente(Conta):
    def __init__(self, cliente, agencia='0001', saldo=0, limite=500, quantidade_saques=3):
        super().__init__(cliente, agencia, saldo)
        self.__limite = limite
        self.__quantidade_saques = quantidade_saques

    @property
    def quantidade_saques(self):
        return self.__quantidade_saques
    
    @quantidade_saques.setter
    def quantidade_saques(self, valor):
        self.__quantidade_saques += valor

    @property
    def limite_atual(self):
        return self.__limite + self.saldo


    def sacar(self, valor):
        excedeu_limite = valor > self.limite_atual
        excedeu_quantidade_saques = self.quantidade_saques < 1

        if excedeu_limite:
            print('Operação falhou! Limite excedido')
        elif excedeu_quantidade_saques:
            print('Operação falhou! Limite de saques excedido')
        else:
            self.saldo -= valor
            self.quantidade_saques = -1
            print(f'Saque de {valor} realizado com sucesso!')
            return True
            
        return False
    
    def depositar(self, valor):
        if valor > 0 :
            self.saldo += valor
            print(f'Depósito de {valor} realizado com sucesso!')
            return True
        else:
            print('Operação falhou!')
            return False

    def __str__(self):
        return f"""\
            Agência: {self.agencia}
            C/C: {self.numero}
            Titular: {self.cliente.nome}
            Saldo Atual: R$ {self.saldo:.2f}
            Limite Restante: {self.limite_atual}
            Total de saques restantes: {self.quantidade_saques}
        """
    