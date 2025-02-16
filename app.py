from src.utils.toolbox import Toolbox
from src.classes.ClientePessoaFisica import ClientePessoaFisica 
from src.classes.ContaCorrente import ContaCorrente 
from src.classes.Saque import Saque
from src.classes.Deposito import Deposito

                                                          

def criar_cliente(lista_clientes, toolbox):
    cpf = toolbox.get_cpf()
    cliente = toolbox.get_cliente(cpf, lista_clientes)

    if cliente is not None:
        print('CPF já cadastrado')
        return
    
    nome = input('Informe o nome do usuário: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: ')
    cliente = ClientePessoaFisica(nome, cpf, data_nascimento,endereco)
    lista_clientes.append(cliente)
    print(f'Usuário: {nome} criado com sucesso!')
    print("\t==============================")
    print("\t       Dados do usuário       ")
    print("\t==============================")
    print(cliente)
    print("\t==============================")



def criar_conta_corrente(lista_contas, lista_clientes, toolbox):
    cpf = toolbox.get_cpf('Informe o cpf do cliente cadastrado para gerar a conta: ')
    cliente = toolbox.get_cliente(cpf, lista_clientes)
    if cliente is None:
        print('Cliente não encontrado!\nPor favor cadastre um cliente antes de gerar uma conta para ele')
        return
    
    conta = ContaCorrente(cliente)
    lista_contas.append(conta)
    print(f'Conta gerada com sucesso!\n')
    print("\t==============================")
    print("\t        Dados da Conta        ")
    print("\t==============================")
    print(conta)
    print("\t==============================")


def executar_transacao(tipo_transacao,lista_clientes, lista_contas, toolbox):
    
    cpf = toolbox.get_cpf()
    cliente = toolbox.get_cliente(cpf, lista_clientes)
    contas_cliente = [conta for conta in lista_contas if conta.cliente.cpf == cpf]
    conta_selecionada = toolbox.get_conta(contas_cliente)

    if cliente is None:
        print('Cliente não cadastrado')
        return

    if len(contas_cliente) == 0:
        print('Sem contas cadastradas para este cliente')
        return


    match tipo_transacao.upper():
        case 'SAQUE':
            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            cliente.realizar_transacao(conta_selecionada, transacao)
        case 'DEPOSITO':
            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            cliente.realizar_transacao(conta_selecionada, transacao)
        case 'EXTRATO':
            movimentacoes = conta_selecionada.historico

            print("\n================ EXTRATO ================")
            print(conta_selecionada)
            print("==========================================")
            print("Não foram realizadas movimentações." if not movimentacoes else movimentacoes)
            print("==========================================")
        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    

    

def listar_contas(contas):
    if len(contas) == 0:
        print('Nenhuma conta cadastrada no momento')
        return

    print("\t==============================")
    print("\t        LISTAR CONTAS         ")
    print("\t==============================")
    for conta in contas:
        print(conta)
    print("\t==============================")
    

def listar_clientes(lista_clientes):
    if len(lista_clientes) == 0:
        print('Nenhum cliente cadastrado no momento')
        return

    print("\t==============================")
    print("\t        LISTAR CLIENTES       ")
    print("\t==============================")
    for cliente in lista_clientes:
        print(cliente)
    print("\t==============================")
    

def main(toolbox):
    lista_clientes = []
    lista_contas = []
    

    while True:
        
        opcao = input(toolbox.get_menu())
        
        match opcao:
            case '1':
                criar_cliente(lista_clientes, toolbox)
            case '2':
                criar_conta_corrente(lista_contas, lista_clientes, toolbox)
            case '3':
                listar_contas(lista_contas)
            case '4':
                listar_clientes(lista_clientes)
            case '5':
                executar_transacao('DEPOSITO', lista_clientes, lista_contas, toolbox)
            case '6':
                executar_transacao('SAQUE', lista_clientes, lista_contas, toolbox)
            case '7':
                executar_transacao('EXTRATO', lista_clientes, lista_contas, toolbox)
            case '8':
                break
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
        toolbox.limpar_console()


if __name__ == '__main__':
    
    main(toolbox = Toolbox())