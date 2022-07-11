n = int(input("Digite o valor a ser fatorado: "))
total = n
for i in range(2, n):
  total = i * total
print(total)