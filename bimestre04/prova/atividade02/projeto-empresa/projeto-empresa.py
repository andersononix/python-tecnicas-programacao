#Funções
def menuPrincipal():
    print("MENU PRINCIPAL")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Altera")
    print("4 - Imprimir")
    print("5 - Sair")

def menuLocal():
    print("Locais para viajar")
    print("1 - EUA              (R$ 5.000,00)")
    print("2 - África do Sul    (R$ 10.000,00)")
    print("3 - Japão            (R$ 15.000,00)")

def menuClasse():
    print("Nosso servisos de voos")
    print("1 - Classe econômica     (Valor da pasagem)")
    print("2 - Classe executiva     (Aumento na pasagem de 30%)")
    print("3 - Primeira classe      (Aumento na pasagem de 50%)")

'''
O usuário deverá escolher entre 3 tipos: 3 estrelas (R$ 100,00 por dia), 4 estrelas
(R$ 200,00 por dia) e 5 estrelas (R$ 300,00)
'''

def menuHospedagem():
    print("")
    print("")
    print("")
    print("")
    print("")

#Listas
cadastros = []
nomes = []
datasPastidas = []
locais = []
classes = []
hospedagens = []
qtdsDias = []
cadastros.append(nomes, datasPastidas, locais, classes, hospedagens, qtdsDias)

print("NOME DA EMPRESA")

#tela de login
resp = 1
while (resp == 1):
    usuario = str(input("\nUsúario: "))
    senha = str(input("Senha: "))
    if(usuario == "1") and (senha == "1"):
        menuPrincipal()
        nome = str(input("Nome do cliente: "))
        data = str(input("Data de partida: "))

        nomes.append(nome)
    else:
        print("\nErro login incorreto")
        print("Tente novamente")
        resp = 1


