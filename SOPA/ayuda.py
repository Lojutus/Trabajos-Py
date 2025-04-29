
print("ingrese la letra")
sopa=str(input(""))
sopa_dividida=[]

pala_dividida=[]

#SEPARAMOS__________________________________________________________________________________
	#print(sopa[0:1])

for i in sopa:
		sopa_dividida.append(sopa[c:cd])
		c=c+1
		cd=cd+1
ayudaxd= len(sopa_dividida)
acabar = False 
posicion = -1
c=0
cd=1
while acabar == False:
    posicion = posicion + 1

    letra = sopa_dividida[posicion]
    
    if (posicion + 1) != ayudaxd:
        futuro = posicion + 1
    
    if (posicion - 1) >= 0:  # Corregido el operador "> 0" a ">= 0"
        pasado = posicion - 1

    if sopa_dividida[pasado] == ">" and sopa_dividida[futuro] == "<":
        pala_dividida.append(letra)
    
    if posicion == ayudaxd:
        acabar = True

	


	

print("su sopa dividida es:", pala_dividida)