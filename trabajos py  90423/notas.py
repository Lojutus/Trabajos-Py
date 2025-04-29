print("introduce tu nota:")

alumnos=input()

def evaluacion(nota):
	valoracion="reprovado"
	if nota>2.9:
		valoracion="aprovado"
	return valoracion
print(evaluacion(int(alumnos)))