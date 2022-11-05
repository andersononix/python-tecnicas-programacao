A = float(input("Digite vum numero:"))
B = float(input("Digite vum numero:"))
C = float(input("Digite vum numero:"))
if( (A < B + C) and ( B < A +C ) and ( C < A + B)):
    print("È um triangulo")
else:
    print("Não é um triangulo")