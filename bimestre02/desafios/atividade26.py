#atividade26
print("\t" * 5 + 'TABELA DE COMBUSTIVEL')
print("_" * 58)
print("Tipo de combustivel {}╏{} Numero comrespontende" .format(('\t' * 2), ('\t' * 2)))
print("_" * 58)
print("Álcool {}╏{} 1"      .format(('\t' * 6), ('\t' * 4)))
print("Gasolina {}╏{} 2"    .format(('\t' * 5), ('\t' * 4)))
print("_" * 58)
combustivel = int(input("\nQual o tipo de combustve:"))
if(combustivel == 1):
    tipo_combustivel = "Àlcool"
    print("")
    print("\t" * 5 + "TABELA ÁLCOOL")
    print("Litros{}╏{}Desconto"     .format(("\t" * 6), ("\t" * 3)))
    print("20L {}╏{} 3%"            .format(("\t" * 6), ("\t" * 3)))
    print("Acima de 20L {}╏{} 5%"   .format(("\t" * 4), ("\t" * 3)))
    litro = float(input("Quantidade de Litros:"))
    if (litro <= 20):
        percentual = 3
        valor_pagar = (2.50 * litro) - percentual / 100
    else:
        percentual = 5
        valor_pagar = (2.50 * litro) - percentual / 100
else:
    tipo_combustivel = "Gasolina"
    print("")
    print("\t" * 5 + "TABELA GASOLINA")
    print("Litros{}╏{}Desconto".format(("\t" * 6), ("\t" * 3)))
    print("20L {}╏{} 4%".format(("\t" * 6), ("\t" * 3)))
    print("Acima de 20L {}╏{} 6%".format(("\t" * 4), ("\t" * 3)))
    litro = float(input("Quantidade de Litros:"))
    if (litro <= 20):
        percentual = 4
        valor_pagar = (1.90 * litro) - percentual / 100
    else:
        percentual = 6
        valor_pagar = (1.90 * litro) - percentual / 100
print("\nTipo de combustivel                          {}".format(tipo_combustivel))
print("O percentual de desconto aplicado            {}%" .format(percentual))
print("Valor a pagar                                R$ {:.2f}".format(valor_pagar))
