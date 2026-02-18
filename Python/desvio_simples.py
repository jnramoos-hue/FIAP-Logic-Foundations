#Escreva “Digite o valor da venda: ”
#Leia venda
venda = float(input("Digite a venda: "))
#se venda  >  300 então
if venda > 300:

	#desconto = venda * 10 / 100
    desconto = venda * 10 / 100

	#venda = venda - desconto
    venda = venda - desconto

#Escreva “Novo valor =  ” , venda
print("Novo valor: " , venda)