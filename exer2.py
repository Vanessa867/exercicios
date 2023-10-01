denovo="s"
while denovo == "s" or denovo == "S":
    numero = int(input("digite um número: "))
    while numero ==0:
        numero= int(input("zero não pode! digite outro número: "))

    if numero <0:
        print("o número é negativo")
    else:
        print("o número é positivo")

    denovo = input("quer repetir?")