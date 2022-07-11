notas = []
media = 0
acima = []
for i in range(10):
  notas.append(float(input("Digite a nota: ")))
media = sum(notas) / 10
for i in notas:
  if i > media:
    acima.append(i)
print("Quantidade de notas acima da media:", len(acima))