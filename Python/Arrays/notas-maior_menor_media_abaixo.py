notas = [1, 1.5, 1.9, 2, 2.5, 2.5, 3, 3.7, 4, 5.3, 5.8, 5.9, 6.5, 8, 6.5, 7, 7.6, 8, 8, 8, 8, 8, 8.5, 8.5, 8.5, 9, 9, 9, 9, 10]
media = 0
abaixo = []
notas.sort()
maior = notas[-1]
menor = notas[0]
media = sum(notas) / 30
media = round(media, 2)
for i in notas:
  if i < media:
    abaixo.append(i)

print("Maior nota:", maior, "\nMenor nota:", menor, "\nMédia:", media, "\nQuantidade de notas abaixo da média:", len(abaixo))