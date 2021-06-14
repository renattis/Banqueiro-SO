class Banqueiro:
	def __init__(self, saldo, lista):
		self.saldo = saldo
		self.saldo_total = saldo
		self.lista = lista
		self.lista_espera = []


class Pessoa:
	def __init__(self, nome, codigo):
		self.nome = nome
		self.codigo = codigo
		self.saldo = 0
		self.devendo = False
		self.ciclo = 0
