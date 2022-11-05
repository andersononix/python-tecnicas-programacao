a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))
if(a % 2 == 0 or a % 3 == 0):
    print("Valor de A: {}" .format(a))
    if (b % 2 == 0 or b % 3 == 0):
        print("Valor de B: {}".format(b))
        if (c % 2 == 0 or c % 3 == 0):
            print("Valor de C: {}".format(c))
            if (d % 2 == 0 or d % 3 == 0):
                print("Valor de D: {}".format(d))
else:
    print("Nenhum dos valores são divisiveis por 2 ou 3")