n = int(input("Digite um número: "))

fat = 1

while n > 1:
    fat = fat * n
    n = n - 1

print("Fatorial = ", fat)