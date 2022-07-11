var1 = []
var2 = []
var3 = []

print("Valores da primeira variável: ")
for i in range(3):
  var1.append(float(input("Digite um numero: ")))
print("Valores da segunda variável: ")
for i in range(3):
  var2.append(float(input("Digite um numero: ")))
var3 = var1 + var2
print("Terceira variável: ", var3)