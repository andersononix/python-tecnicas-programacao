# Exemplo 01
# Anderson e Kayck
print("$$ Menu Comida $$")
print("1. Quesadilla - R$ 30,00 (unidade)")
print("2. Burritos - R$ 25,00 (unidade)")
print("3. Nachos - R$ 20,00 (unidade)")
print("4. Tacos - R$ 15,00 (unidade)")
print("\n$ Menu Bebida $$")
print("1. Refrigerante - R$ 8,00 (unidade)")
print("2. Suco - R$ 5,00 (unidade)")
print("3. Bebida Picante - R$ 15,00 (unidade)\n")
resp = 1
qtd_total_b = 0
qtd_total_c = 0
while (resp == 1):
    op = int(input("digite a opcao da comida:"))
    qtd = int(input("Qual comida vai querer:"))
    if(op == 1):
        qtd_total_c += qtd * 30

    elif(op == 2):
        qtd_total_c += qtd * 25

    elif(op == 3):
        qtd_total_c += qtd * 20

    elif(op == 4):
        qtd_total_c += qtd * 15

    else:
        print("Opcao invalida")
    resp = float(input("Deseja Fazer outro pedido? 1.sim e 2.não:"))

    while (resp == 2):
        op = int(input("digite a opcao da bebida:"))
        qtd = int(input("Qual bebida vai querer:"))
        if(op == 1):
            qtd_total_b += qtd * 8

        elif(op == 2):
            qtd_total_b += qtd * 5

        elif(op ==  3):
            qtd_total_b += qtd * 15

        else:
            print("opção invalida")
        resp = int(input("Deseja Fazer outro pedido 2.sim e 3.nao"))
cal = qtd_total_c + qtd_total_b
print(f"Valor total de comida= {qtd_total_c:.2f}")
print(f"valor total da bebida:{qtd_total_b:.2f}")
print(f"valor total da bebida:{cal:.2f}")
