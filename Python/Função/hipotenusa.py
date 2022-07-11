def h (co, ca):
  from math import sqrt
  hipotenusa = sqrt(co ** 2 + ca ** 2)
  return hipotenusa

catetos = h (10, 10)
print(catetos)