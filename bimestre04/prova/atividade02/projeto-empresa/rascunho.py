'''
lista = []
lista1 = []
dados = []

resp = 1

while (resp == 1):
    op = int(input("op: "))
    if(op == 1):
        lista.append(str(input("Qual o seu nome: ")))
        dados.append(lista)
        dados.append(lista1)
    else:
        print("Obrigado")
        break
    resp = 1
for c, v in enumerate(lista):
    print(f"Naposiçao {c} tem o nomes: {v}")
'''
nomes = []
resp = 1
while (resp == 1):
    nomes.append(str(input("Nome do cliente: ")))
    nomes.append(str(input("Nome do cliente: ")))
    alterar = int(input("Qual aopção: "))
    if(alterar == 1):
        nome1 = str(input("Nome do cliente: "))
        nomes.pop(0)
        nomes.insert(0, nome1)
        print(nomes)
        break
    else:
        print("Nãõ tem na lista")
        resp = 1
