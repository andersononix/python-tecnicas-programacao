print("1 - Fusca\n2 - BMW\n3 - Gol")
carro = int(input("Digite um carro:"))
km = float(input("Digite quantos quilometros pecorrido:"))
if(carro == 1):
    comsumo = km / 8
    print("Tipo de carro: Fusca")
    print("Quanto de compustivo: {}" .format(comsumo))
elif (carro == 2):
    comsumo = km / 9
    print("Tipo de carro: BMW")
    print("Quanto de compustivo: {}".format(comsumo))
elif (carro == 3):
    comsumo = km / 12
    print("Tipo de carro: Gol")
    print("Quanto de compustivo: {}".format(comsumo))
else:
    print("ERRO! Esse carro não tem!!!")
