# Solicitando os dados ao usuário
preco_maco = float(input("Digite o preço do maço: "))
qtd_maco = int(input("Digite a quantidade de maços por dia: "))
anos = float(input("Digite o número de anos que você fuma: "))

# Calcula a quantidade de dias como fumante
dias_fumante = anos * 365

# Calcula o custo total
custo = dias_fumante * qtd_maco * preco_maco

# Exibe o custo 
print("Voce já gastou {:.2f} fumando.".format(custo))