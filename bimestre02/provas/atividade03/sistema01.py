#Atividade 1
print ("===== Agência de Viagem =====")
print ("===== Vamos Ali =====")
nome_cliente=input("Nome do cliente: ")
print ("===== Menu Cidades =======")
print ("1. Rio de Janeiro")
print ("2. Alagoas ")
print ("3. Serra Gaucha")
opcao=int(input("Digite sua opção: "))
if opcao == 1:
    transfer= str(input("Deseja trasnfer? "))
    v_cidade=500
    nome_cidade="Rio de Janeiro"
elif opcao == 2:
    transfer= str(input("Deseja transfer? "))
    v_cidade=800
    nome_cidade="Alagoas"
elif opcao == 3:
    transfer= str(input("Deseja trasnfer? "))
    v_cidade=1000
    nome_cidade="Serra Gaucha"
hotel = int(input("Hotel de quantas estrelas? "))
dias =int(input("Ira ficar quantos dias no hotel? "))
if hotel == 3:
    v_hotel = 50
    totalhotel = v_hotel*dias
elif hotel == 4:
    v_hotel = 80
    totalhotel = v_hotel*dias
elif hotel == 5:
    v_hotel = 100
    totalhotel = v_hotel*dias
else:
    print("Opção inválida")
qtd_pessoas=int(input("Quantidade de pessoas: "))
if qtd_pessoas == 1:
    v_total = (v_cidade + totalhotel)
    print("Valor total: {:.2f}".format(v_total))
elif qtd_pessoas == 2:
    v_total = (v_cidade + totalhotel)* qtd_pessoas
    print("Cliente: {}".format(nome_cliente))
    print("Cidade: {}".format(nome_cidade))
    print("Qtd de pacotes para 2 pessoas: {}".format(qtd_pessoas))
    print("Hotel: {} Estrelas".format(hotel))
    print("Qtd dias: {}".format(dias))
    print("Transfer: {}".format(transfer))
    print("Valor total: {:.2f}".format(v_total))
else:
    print("Quantidade mínima de 2 pessoas")
