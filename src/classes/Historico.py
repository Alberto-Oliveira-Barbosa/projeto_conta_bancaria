from datetime import datetime

class Historico:
    def __init__(self):
        self.__transacoes = []

    def adicionar_transacao(self, transacao):
        self.__transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor':transacao.valor,
            'data_operacao': datetime.now()
        })

    @property
    def transacoes(self):
        return self.__transacoes
    
    def __str__(self):
        return '\n'.join([
            f'{transacao["data_operacao"].strftime("%d/%m/%Y %H:%M:%S")} - {transacao["tipo"]}: {transacao["valor"]}' 
            for transacao in self.__transacoes
        ])