#Escreva “Digite o seu tempo de casa:”
#Leia tc
tc = int(input("Digite o seu tempo de casa:"))
               
#Escreva “Digite o seu salário: ”
#Leia sal
sal = float(input("Digite o seu salário: "))
                  
#Se tc < 3 então
if tc < 3:
    #aumento = salário * 0.05
    aumento = sal *0.05

#Senão
#aumento = salário * 0.1
else:
    aumento = sal * 0.1
#fim_se

#novo_sal = sal + aumento
novo_sal = sal + aumento
#Escreva ”O seu salário foi de”, sal, “ para” ,  novo_sal
print("O seu salário foi de: ", sal, "para ", novo_sal)