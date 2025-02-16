from .Historico import Historico

class Conta:
    __numero = 0

    def __init__(self, cliente,agencia, saldo):
        Conta.__numero += 1
        self.__numero = Conta.__numero
        self.__cliente = cliente
        self.__agencia = agencia
        self.__saldo = saldo
        self.__historico = Historico()

    @property
    def numero(self):
        return self.__numero
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def agencia(self):
        return self.__agencia

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    
    @property
    def historico(self):
        return self.__historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @staticmethod
    def sacar(self, valor):
        pass
    
    @staticmethod
    def sacar(self, valor):
        pass

    @staticmethod
    def depositar(self, valor):
        pass