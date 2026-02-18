#Solicitar ao usuário que digite S para sim ou N para não obrigatioriamente
#Entrada 1:
    #Digite [S]im ou [N]ão: 
#Saída 1
    #Você digitou S ou N

#Solicitar ao usuário que digite S para sim ou N para não obrigatioriamente
#Entrada 1:
    #Digite [S]im ou [N]ão: H 
#Saída 1
    #Você digitou 'H', digite  S ou N

opcao = input("Digite [S]im ou [N]ão: ")
while opcao != 's' and opcao != 'S' and opcao != 'n' and opcao != 'N':
    print("Você digitou ", opcao, "digite S ou N!")
    opcao = input("Digite [S]im ou [N]ão: ")
print("Voce digitou ", opcao)
