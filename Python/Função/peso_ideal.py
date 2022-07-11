def p_ideal (h, sexo):
  if sexo == 1:
    peso = (62.1 * h) - 44.7
  elif sexo == 2: 
    peso = (72.7 * h) - 58
  else:
    return 'Digite "1", caso o indivíduo seja mulher, ou "2", caso o indivíduo seja homem. '
  return peso

dados = p_ideal (1.70, 2)
print(dados)