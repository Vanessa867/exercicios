base = int(input("Qual a base do triangulo: "))
while base <=0:
    base = int(input("Zero não pode! digite dnv: "))
altura = int(input("Qual a altura do triangulo: "))
while altura <=0:
    altura= int(input("Zero não pode! digite dnv: "))
formula = (base * altura)/2
print(f" o resultado é {formula}")