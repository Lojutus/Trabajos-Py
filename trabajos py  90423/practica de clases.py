class coche():
	alto=90 
	ancho=30 
	ruedas=4
	enmarcha=False

	def arrancar(self):
		self.enmarcha=True
	def apagar(self):
		self.enmarcha=False
	def estado(self):
		if(self.enmarcha):
			return "esta andando capo"
		else:
			return "zzzzz"
camion=coche()
camion.arrancar()
print(camion.estado())
camion.apagar()
print(camion.estado())