inicio = int(input("Digite a hora de início do jogo: "))
fim = int(input("Digite a hora de fim do jogo: "))

if inicio > fim:
    duracao = (24 - inicio) + fim
else:
    duracao = fim - inicio

print(f"a duração do jogo é de: {duracao} horas")

while duracao > 24:
    print("O jogo excedeu o tempo máximo permitido de 24 horas.")
    break
