vetor1 = []
vetor2 = []
vetor3 = []
for i in range(3):
  n1 = float(input("Digite um número real: "))
  vetor1.append(n1)
for i in range(3):
  n2 = float(input("Digite um número real: "))
  vetor2.append(n2)
vetor3 = vetor1[0] + vetor2[0]

print("Vetor1:", vetor1, "\nVetor2:", vetor2, "\nVetor3:", vetor3)