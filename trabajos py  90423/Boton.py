import pygame.font 

class boton():
	def __init__(texto,width,height,imagen,d,tcolor,Ttamano):
		smallfont = pygame.font.SysFont('Corbel',35) 
  
		text = smallfont.render('quit' , True , tcolor)
		PANTALLA.blit(text ,(width/2+50,height/2)) 
	
		#imga = pygame.blit(imagen,d,(width,height))
		#imga = img2.pygame.blit(text,d+50,Ttamano)
