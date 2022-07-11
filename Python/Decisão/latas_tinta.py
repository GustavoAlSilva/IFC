m = float(input("Digite a metragem quadrada à ser pintada: "))
latas = m / 3 / 18 
if latas % 1 != 0:
  latas = latas + 1
valor = int(latas) * 80
print("Quantidade de lata de tinta necessária:", int(latas), "\nValor a se pagar: R$", valor)