X = float(input("Digite vum numero:"))
Y = float(input("Digite vum numero:"))
Z = float(input("Digite vum numero:"))
if( (X == Y)and(Y == X)and(Z == X)and(X == Z)and(Y == Z)and(Z == Y)):
    print("È um triângulo equilátero")
else:
    print("Não È equilátero")
    if( (X > Y)and(Y < X)and(Z == X )and(X== Z)and(Z > Y)and(Y < Z)):
        print("È um triângulo isósceles")
    else:
        print("Não È isósceles")
        if( (X < Y) and (Y > X) and (Z > X)and(X < Z)and(Z > Y)and(Y < Z)):
            print("È um triângulo escaleno.")
        else:
            print("Não È escaleno")