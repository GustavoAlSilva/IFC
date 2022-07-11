# Lista de exercícios com 1 questão objetiva.


#1: Alternativa D


#2, 3, 4 e 5:

class Usuario(): 

  __primeiroNome = "" 

  def setprimeiroNome(self, primeiroNome):
    self.__primeiroNome = primeiroNome

  def getprimeiroNome(self):
    return self.__primeiroNome

usuario1 = Usuario()
usuario1.setprimeiroNome("Joe")
print(usuario1.getprimeiroNome())