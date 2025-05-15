cadastros = {}
numCadastros = 0

def cadastrarUsuario(id_usuario) -> dict:
    usuario = {}
    infosTrabalho = {}

    usuario['nome'] = input('Nome: ')
    dataNascimento = input('Data de nascimento (DD/MM/YYYY): ')
    anoNascimento = int(dataNascimento[6::])
    usuario['idade'] = 2025 - anoNascimento
    usuario['carteiraTrabalho'] = int(input('Número da Carteira de Trabalho: '))

    if usuario['carteiraTrabalho'] != 0:
        infosTrabalho['anoContratacao'] = int(input('Ano de contratação (YYYY): '))
        infosTrabalho['salario'] = float(input('Salário: '))
        infosTrabalho['idadeAposentadoria'] = infosTrabalho['anoContratacao'] - anoNascimento + 35
        usuario['infosTrabalho'] = infosTrabalho

    cadastros[id_usuario] = usuario

def imprimirUsuario() -> None:
    nomeUsuario = input('Nome do usuário: ')

    for usuario in cadastros:
        if nomeUsuario in cadastros[usuario].values():
            print(cadastros[usuario].items())

def imprimirCadastros() -> None:
    print(cadastros)

dictMenu = {1: cadastrarUsuario, 2: imprimirUsuario, 3: imprimirCadastros}

print('O que deseja fazer?')
menu = int(input('1: Cadastrar usuário\n2: Imprimir dados de um usuário\n3: Imprimir todos os dados\n4: Encerrar programa\n'))

while menu != 4:

    if menu in dictMenu.keys() and menu != 1:
        dictMenu.get(menu)()
    elif menu == 1: 
        dictMenu.get(menu)(numCadastros)
        numCadastros += 1
    elif menu != 4:
        print('Valor desconhecido.')

    print('O que deseja fazer?')
    menu = int(input('1: Cadastrar usuário\n2: Imprimir dados de um usuário\n3: Imprimir todos os dados\n4: Encerrar programa\n'))
    
