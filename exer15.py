valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
while valor1 == valor2:
    valor2 = float(input("os valores não podem ser iguais!  digite novamente: "))

if valor1 > valor2:
    print(f"em ordem crescente: {valor1}, {valor2}")
else:
    print(f"em ordem crescente: {valor2}, {valor1}")
