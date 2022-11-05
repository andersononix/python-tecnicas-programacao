salario=float(input("salário: "))
if salario < 280:
    print("20%")
    salario=salario+(salario*0.2)
    print(salario)
elif salario > 280 and salario < 700:
    vhora = float(input("Valor hora: "))

    horast = float(input("Horas trabalhadas: "))

    salbruto = vhora * horast

    if salbruto <= 900:

        ir = 0

        inss = salbruto * 0.1

        fgts = (salbruto * 0.11)

        total = ir + inss + fgts

        salliq = salbruto - total

        print("=" * 40)

        print(f"""Salario Bruto: ({vhora}*{horast})    :R$ {salbruto}

    (-) IR (0%)                   :R$ {ir}

    (-) INSS (10%)                :R$ {inss}

    FGTS (11%)                    :R$ {fgts}

    Total de descontos            :R$ {total}

    Salário Liquido               :R$ {salliq}""")



    elif salbruto > 900 and salbruto <= 1500:

        ir = salbruto * 0.05

        inss = salbruto * 0.1

        fgts = (salbruto * 0.11)

        total = ir + inss + fgts

        salliq = salbruto - total

        print("=" * 40)

        print(f"""Salario Bruto: ({vhora}*{horast})    :R$ {salbruto}

    (-) IR (5%)                   :R$ {ir}

    (-) INSS (10%)                :R$ {inss}

    FGTS (11%)                    :R$ {fgts}

    Total de descontos            :R$ {total}

    Salário Liquido               :R$ {salliq}""")




    elif salbruto > 1500 and salbruto < 2500:

        ir = salbruto * 0.1

        inss = salbruto * 0.1

        fgts = (salbruto * 0.11)

        total = ir + inss + fgts

        salliq = salbruto - total

        print("=" * 40)

        print(f"""Salario Bruto: ({vhora}*{horast})    :R$ {salbruto}

    (-) IR (10%)                  :R$ {ir}

    (-) INSS (10%)                :R$ {inss}

    FGTS (11%)                    :R$ {fgts}

    Total de descontos            :R$ {total}

    Salário Liquido               :R$ {salliq}""")




    elif salbruto > 2500:

        ir = salbruto * 0.2

        inss = salbruto * 0.1

        fgts = (salbruto * 0.11)

        total = ir + inss + fgts

        salliq = salbruto - total

        print("=" * 40)

        print(f"""Salario Bruto: ({vhora}*{horast})    :R$ {salbruto}

    (-) IR (20%)                   :R$ {ir}

    (-) INSS (10%)                :R$ {inss}

    FGTS (11%)                    :R$ {fgts}

    Total de descontos            :R$ {total}

    Salário Liquido               :R$ {salliq}""")