#lista_Economica = []
#lista_Executiva = []
#lista_Primeira = []
login = str(input("login:"))
senha = str(input("senha:"))
op = 1
if(login == 'admin')and(senha == 'admin'):
    print("Menu\n1 - Cadastrar: Armazenar e Imprimir\n2 - Excluir")
    while (op == 1):
        data = str(input("Qual é a data de partida:"))
        print("[1]-EUA\n[2]-África\ndo Sul\n[3]-Japão")
        local = int(input("Qual o local que deseja:"))
        print("[1]-Classe Econômica\n[2]-Executiva\ndo Sul\n[3]-Primeira classe")
        classes = int(input("Escolha uma classe:"))
        print("[1]-3 estrelas (R$ 100,00 por dia)\n[2]-4 estrelas(R$ 200,00 por dia)\n[3]-5 estrelas (R$ 300,00 por dia)")
        hospedagem = int(input("Escolha um tipo:"))
        if(hospedagem == 1):
            hospedagem = 100
        elif(hospedagem == 2):
            hospedagem = 200
        else:
            hospedagem = 300
        quantidade_dias = int(input("Quantidade de dias:"))
        op = int(input("escolha uma op :"))
        while (op == 2):
            excluir = int(input("Oq vc deseja escluir:"))
print(f'{data}')
print(f'{local}')
print(f'{quantidade_dias}')