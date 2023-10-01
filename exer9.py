while True:
    num = int(input(" digite um número inteiro: "))
    pergunta = input("Digite 1 para mostrar o sucessor e 2 para mostar o antecessor e 3 para finalizar: ")

    if pergunta == "1":
        print(num+1)
    elif pergunta == "2":
        print(num-1)
    else:
        break
