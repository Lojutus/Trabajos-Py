import pygame, sys
pygame.init()
# Definir 
BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
W,H=1000,600
#Crear ventana
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("PRACTICA")
#fondo
fondo=pygame.image.load("c.jpg")
fondo_redimencionado = pygame.transform.scale(fondo,(W,H))
x=0
#
icono=pygame.image.load("images.png")
pygame.display.set_icon(icono)
#Controlar FPS
clock = pygame.time.Clock()
#Velocidad a la que se movera el cuadrado
speed_x = 3
speed_y = 3
#bucle principal
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.blit(fondo_redimencionado,(0,0))
	x_r= x % fondo_redimencionado.get_rect().width
	screen.blit(fondo_redimencionado,(x_r-fondo_redimencionado.get_rect().width,0))
	if x_r< W:
		screen.blit(fondo_redimencionado,(x_r,0))
	x-=1
	#Zona de dibujo
	#Zona de dibujo
	#Actualizar pantalla
	pygame.display.flip()
	clock.tick(700)