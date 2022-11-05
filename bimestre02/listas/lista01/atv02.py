p = float(input("Digite a sua Nota da prova:"))
a = float(input("Digite a sua Nota das Atividades:"))
c = p + a
if(c >= 7):
    print("Aprovado com a media: {}" .format(c))
else:
    print("Rodado com a media: {}" .format(c))