#Atividade11
culo3 = salario * (15/100)
elif((salario > 699)and(salario < 1500)):
    percentual = 10
    calculo1 = (10 / 100)
    calculo2 = salario + (salario * calculo1)
    calculo3 = salario * (10/100)
elif(salario >= 1500):
    percentual = 5
    calculo1 = (5 / 100)
    calculo2 = salario + (salario * calculo1)
    calculo3 = salario * (5/100)

print("O salário antes do reajuste:{}".format(salario))
print('O percentual de aumento aplicado:{}%' .format(percentual))
print("O valor do aumento:{:.2f}".format(calculo3))
print("O novo salário seu:{}".format(calculo2))
salario = float(input("Qual o seu salario:"))
if(salario <= 280):
    percentual = 20
    calculo1 = (20 / 100)
    calculo2 = salario+(salario * calculo1)
    calculo3 = salario * (20/100)
elif((salario > 280)and(salario < 700)):
    percentual = 15
    calculo1 = (15 / 100)
    calculo2 = salario + (salario * calculo1)
    cal