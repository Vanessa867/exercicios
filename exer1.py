repetir = 'sim'
while repetir == 'sim':
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2)/2

    if media >=7:
        print("Aprovado!")
    elif media >=4:
        print("recuperação!")
    else:
        print("Reprovado!")

    print(f"Sua média é{media}")

    repetir = input("Quer repetir o calculo? ")
