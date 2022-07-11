positivo = 0
somap = 0

for i in range(-10, 10):
  if i > 0:
    positivo += i
    somap += 1
  elif i < 0:
    print(i)
mediap = round((positivo / somap), 2)
print("Média dos positivos:", mediap)