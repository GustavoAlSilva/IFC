a = float(input("Digite o número a: "))
b = float(input("Digite o número b: "))
c = float(input("Digite o número c: "))
if a > b and a > c:
  print("O maior número é", a)
elif b > c:
  print("O maior número é", b)
else:
  print("O maior número é", c)
if a < b and a < c:
  print("O menor número é", a)
elif b < c:
  print("O menor número é", b)
else:
  print("O menor número é", c)