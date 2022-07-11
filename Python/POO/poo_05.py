#1, 2, 3, 4 e 5:

class Usuario():
  __primeiroNome = ""
  __ultimoNome = ""

  def __init__(self, primeiroNome = None, ultimoNome = None):
    if primeiroNome != None and ultimoNome != None:
      self.__primeiroNome = primeiroNome
      self.__ultimoNome = ultimoNome

  def getnomeCompleto(self):
    return ("" + self.__primeiroNome + " " + self.__ultimoNome)

usuario1 = Usuario("Gustavo", "Almeida da Silva")
print(usuario1.getnomeCompleto())