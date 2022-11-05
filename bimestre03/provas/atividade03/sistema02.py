#Exemplo 02
#Anderson e Kayck
print("\tMenu Delivery")
print("1. Acapulco - R$ 12,00 (unidade)")
print("2. Clandestino - R$ 14,00 (unidade)")
print("3. Cancún - R$ 10,00 (unidade) ")
print("4. Maria del Barrio - R$ 15,00 (unidade)")
resp = 1; valor = 0; pedido = 0; desconto = 0
while (resp == 1):
    opcao = int(input("\nDigite uma opção do cardapio desejada:"))
    quantidade = float(input("Informe a quantidade de tacos:"))

    if (opcao == 1):
        sabor = "Acapulco"
        pedido += quantidade * 12
        if (quantidade >= 4):
            desconto += quantidade

    elif (opcao == 2):
        sabor = "Acapulco"
        pedido += quantidade * 14
        if (quantidade >= 5):
            desconto += quantidade

    elif (opcao == 3):
        sabor = "Acapulco"
        pedido += quantidade * 10
        if (quantidade >= 4):
            desconto += quantidade

    elif (opcao == 4):
        sabor = "Acapulco"
        pedido += quantidade * 15
        if (quantidade >= 5):
            desconto += quantidade

    else:
        print("ERRO! Opção invalida!")
    valor = pedido - desconto
    resp = int(input("\nDeseja continuar 1-Sim 2-Não:"))

print(f"Total do pedido = R$ {pedido:.2f}")
print(f"Total descontado promoção = R$ {desconto:.2f}")
print(f"Total a pagar = R$ {valor:.2f}")
