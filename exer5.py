repetir = 's'
while repetir == 's' or repetir == 'S':
    num = float(input("Digite um número: "))
    if num % 2:
        print("Esse número é ímpar!")
    else:
        print("Esse número é par!")

    repetir = input("quer testar outra vez? ")