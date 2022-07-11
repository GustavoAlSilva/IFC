par = 0
somap = 0
impar = 0
somai = 0

for i in range(2, 100):
    if i % 2 == 0:
        par += i
        somap += 1
    else:
        impar += i
        somai += 1
print("A soma dos pares é:", par)
print("A soma dos impares é:", impar)