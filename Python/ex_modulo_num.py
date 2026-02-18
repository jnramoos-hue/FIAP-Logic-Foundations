#exibe “Solicita um número para o usuário”
#Escreva”Digite um numero: ”
n = int(input("Digite um número: "))

#Comando de decisão: Verifica se o número é negativo
#Se n <  0 então
#n = n * -1
if n <  0:
    n = n * -1
#Fim_se

#//Exibe o número positivo
#Escreva “Módulo: ”, n
print("Módulo: ", n)