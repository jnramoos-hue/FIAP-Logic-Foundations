ini = int(input("Digite o numeor inicial"))
f = int(input("Digite o valor final"))

for cont in range(ini, f + 1, 1):
    print(cont, " ")

while True:
    print(ini, " ")
    ini = ini + 1
    if ini > f:
        break