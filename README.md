## Conta corrente

### Descrição

Simulação de uma conta bancária para a prática de conceitos de programação.

### Tecnologias usadas
- Python

### Status

![em progresso](https://img.shields.io/badge/work_in-progress-blue)


### Definições das Branchs do projeto
Para facilitar o entendimento da evolução dos exercícios, o projeto foi dividido em branchs com a evolução de cada passo:
- **Main** --> Estado atual da aplicação, com o merge das branchs das versões anteriores.
- **v1** --> Implementação básica da conta, sem orientação a objetos, ou funções específicas. Implementados os esqueletos de *depositar*, *sacar* e *exibir extrato*   
- **v2** --> Nesta versão é iniciado o processo de modularização do código, separando ele em funções e criando novas funcionalidades:
    - Dividir o código em funções para *sacar*, *depositar* e *exibir extrato*.
    - A função de *saque* deve receber os argumentos **apenas por nome**.
    - A função *depositar* deve receber os argumentos **apenas por posição**.
    - A função exibir extrato deve receber *saldo* **apenas por posição** e extrato **apenas nomeado**
    - Criar funções: 
        - **criar usuário**--> Armazenar em uma lista, ele deve possuir os atributos: *nome*, *data de nascimento*, *cpf* e *endereço*. Não pode ser cadastrado dois usuários para o mesmo cpf.
        - **criar conta**--> Armazenar a conta em uma lista, ela deve possuir *agência*, *número da conta* e *usuário*.O número da conta deve ser sequencial, iniciando em 1, a agência deve ser fixa com o valor "0001" e um usuário pode ter mais de uma conta, mas uma conta só pode pertencer a um usuário.
        - **listar contas**--> Implementar uma listagem das contas criadas.
- **v3** --> Aplicação de orientação a objetos para o projeto.

### Organização da estrutura do projeto:
- **app.py** --> Arquivo principal que inicializa a execução do projeto.
- **src/classes** --> Diretório com as classes do projeto.
- **src/utils** --> Diretório com ferramentas usadas pelas classes.

### Modo de usar:
Clonar o projeto com o comando:
```shell
git@github.com:Alberto-Oliveira-Barbosa/projeto_conta_bancaria.git
```
Mudar para a pasta *projeto_conta_bancaria* com o comando:
```shell
cd projeto_conta_bancaria
```
Ativar o projeto com o comando:
```shell
python app.py
```
