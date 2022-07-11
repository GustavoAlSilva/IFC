#1, 2, 3, 4, 5 e 6:

class Usuario:
  nome=""

  def ola(self):
    print("Olá," ,self.nome)
    return self

  def registrar(self):
    print("Registrado;")
    return self

  def email(self):
    print(("E-mail enviado."))

usuario1=Usuario()
usuario1.nome="Jane"
usuario1.ola().registrar().email()