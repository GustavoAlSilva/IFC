a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if a < c+b and b < a+c and c < a+b and a > b-c and a > c-b and b > a-c and b > c-a and c > a-b and c > b-a:
  if a == b == c:
    print("Triângulo equilátero")
  elif a != b != c:
    print("Triângulo escaleno")
  else:
    print("Triângulo isósceles")
else:
  print("Não é um triângulo")