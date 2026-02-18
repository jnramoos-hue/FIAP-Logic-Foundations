# Solicita a quantia
quantia = int(input("Digite a quantia: "))
# Efetua o cálculo das quantias de cédulas 
ced50 = quantia // 50
quantia = quantia % 50
ced20 = quantia // 20
quantia = quantia % 20
ced10 = quantia // 10
quantia = quantia % 10
# Exibe as quantidade de cédualas
print("Quantidade de cédulas de 50:", ced50)
print("Quantidade de cédulas de 20:", ced20)
print("Quantidade de cédulas de 10:", ced10)