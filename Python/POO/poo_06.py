#1, 2, 3, 4, 5, 6, 7, 8, 9 e 10:

class Usuario():
  _nomeUsuario = ""

  def setnomeUsuario(self, nomeUsuario):
    self._nomeUsuario = nomeUsuario

  def getnomeUsuario(self):
    return self._nomeUsuario

class Admin(Usuario):

  def escrevaNome(self):
    return "Admin"

  def digaOla(self):
    print("Olá Admin, " + self.getnomeUsuario())

admin1 = Admin()
admin1._nomeUsuario = "Gustavo"
admin1.digaOla()
