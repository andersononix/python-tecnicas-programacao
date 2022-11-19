#Listas
nomes = []
datasPastidas = []
locais = []
classes = []
hospedagens = []
qtdsDias = []
valorFinal = []

# Funções
def menuPrincipal():
    print("\nMENU PRINCIPAL")
    print("[1] - Cadastrar")
    print("[2] - Excluir")
    print("[3] - Altera")
    print("[4] - Imprimir")
    print("[5] - Sair")

def menuLocal():
    print("\nLocais para viajar")
    print("[1] - EUA              (R$ 5.000,00)")
    print("[2] - África do Sul    (R$ 10.000,00)")
    print("[3] - Japão            (R$ 15.000,00)")

def menuClasse():
    print("\nNosso servisos de voos")
    print("[1] - Classe econômica     (Valor da pasagem)")
    print("[2] - Classe executiva     (Aumento na pasagem de 30%)")
    print("[3] - Primeira classe      (Aumento na pasagem de 50%)")

def menuHospedagem():
    print("\nTipos de Hospedagem")
    print("[1] - 3 estrelas   (R$ 100,00 por dia)")
    print("[2] - 4 estrelas  (R$ 200,00 por dia)")
    print("[3] - 5 estrelas  (R$ 300,00)")

def Imprimir(nomes, datasPastidas, locais, hospedagens, qtdsDias):
    for v in nomes:
        print(f"Nome do cliente: {v}")
    for v in datasPastidas:
        print(f"Data de partida: {v}")
    for v in locais:
        print(f"Local: {v}")
    for v in datasPastidas:
        print(f"Classe: {v}")
    for v in hospedagens:
        print(f"Hospedagem: {v}")
    for v in qtdsDias:
        print(f"Quantidade de dias: {v}")
        print(valor)

def nemuNomes(nomes):
    for c, v in enumerate(lista):
        print(f"Na posição: {c} tem o nomes: {v}", end=" ")

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
            nomes.append(str(input("\nNome do cliente: ")))
            datasPastidas.append(str(input("Data de partida: ")))

            # Tipos de local
            resp = 1
            while (resp == 1):
                menuLocal()
                opcao = int(input("Escolha sua opção: "))
                locais.append(opcao)
                if (opcao == 1):
                    valorLocal = 5000
                    break
                elif (opcao == 2):
                    valorLocal = 10000
                    break
                elif (opcao == 3):
                    valorLocal = 150000
                    break
                else:
                    print("\nNão tem essa opção")
                    resp = 1

            # Classes de voos
            resp = 1
            while (resp == 1):
                menuClasse()
                opcao = int(input("Escolha sua opção: "))
                classes.append(opcao)
                if(opcao == 1):
                    desconto = valorLocal
                    break
                elif(opcao == 2):
                    desconto = valorLocal + (valorLocal * 0.3)
                    break
                elif(opcao == 3):
                    desconto = valorLocal + (valorLocal * 0.5)
                    break
                else:
                    print("\nNão tem essa opção")
                    resp = 1

            # Hospedagem
            resp = 1
            while (resp == 1):
                menuHospedagem()
                opcao = int(input("Escolha sua opção: "))
                hospedagens.append(opcao)
                if(opcao == 1):
                    valorHospedagem = 100
                    break
                elif(opcao == 2):
                    valorHospedagem = 200
                    break
                elif(opcao == 3):
                    valorLocal = 300
                    break
                else:
                    print("\nNão tem essa opção")
                    resp = 1

            qtdDias = int(input("Quantidade de dias: "))
            qtdsDias.append(qtdDias)
            valor = desconto + (valorHospedagem * qtdDias)
            valorFinal.append(valor)

        #EXCLUIR USUARIO
        elif(opcao == 2):
            print()

        #ALTERAR CADASTRO DO USUARIO
        elif (opcao == 3):
            resp = 1
            while (resp == 1):
                alterar = int(input("Escolha uma opção: "))
                if(alterar == 1):
                    nomes.pop(0)
                    nome = str(input("Nome do cliente: "))
                    nomes.append(0, nome)
                    break
                elif(alterar == 2):
                    print()
                    break
                elif (alterar == 3):
                    print()
                    break
                elif (alterar == 4):
                    print()
                    break
                elif (alterar == 5):
                    print()
                    break
                elif (alterar == 6):
                    print()
                    break
                else:
                    print("Nao tem essa opção")
                    resp = 1

        #IMPRIMIR DADOS DO USUARIO
        elif (opcao == 4):
            Imprimir(nomes, datasPastidas, locais, hospedagens, qtdsDias)

        #SAIR
        else:
            print("Obigado")
            break
    else:
        print("\nErro login incorreto")
        print("Tente novamente")
        resp = 1


