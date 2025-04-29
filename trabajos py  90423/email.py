contador=0
contador2=False
elemail=input("introduce el email")
for i in elemail:
	if(i=="@"):
		contador=contador+1
	if( i=="."):
		contador2=True
if contador>1:
	print("introduce un email valido")
elif  contador==1 and contador2==True:
	print("email es valido"+ elemail)
else:
	print("introduce un email valido")
	