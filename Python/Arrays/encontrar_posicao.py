numeros = []
for i in range(10):
  numeros.append(int(input("Digite um número: ")))
for i in range(len(numeros)):
  if numeros[i] == 30:
    print("Existe um número 30 na posição: ", i)