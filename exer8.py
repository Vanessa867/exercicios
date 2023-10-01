quantidade = int(input(" Digite quantos números serão: "))
soma = 0
for x in range(quantidade):
    numero = float(input(" digite o número: "))
    soma = soma +numero
media = soma/ quantidade
print(f"a soma dos números é {soma} e a média é{media}")