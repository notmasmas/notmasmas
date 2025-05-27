class Cliente():
    def __init__(self, raca: str, peso: float, idade: int, nome: str, dono: str, valor_banho: float = 25):
        self.raca = raca
        self.peso = peso
        self.idade = idade
        self.nome = nome
        self.dono = dono
        self.valor_banho = valor_banho
        
    def retornar_mensalidade(self, dias: int):
        mensalidade = self.valor_banho * dias
        return mensalidade
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Raca: {self.raca}, Dono: {self.dono}'

class ClienteVIP(Cliente):
    def __init__(self, raca: str, peso: float, idade: int, nome: int, dono: str, restricao_alimentar: bool):
        super().__init__(raca, peso, idade, nome, dono)
        self.restricao_alimentar  = restricao_alimentar
        
    def verificar_restricao(self):
        if self.restricao_alimentar:
            print('Possui restrições!')
        else:
            print('Não possui restrições!')
            
    def retornar_mensalidade(self, dias: int):
        return super().retornar_mensalidade(dias) * 0.8
    
cadastro_clientes = []

def cadastrar_clientes():
    raca = input('Raça: ')
    peso = float(input('Peso: '))
    idade = int(input('Idade: '))
    nome = input('Nome: ')
    dono = input('Dono: ')

    VIP = input('Cliente VIP? (Y/N): ')

    if VIP == 'Y':
        possui_restricao = input('Possui restrição alimentar? (Y/N) ')
        if possui_restricao == 'Y':
            restricao_alimentar = True
        else:
            restricao_alimentar = False
        novo_cliente = ClienteVIP(raca, peso, idade, nome, dono, restricao_alimentar)
    else:
        novo_cliente = Cliente(raca, peso, idade, nome, dono )

    cadastro_clientes.append(novo_cliente)

def imprimir_informacoes():
    nome = input('Nome: ')

    for cliente in cadastro_clientes:
        if cliente.nome == nome:
            print(cliente)
        else:
            print('Cadastro não encontrado')

def verificar_mensalidade():
    nome = input('Nome: ')
    dias = int(input('Quantos banhos por mês? '))
    for cliente in cadastro_clientes:
        if cliente.nome == nome:
            print(cliente.retornar_mensalidade(dias))


comando = int(input('1 (CADASTRAR) / 2 (PESQUISAR) / 3 (VERIFICAR MENSALIDADE) / 4 (SAIR) '))

while comando != 4:
    if comando == 1:
        cadastrar_clientes()
    elif comando == 2:
        imprimir_informacoes()
    elif comando == 3:
        verificar_mensalidade()
    elif comando != 4:
        print('Comando inválido')
    
    comando = int(input('1 (CADASTRAR) / 2 (PESQUISAR) / 3 (VERIFICAR MENSALIDADE) / 4 (SAIR) '))

