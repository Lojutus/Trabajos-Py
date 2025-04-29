print("asignaturas disponibles")
print("asignaturas: matematicas, lenguaje, naturales, artistica")
asignaturas=["matematicas","lenguaje","naturales","artistica"]
minuscula=input("escribe la asignatura")
minuscula.lower()
asignaturas=minuscula

if minuscula in (asignaturas):
	print("Esta materia si existe:"+ minuscula)
else:
	print("esta materia no se encuntra, ")