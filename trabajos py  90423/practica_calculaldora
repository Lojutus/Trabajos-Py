from tkinter import *
r=Tk()
r.title("CALCULADORA CHAFA")
r.resizable(0,0)
f=Frame(r)
rst=0
operacion=""
operacion2=""
f.pack()
f.config(bg="white",width=500, height=500)
#_____________________pantalla:O__________________________________________________________________
numerop=StringVar()
numerop.set("")
pantalla=Entry(f,textvariable=numerop)
pantalla.grid(row=1, column=1, padx=5, pady=5,columnspan=4)
pantalla.config(background="white", fg="black")
#_____________________pantalla2:o______________________________________________________________________
numerop2=StringVar()
pantalla2=Entry(f,textvariable=numerop2)
lore=Label(f,text="RESULT")
lore.grid(row=1, column=5, padx=5, pady=5,columnspan=4)
pantalla2.grid(row=2, column=5, padx=5, pady=5,columnspan=4)
#___________________FUNCIONES L)_____________________________________________________________________
def registro():
	global rst
	global operacion2
	global restat
	while
	if operacion2=="suma":
		numerop2.set(rst+int(numerop.get()))
	elif operacion2=="resta":
		numerop2.set(rst-int(numerop.get()))
	elif operacion2=="mult":
		numerop2.set(rst*int(numerop.get()))
	else:
		numerop2.set("error")

def numeros(num):
	global operacion
	if operacion!="":
		numerop.set(num)
		operacion=""




	else:
		numerop.set(numerop.get() + num)
			
def borrar():
	global rst
	numerop2.set("")
	rst=0
	numerop.set("")

#suma
def suma(num):
	global operacion
	global operacion2
	global rst
	operacion="suma"
	operacion2="suma"

	rst+=int(num)
#resta
def resta(num):
	global operacion
	global rst
	rst-=int(num)
	operacion="resta"
	operacion2="resta"
def mult(num):
	global operacion
	global rst
	rst-=int(num)
	operacion="mult"
	operacion2="mult"


#_____________________botones_____________________________________________________________________
#_____________________boton linea 1________
boton7=Button(f, text="7",width=3,padx=3, pady=3, command=lambda:numeros("7"))
boton7.grid(row=2, column=1)
boton9=Button(f, text="9",width=3,padx=3, pady=3,command=lambda:numeros("9"))
boton9.grid(row=2, column=3)
boton8=Button(f, text="8",width=3,padx=3, pady=3,command=lambda:numeros("8"))
boton8.grid(row=2, column=2)
botonmas=Button(f, text="+",width=3,padx=3, pady=3,command=lambda:suma(numerop.get()))
botonmas.grid(row=2, column=4)


#_____________________boton linea 2________


boton4=Button(f, text="4",width=3,padx=3, pady=3,command=lambda:numeros("4"))
boton4.grid(row=3, column=1)
boton5=Button(f, text="5",width=3,padx=3, pady=3,command=lambda:numeros("5"))

boton5.grid(row=3, column=3)
boton0=Button(f, text="0",width=3,padx=3, pady=3,command=lambda:numeros("0"))
boton0.grid(row=3, column=5)
boton6=Button(f, text="6",width=3,padx=3, pady=3,command=lambda:numeros("6"))
boton6.grid(row=3, column=2)
botonmen=Button(f, text="-",width=3,padx=3, pady=3,command=lambda:resta(numerop.get()))
botonmen.grid(row=3, column=4)
#_____________________boton linea 3________


boton1=Button(f, text="1",width=3,padx=3, pady=3,command=lambda:numeros("1"))
boton1.grid(row=4, column=1)
boton2=Button(f, text="2",width=3,padx=3, pady=3,command=lambda:numeros("2"))
boton2.grid(row=4, column=2)
boton3=Button(f, text="3",width=3,padx=3, pady=3,command=lambda:numeros("3"))
boton3.grid(row=4, column=3)
botonpor=Button(f, text="*",width=3,padx=3, pady=3,command=lambda:mult(numerop.get()))
botonpor.grid(row=4, column=4)
#_____________________especiales linea 4________________
borrarc=Button(f, text="CE", width=3, padx=3, pady=3,command=lambda:borrar())
borrarc.grid(row=5, column=1)
borrarp=Button(f,text="C",width=3,padx=3, pady=3)
borrarp.grid(row=5, column=2)
igual=Button(f,text="=",width=8,padx=3, pady=3,command=lambda:registro())
igual.grid(row=5, column=3,columnspan=2)



















r.mainloop()

