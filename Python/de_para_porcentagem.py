#Leia valor
valor = input("Digite o valor: £")
valor = float(valor)
#Escreva “Digite a porcentagem: ”
porc = input("Digite a porcentagem: ")
porc = float(porc)
# Calcular o percentual
perc = valor * porc / 100
# Calcular o acrescimo
acresc = valor + perc
# Calcular o desconto
desc = valor - perc

#Escreva “Percentual: ”, perc
print("Percentual: ", perc)
#Escreva ”Acrescimo: ”, acresc
print("Acréscimo: ", acresc)
#Escreva ”Desconto: ”, desc
print("Desconto: ", desc)