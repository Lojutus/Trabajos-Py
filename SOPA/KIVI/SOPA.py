c=0
cd=1
Posicion_en_la_lista=0
v=0
posicion=0
comenzar=False	
cz=1
	
ct=0
cm=0
	
posicion_antes=0

ab=0
def Solucionar():
	global c,cd,Posicion_en_la_lista,v,posicion,comenzar,cz,ct,cm, posicion_antes, ab

	Resultado =("Palabra no encontrada")


	# INICIO__________________________________________________________________________

	#INICIO__________________________________________________________________________
	while comenzar==False:
		try:
			with open("Ancho.txt", "r") as archivo:
				Y=int(archivo.read())
			with open("Sopa.txt", "r") as archivo:
				sopa=str(archivo.read())
				sopa=sopa.upper()
			with open("Palabras.txt", "r") as archivo:
			
				palabra=str(archivo.read())
				palabra=palabra.upper()
				comenzar=True
		
			

			
		except:
			Respuesta=("agregue caracteres validos")
	sopa_dividida=[]
	pala_dividida=[]

	#SEPARAMOS__________________________________________________________________________________
	#print(sopa[0:1])
	for i in sopa:
		sopa_dividida.append(sopa[c:cd])
		c=c+1
		cd=cd+1
	c=0
	cd=1
	for i in palabra:
		pala_dividida.append(palabra[c:cd])
		c=c+1
		cd=cd+1
	#FUNCIONES_______________________________________________________________________________________
	posicion_antes=Posicion_en_la_lista
	cm=len(sopa_dividida)
	cz=len(pala_dividida)
	def siguiente():
		global comenzar,ct,Posicion_en_la_lista,posicion
		comenzar=0
		ct=0
		Posicion_en_la_lista=0
		posicion=sopa_dividida[Posicion_en_la_lista]
		Reiniciar()
	def es_multiplo(numero, multiplo):
		# Si el residuo es 0, es múltiplo
		if numero % multiplo == 0:
			return True
		else:
			return False
	def Reiniciar():
		global posicion,ct
		
		posicion=sopa_dividida[Posicion_en_la_lista]

		
	def Seguir():
		global posicion,posicion_antes,Posicion_en_la_lista,comenzar,cm
		comenzar=comenzar+1	
		posicion_antes=Posicion_en_la_lista
		if Posicion_en_la_lista<cm-1:
			Posicion_en_la_lista=Posicion_en_la_lista+1
			posicion=sopa_dividida[Posicion_en_la_lista]
			
	ct=0
	def Escanear_entorno():
		global posicion
		
		if posicion == pala_dividida[ct]:
			return True
	Reiniciar()
	print(pala_dividida)
	print(sopa_dividida)
	print(ct,cz,cm)
	#BUCLE_______________________________________________________________________________________
	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
					
					if posicion==pala_dividida[ct]:
						ct=ct+1
						
						
						if Posicion_en_la_lista<cm-1:
							Posicion_en_la_lista=Posicion_en_la_lista+1
							posicion=sopa_dividida[Posicion_en_la_lista]
							
						if ct==cz:
							Resultado=("Primer for","PALABRA ENCONTRADA",Posicion_en_la_lista-cz+1,Posicion_en_la_lista)
							comenzar=cm
							print("Primer for")
							Reiniciar()

					else:
						
						ct=0
						Reiniciar()

		ct=0		
		Seguir()
	siguiente()

	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
					
					if posicion==pala_dividida[ct]:
						ct=ct+1
						if Posicion_en_la_lista>0:
							
							Posicion_en_la_lista=Posicion_en_la_lista-1
							posicion=sopa_dividida[Posicion_en_la_lista]
							
						if ct==cz:
							Resultado=("Segundo for","PALABRA ENCONTRADA",Posicion_en_la_lista+2,Posicion_en_la_lista+cz+1)
							comenzar=cm
							print("segundo for")
							Reiniciar()

					else:
						
						ct=0
						
						Reiniciar()
						
		ct=0		
		Seguir()

	siguiente()

	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
					
					if posicion==pala_dividida[ct]:
						ct=ct+1
						if Posicion_en_la_lista>Y:
							
							Posicion_en_la_lista=Posicion_en_la_lista-Y
							posicion=sopa_dividida[Posicion_en_la_lista]
							
						if ct==cz:
							Resultado=("PALABRA ENCONTRADA",Posicion_en_la_lista+(Y*(cz-1))+1,Posicion_en_la_lista+1)
							comenzar=cm
							print("CUARTO for")
							Reiniciar()

					else:
						
						ct=0
						
						Reiniciar()
		ct=0		
		Seguir()
	siguiente()
	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
					
					if posicion==pala_dividida[ct]:
						ct=ct+1
						if cm>(Posicion_en_la_lista+Y):
							
							Posicion_en_la_lista=Posicion_en_la_lista+Y
							posicion=sopa_dividida[Posicion_en_la_lista]
							
						if ct==cz:
							Resultado=("PALABRA ENCONTRADA",Posicion_en_la_lista+1,Posicion_en_la_lista-(Y*(cz-1)))
							comenzar=cm
							print("QUINTO for")
							Reiniciar()

					else:
						
						ct=0
						
						Reiniciar()
		ct=0		
		Seguir()
	siguiente()
	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
					
					if posicion==pala_dividida[ct]:
						ct=ct+1
						Guardar=es_multiplo(Posicion_en_la_lista,(Y))
						
						if Guardar==False:
							Posicion_en_la_lista=Posicion_en_la_lista-Y-1
							posicion=sopa_dividida[Posicion_en_la_lista]
							
						if ct==cz:
							Resultado=("PALABRA ENCONTRADA",Posicion_en_la_lista+1,Posicion_en_la_lista+(Y*(cz)))
							comenzar=cm
							print("SEXTO for")
							Reiniciar()

					else:
						
						ct=0
						
						Reiniciar()
		ct=0		
		Seguir()
	siguiente()
	ab=Y+Y-1
	#si da problemas a futuro revisa esto, la verdad no se poque funciona pero ahi anda
	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
					
					if posicion==pala_dividida[ct]:
						ct=ct+1
						
						Guardar=es_multiplo(Posicion_en_la_lista,(ab))
						
						if Guardar==False or Y>Posicion_en_la_lista:
							
							Posicion_en_la_lista=Posicion_en_la_lista-Y+1
							posicion=sopa_dividida[Posicion_en_la_lista]
							
						if ct==cz:
							Resultado=("PALABRA ENCONTRADA",Posicion_en_la_lista+Y,Posicion_en_la_lista+(Y*(cz-1))+1)
							comenzar=cm
							print("septimo for")
							Reiniciar()

					else:
						
						ct=0
						
						Reiniciar()
		ct=0		
		Seguir()
	siguiente()
	ab=Y-1
	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
				
					if posicion==pala_dividida[ct]:
						ct=ct+1
						Guardar=es_multiplo(Posicion_en_la_lista,(cm+1))
						
						if (Posicion_en_la_lista+Y+1)<cm:
							
							Posicion_en_la_lista=Posicion_en_la_lista+Y+1
							
							posicion=sopa_dividida[Posicion_en_la_lista]

						if ct==cz:
							Resultado=("PALABRA ENCONTRADA",Posicion_en_la_lista-(Y*(cz)),Posicion_en_la_lista-1,)
							comenzar=cm
							print("octavo for")
							Reiniciar()

					else:
						Posicion_en_la_lista=posicion_antes+1
						ct=0
						
						Reiniciar()
		ct=0		
		Seguir()
	siguiente()
	ab=Y
	while comenzar<cm:
		if Escanear_entorno()==True:
				for i in range(cz):
				
					if posicion==pala_dividida[ct]:
						ct=ct+1
						Guardar=es_multiplo(Posicion_en_la_lista,(Y))
						
						if Guardar==False and Posicion_en_la_lista<(cm-Y):
							
							Posicion_en_la_lista=Posicion_en_la_lista+Y-1
							posicion=sopa_dividida[Posicion_en_la_lista]					
						if ct==cz:
							Resultado=("PALABRA ENCONTRADA",Posicion_en_la_lista+1,Posicion_en_la_lista-(Y*(cz-2)))
							comenzar=cm
							print("NOVENO for")
							Reiniciar()

					else:
						
						ct=0
						
						Reiniciar()
		ct=0		
		Seguir()
	siguiente()

	siguiente()
	print("PROGRESSFUL")
	return Resultado
print(Solucionar())
	###if es_multipo(Posicion_en_la_lista,Y)==True: