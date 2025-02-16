from .Cliente import Cliente

class ClientePessoaFisica(Cliente):
    
    def __init__(self, nome, cpf, data_nascimento,endereco):
        super().__init__(nome, endereco)
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @property
    def cpf(self):
        return self.__cpf
    
    def __str__(self):
        return f"""\
            Nome: {self.nome}
            CPF: {self.cpf}
            Data Nascimento: {self.data_nascimento}
            Endereço: {self.endereco}            
        """