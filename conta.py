def get_menu():

    menu = """

    Gerenciamento da conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    
    ===============================

    Manutenção de contas
    [u] Cadastrar novo usuário
    [c] Cadastrar nova conta
    [l] Listar contas cadastradas
    
    [q] Sair

    => """

    return menu

def depositar(valor, saldo, extrato, / ):
    # o exercício pede que todos os argumentos 
    # passados para a função depositar sejam posicionais 
    if valor > 0:
        saldo += valor
        extrato += f"(+) Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    # o exercício pede que todos os argumentos passados
    # sejam passados nomeados
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"(-) Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def get_extrato(saldo, /, *, extrato ):
    # o exercício pede que os o seguinte para a função extrato:
    # - saldo como argumento posicional
    # - extrato como argumento nomeado
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def __get_cpf():
    cpf = None

    while cpf is None:
        cpf = input('Informe o cpf: ')
        cpf = cpf.replace('-', '').replace('/','').replace('.','')
        
        if (not cpf.isdigit()) | (len(cpf) == 0):
            print('Digite um cpf valido')
            cpf = None

    return cpf


def __get_usuario(cpf, usuarios):
    usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    if len(usuario) == 0:
        usuario = None
    else:
        usuario = usuario[0]

    return usuario


def criar_usuario(usuarios):
    cpf = __get_cpf()
    usuario = __get_usuario(cpf, usuarios)

    if usuario is not None:
        print('CPF já cadastrado')
        return
    
    nome = input('Informe o nome do usuário da conta: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: ')

    usuarios.append({'usuario': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print(f'Usuário: {nome} criado com sucesso!')


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = '0001'
    total_contas = 1

    while True:
        opcao = input(get_menu())
        
        match opcao.lower():
            case 'd':
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(valor, saldo, extrato)
            case 's':
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
            case 'e':
                get_extrato(saldo, extrato=extrato)
            case 'u':
                criar_usuario(usuarios)
            case 'q':
                break
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    main()