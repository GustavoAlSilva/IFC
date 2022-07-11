# usando a biblioteca "math" invés de "IF"
m = float(input("Digite a metragem quadrada à ser pintada: "))
latas = m / 3 / 18 
from math import ceil
valor = ceil(latas) * 80
print("Quantidade de lata de tinta necessária:", ceil(latas), "\nValor a se pagar: R$", valor)