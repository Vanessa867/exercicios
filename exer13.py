repetir = 's'
while repetir == 's' or repetir == 'S':
    base = float(input("digite a base do retângulo: "))
    altura = float(input("digite a altura do retângulo: "))
    area = base * altura
    print(f"a área do retângulo é: {area}")

    repetir = input("gostaria de repetir? digite S para sim ou N para não: ")