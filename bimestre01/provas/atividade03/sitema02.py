#Sistema2
NM = str(input("Nome do cliente:"))
EM = str(input("Seu Jereba E-mail de contato:"))
VUP = float(input("Valor unitário do produto:"))
QTD = float(input("Quantidade:"))
VE = float(input("Valor da embalagem:"))
VF = float(input("Valor do frete:"))
VPO = (VUP * QTD) + (VE * QTD) + VF
SJ = VPO / 2
FN = VPO * 0.01
CJ = (VPO + FN) / 4
print("Valor total do pedido: {}\nEm 2x sem juros: {}\n Em 4x com juros: {}".format(VPO, SJ, CJ))
