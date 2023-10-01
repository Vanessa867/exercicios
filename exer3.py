idade = int(input("Qual é a sua idade? "))
mes = input("qual o mês de nascimento? ")
mesatual = input("qual mês atual")
ano = 2023 - idade
if mesatual <= mes:
    print(f"Você nasceu em{ano}")
else:
    ano1 =  ano-1
    print(f" você nasceu em {ano1}")
