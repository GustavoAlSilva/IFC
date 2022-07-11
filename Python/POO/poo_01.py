# Lista de exercícios com 4 questões objetivas.


#1: Alternativa B

#2: Alternativa A

#3: Alternativa B

#4: Alternativa A


#5, 6, 7, 8, 9, 10 e 11:

class Usuario():
  nome = ""
  sobrenome = ""

  def ola(self):
    return "Olá"

usuario1 = Usuario()
ola = usuario1.ola()
usuario1.nome = "Gustavo"
usuario1.sobrenome = "Silva"
print(ola, usuario1.nome, usuario1.sobrenome, "!")

usuario2 = Usuario()
usuario2.nome = "Fulano"
usuario2.sobrenome = "Almeida"
print(ola, usuario2.nome, usuario2.sobrenome, "!")