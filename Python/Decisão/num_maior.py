a = float(input("Digite o número a: "))
b = float(input("Digite o número b: "))
c = float(input("Digite o número c: "))

if a > b and a > c:
  print("Maior número:", a)
elif b > c:
  print("Maior número:", b)
else:
  print("Maior número:", c)