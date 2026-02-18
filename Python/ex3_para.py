n = int(input("Digite um número"))

mult = 1

# Laço configurado para 10 voltas
for i in range(1, 11, 1):
    mult = i * n
    print(f"{n} X {i} = {mult}")