notas = []
for i in range(10):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
media = sum(notas) / 10
media = round(media, 2)
print(media)