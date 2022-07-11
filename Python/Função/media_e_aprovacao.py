def media (n1, n2):
  m = (n1 + n2) / 2
  if m >= 6:
    return m, "PARABÉNS! Você foi aprovado!"

notas = media (6, 8)
print(notas)