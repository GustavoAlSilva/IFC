total = 0
for i in range(1, 21):
    altura = float(input("Digite a altura: "))
    total += altura
    media = round((total / 20), 2)

print("A média é: ", media )