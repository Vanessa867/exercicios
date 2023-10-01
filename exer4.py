dnv = 's'
while dnv == 's':
    num1 = float(input("digite o primeiro número"))
    num2 = float(input("digite o segundo número"))
    num3 = float(input("digite o terceiro número"))

    if num1 > num2:
        print(num1)
    elif num2> num3:
        print(num2)
    else:
        print(num3)

    dnv = input("iae vc quer  testar dnv? ")