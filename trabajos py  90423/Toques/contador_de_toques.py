import pygame , sys
from io import open
#inicamos pygame

pygame.init()

#cargamos imagenes 
imagen = pygame.image.load("png-transparent-button-ico-icon-button-miscellaneous-orange-material-thumbnail.png")
icon = pygame.image.load("png-transparent-button-ico-icon-button-miscellaneous-orange-material-thumbnail.png")
#definimos algunos colores

BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN = (0,255,0)mar 18 feb 2025 11:33:39 
RED = (255,0,0)
BLUE = (0,0,255)
#cargamos data
Data=open("Data.txt","r")
info=Data.read()
Data.close()
numero=(int(info))
#definimos tamañosmar 18 feb 2025 11:33:48 

width=500
height=600
LOCAL=(100,50)
po=width/2-50
po2=height/2-50
#creamos la ventana

PANTALLA = pygame.display.set_mode((width,height))
PANTALLA.fill(WHITE)

#nombre y icono de la PANTALLA

pygame.display.set_caption("Toques")
pygame.display.set_icon(icon)

#zona de pruebas
und = (str(numero))
imagenf = pygame.transform.scale(imagen,(100,100))
smallfont = pygame.font.SysFont('Corbel',20) 

  
text = smallfont.render(und , True , BLUE) 
#f boton:



#control de FPS

reloj = pygame.time.Clock()
#bucle principla
PANTALLA.fill(WHITE)
while True:
    #procesoss
    und = (str(numero))
    text = smallfont.render(und , True , BLACK) 
    mouse = pygame.mouse.get_pos() 
    PANTALLA.blit(imagenf,(po,po2))
    PANTALLA.blit(text,(width/2-25,height/2-25))
    def s():
        global numero
        numero+=1
	#para ver eventos 
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT:
            data=open("Data.txt","r+")
            conteo=numero
            data.write(str(conteo)) 
            sys.exit()
        #if ev.type == pygame.
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            
            
            if po <= mouse[0] <= po+100 and po2 <= mouse[1] <= po2+100: 
                s()       
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_w:
                s() 
    #pygame.draw.rect(PANTALLA,BLACK,[62,360,300,390])  
    pygame.display.update()
    reloj.tick(4)
#width/2-50,height/2-50
