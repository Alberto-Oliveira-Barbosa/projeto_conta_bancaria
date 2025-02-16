import os

class Toolbox:

    def limpar_console(self):
        input('\nTecle <ENTER> para continuar...')
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para macOS e Linux
            os.system('clear')



    def get_menu(self):
        
        menu = """

        ===============================
         Gerenciamento de novas contas 
        ===============================
        [1] Cadastrar novo cliente
        [2] Cadastrar nova conta
        [3] Listar contas cadastradas
        [4] Listar clientes cadastrados

        ==+============================
         Operações por conta corrente    
        ===+===========================
        [5] Depositar
        [6] Sacar
        [7] Extrato
        
        
        [8] Sair

        => """

        return menu
    
    def get_cpf(self, mensagem='Informe o cpf: '):
        cpf = None

        while cpf is None:
            cpf = input(mensagem)
            cpf = cpf.replace('-', '').replace('/','').replace('.','')
            
            if (not cpf.isdigit()) | (len(cpf) == 0):
                print('Digite um cpf valido')
                cpf = None

        return cpf


    def get_cliente(self, cpf, lista_clientes):
        clientes = [cliente for cliente in lista_clientes if cliente.cpf == cpf]
        
        if len(clientes) == 0:
            cliente_selecionado = None
        else:
            cliente_selecionado = clientes[0]

        return cliente_selecionado
    
    def get_conta(self, contas_cliente):
        
        opcoes = []

        if len(contas_cliente) < 1:
            return None
        
        print('\tContas disponíves: ')                
        for conta in contas_cliente:
            print(f'\tC/C: {conta.numero}')
            opcoes.append(conta.numero)
        
        conta_selecionado = None
        
        while conta_selecionado not in opcoes:

            try:
                conta_selecionado = int(input('Selecione a conta para efetuar a transação: '))
            except ValueError:
                print("Operação inválida! Por favor, insira um número válido.")
                conta_selecionado = None
            


        conta = [c for c in contas_cliente if c.numero == conta_selecionado]
        return conta[0] if conta else None

        
