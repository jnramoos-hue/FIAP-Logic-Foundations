n = int(input("Digite um número: "))

fat = 1

while True:
    fat = fat * n
    n = n - 1
    if n < 1:
        break
print("Fatorial = ", fat)