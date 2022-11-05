#Sistema1
n = str(input("Nome do produto:"))
ctp = float(input("total do produto:"))
pdf = float(input("Percentual das despesas fixas:"))
mld = float(input("Margem de Lucro desejada:"))
pv = (ctp / (100 - pdf - mld))
vl = (ctp / 65) * 100
print(" Saída O preço final da camisa é {:.2f}" .format(vl))
