#1, 2, 3, 4, 5 e 6:

class Usuario:
  pontos = 0
  numeroDeArtigos = 0

  def setnumeroDeArtigos(self, nart):
    self.numeroDeArtigos = nart

  def getnumeroDeArtigos(self):
    return self.numeroDeArtigos

  def calcPontuacao(self):
    pass

class Autor(Usuario):
  def calcPontuacao(self):
   return self.numeroDeArtigos * 10 + 20

class Editor(Usuario):
  def calcPontuacao(self):
    return self.numeroDeArtigos * 6 + 15


autor1 = Autor()
autor1.numeroDeArtigos = 8
print(autor1.calcPontuacao())

editor1 = Editor()
editor1.numeroDeArtigos = 15
print(editor1.calcPontuacao())