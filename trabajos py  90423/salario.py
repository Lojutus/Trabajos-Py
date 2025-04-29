salariop=int(input("intoduce el salario del presidente"))
print("salario presidente:"+ str(salariop))

salarioD=int(input("intoduce el salario del director"))
print("salario DIRECTOR:"+ str(salarioD))

salarioJ=int(input("intoduce el salario del Jefe area"))
print("salario Jefe de area:"+ str(salarioJ))


if salariop>salarioD>salarioJ:
	print("todo esta bien")
else:
	print("Algo esta mal en esta empresa")