print("Digite 0 para finalizar")
# zera a variável que acumula a som
soma = 0 
# para entrar no laco a primeira vez
num = 1

# inicio do laco Enquanto-faca
while num != 0: 
    # Bloco de repeticao
    num = float(input("Digite um número: "))
    soma = soma + num

# fluxo depois do final do laço: Exibir o valor da somatoria
print("Somatorioa = ", soma)