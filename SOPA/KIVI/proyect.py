from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
# DEclaramos variables________________________________
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
		global posicion,ct, Posicion_en_la_lista
		
		posicion=sopa_dividida[Posicion_en_la_lista]

		
	def Seguir():
		global posicion,posicion_antes,Posicion_en_la_lista,comenzar,cm
		comenzar=comenzar+1	
		posicion_antes=Posicion_en_la_lista
		if Posicion_en_la_lista<cm:
			Posicion_en_la_lista=Posicion_en_la_lista+1
			posicion=sopa_dividida[Posicion_en_la_lista]
			
	ct=0
	def Escanear_entorno():
		global posicion, pala_dividida
		
		if posicion == pala_dividida[ct]:
			return True
	Reiniciar()
	print(pala_dividida)
	print(sopa_dividida)
	print(ct,cz,cm)
	encontrar = False
#BUCLE_______________________________________________________________________________________

def Solucionar():
	#DEclaracion de variables de comparacion_____
	global posicion, Posicion_en_la_lista,comenzar,cm,cz

	Primer_bucle=0
	Segundo_bucle=0
	Tercer_bucle=0
	Cuarto_bucle=0
	Quinto_bucle=0
	Sexto_bucle=0
	Septimo_bucle=0
	Octavo_bucle=0
	while comenzar<cm:
		if Escanear_entorno():
			for i in range(cz):
				#Comparacion en el primer bucle, hacia delante 
				if (Posicion_en_la_lista+1)<cm:
					Posicion_en_la_lista= Posicion_en_la_lista + 1
				posicion=sopa_dividida[Posicion_en_la_lista]
				if Escanear_entorno():
					
					Primer_bucle= Primer_bucle + 1
					if Primer_bucle==cz:
						print("El primer for lo a encontrado")
						comenzar=cm
				Posicion_en_la_lista=comenzar
				#Comparacion del segundo bulce, hacia atras
				if (Posicion_en_la_lista-1)>0:
					Posicion_en_la_lista= Posicion_en_la_lista - 1
					posicion=sopa_dividida[Posicion_en_la_lista]

					if Escanear_entorno():

						Segundo_bucle= Segundo_bucle +1 
						
						if Segundo_bucle==cz:
							print("El segundo for lo a encontrado")
							comenzar=cm
	Seguir()
						







#Interfaz grafica_________________________________

class Name(FloatLayout):
	try:
		def guardar(self):
			with open("Ancho.txt", "w") as archivo:
				archivo.write(f"{self.ids.ancho.text}")
				with open("Sopa.txt", "w") as archivo:
					archivo.write(f"{self.ids.Sopa.text}")
				with open("Palabras.txt", "w") as archivo:
					archivo.write(f"{self.ids.Palabras.text}")
		def Pensar(self):
			Solucionar()
				
	except Exception as e:
	    print("Erroor : {}".format(e))

class MainApp(App):
    title = "Sopath"
    def build(self):
        return Name()
if __name__ == "__main__":
    MainApp().run()