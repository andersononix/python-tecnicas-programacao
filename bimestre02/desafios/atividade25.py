#Atividade25
print("Vou fazer algumas perguntas responda[Sim ou Não]")
print("-" *30)
a = str(input("Você Telefonou para a vítima:")) .upper()
b = str(input("Esteve no local do crime:")) .upper()
c = str(input("Mora perto da vítima:")) .upper()
d = str(input("Devia para a vítima:")) .upper()
e = str(input("Já trabalhou com a vítima?:")) .upper()
p = 0
if(a == "Sim"):
    p = p + 1
if(b == "Sim"):
    p = p + 1
if(c == "Sim"):
    p = p + 1
if(d == "Sim"):
    p = p + 1
if(e == "Sim"):
    p = p + 1
if(p == 2):
    print("Suspeito!!!")
    print(" [Você]  /﹋\.")
    print("        (҂`_´)")
    print("        <,︻╦╤─ ")
    print("         _/ \_")
elif((p == 3)or(p== 4)):
    print("Cúmplice")
    print("[Assassino] /﹋\  [Você]  /﹋\.")
    print("           (҂`_´)        (҂`_´)")
    print("           <,︻╦╤─҉ - -   <,︻╦╤─ ҉ - -")
    print("            /﹋\.         _/ \_")
elif(p == 5):
    print("Assassino!!!")
    print("[Você] /﹋\           /﹋\.")
    print("      (҂`_´)        (`_´҂)")
    print("      <,︻╦╤─ ҉ - -   <|>")
    print("       /﹋\.         _/ \_")
else:
    print("Inocente")
    print(" /﹋\.")
    print("(҂`_´)")
    print(" <|> ")
    print(" /﹋\.")
