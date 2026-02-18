n =int(input("Digite um número: "))

volta = n
fat = 1

for volta in range(n, 1, -1):
    fat = fat * volta

print("Fatorial: ", fat)