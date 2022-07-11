# Lista de exercícios com 1 questão objetiva.


#1: Alternativa C


#2, 3 e 4:

class Usuario():
  nome = ""
  sobrenome = ""
 
  def ola (self):
    return "Olá!" + " " + self.nome + " " + self.sobrenome

usuario1 = Usuario()
usuario2 = Usuario()

usuario1.nome = "Jonnie"
usuario1.sobrenome = "Bravo"

usuario2.nome = "Gustavo"
usuario2.sobrenome = "Silva"

print(usuario1.ola())
print(usuario2.ola())