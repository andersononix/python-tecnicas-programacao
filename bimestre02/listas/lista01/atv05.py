print("1 - homem\n2 - mulher")
sexo = int(input("Digite seu sexo:"))
altura = float(input("Digite sua altura:"))
if(sexo == 1):
    homem = (72.7 * altura) - 58
    print("Seu sexo é Masculino")
    print("Seu peso ideal é: {:.2f}" .format(homem))
else:
    mulher = (62.1 * altura) - 44.7
    print("Seu sexo é Feminino")
    print("Seu peso ideal é: {:.2f}" .format(mulher))