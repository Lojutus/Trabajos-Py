def devulve_ciudades(*ciudades):
	for elemento in ciudades:
		yield from elemento

devuelto=devulve_ciudades("madrid","barcelona","bilbao","valencia")

for i in devuelto:
	print(i)
