#Atividade 2
nome_cliente=input("Nome do cliente:")
nome_cidade = str(input("Qual a cidade que vai:"))
opcao=int(input("Digite seu Passeio:"))
qtd_pessoas = int(input("Quantidade de pessoas:"))
if (opcao == 1)and(nome_cidade == "Rio de Janeiro"):
    Passeio = 1
    calculo = 200 * qtd_pessoas  
elif (opcao == 2)and(nome_cidade == "Rio de Janeiro"):
    Passeio = 2
    calculo = 100 * qtd_pessoas   
elif (opcao == 1)and(nome_cidade == "Alagoas"):
    Passeio = 1
    calculo = 250 * qtd_pessoas  
elif (opcao == 2)and(nome_cidade == "Alagoas"):
    Passeio = 2
    calculo = 125 * qtd_pessoas   
elif (opcao == 1)and(nome_cidade == "Serra Gaucha"):
    Passeio = 1
    calculo = 300 * qtd_pessoas  
elif (opcao == 2)and(nome_cidade == "Serra Gaucha"):
    Passeio = 2
    calculo = 150 * qtd_pessoas
else:
    print("Não tem Viagens para essa cidade")

print("$$ Agência de Viagens Vamos Ali $$")
print("$$ Pacotes de passeios $$")
print("Cliente: {}".format(nome_cliente))
print("Cidade: {}".format(nome_cidade))
print("Passeio: {}".format(Passeio))
print("Quantidade pessoas: {}".format(qtd_pessoas))
print("Valor total: {}".format(calculo))
