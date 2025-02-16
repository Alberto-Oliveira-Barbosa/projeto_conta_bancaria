from .Transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

        
    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)