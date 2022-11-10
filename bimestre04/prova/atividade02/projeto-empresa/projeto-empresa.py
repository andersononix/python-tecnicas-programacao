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

def menuHospedagem():
    print("Tipos de Hospedagem")
    print("1 - 3 estrelas   (R$ 100,00 por dia)")
    print("2 -  4 estrelas  (R$ 200,00 por dia)")
    print("3 -  5 estrelas  (R$ 300,00)")

def escolhaLocal(opcao):
    if(opcao == 1):
        print()


#Listas
nomes = []
datasPastidas = []
locais = []
classes = []
hospedagens = []
qtdsDias = []

print("NOME DA EMPRESA")

#tela de login
resp = 1
while (resp == 1):
    usuario = str(input("\nUsúario: "))
    senha = str(input("Senha: "))
    if(usuario == "1") and (senha == "1"):
        #INICIO
        menuPrincipal()
        opcao = int(input("Digiti sua opção: "))

        #CASDASTRAR USUARIO
        if  (opcao == 1):
            nomes.append(str(input("Nome do cliente: ")))
            datasPastidas.append(str(input("Data de partida: ")))
            # Tipos de local
            menuLocal()
            opcao = int(input("Escolha sua opção: "))
            escolhaLocal(opcao)
            # Classes de voos
            menuClasse()
            classes.append(int(input("Escolha sua opção: ")))
            # Hospedagem
            menuHospedagem()
            hospedagens.append(int(input("escolha sua opção: ")))
            qtdsDias.append(str(input("Quantidade de dias: ")))

        #EXCLUIR USUARIO
        elif(opcao == 2):
            print()

        #ALTERAR CADASTRO DO USUARIO
        elif (opcao == 3):
            print()

        #IMPRIMIR DADOS DO USUARIO
        elif (opcao == 4):
            print()

        #SAIR
        else:
            print()
    else:
        print("\nErro login incorreto")
        print("Tente novamente")
        resp = 1
print(nomes)
print(datasPastidas)
print(locais)
print(classes)
print(hospedagens)
print(qtdsDias)

