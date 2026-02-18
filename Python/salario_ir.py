#Escreva “Digite o salário:  ”
#Leia sal
sal = float(input("Digite o seu salário: "))
#Se sal <= 1900 então
if sal <= 1900:
    #ir = 0
    ir = 0
#Senão
else:
	#Se sal <= 2800 então
    if sal <= 2800:
		#ir = sal * 0.15
        ir = sal * 0.15

		#senão   
    else:
		#ir = sal * 0.275
        ir = sal * 0.275
		#fim_se
	#fim_se
#sal_li = sal - ir
sal_liq = sal - ir

#Escreva “IR: ” , ir
print(f"IR: {ir: .2f} ")

#Escreva “Salário Liquido: ”, sal_liq
print(f"Salário Líquido: {sal_liq:.2f}")