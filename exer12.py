eleitores = int(input("qual o total de leitoires do município? "))

validos = int(input("quantos votos foram válidos? "))
nulos = int(input("quantos votos fotam anulados? "))
brancos = int(input("quantos votaram branco? "))

percentual1 = (validos/eleitores)*100
percentual2 = (nulos/eleitores)*100
percentual3 = (brancos/eleitores)*100
print(f"o percentual de válidos foi : {percentual1}%, ja os nulos foram: {percentual2}% e os brancos foram: {percentual3}%")
