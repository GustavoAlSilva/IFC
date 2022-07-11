peso = int(input("Digite o peso da pesca: "))
excesso = peso - 50
multa = excesso * 4
if peso > 50:
  print("O peso excedeu em:", excesso, "kg", "\nA Multa: R$", multa)
else:
  print("O peso excedeu em: 0", "kg", "\nA Multa: R$0")