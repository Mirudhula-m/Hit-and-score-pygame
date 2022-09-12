import sys, pygame
pygame.init()   #initializing pygame

screen=pygame.display.set_mode((700,1010))    #Sets the dimensions of our game screen, size uses tuples, measured in terms of pixels

pim=pygame.image.load("pim.jpg")   #loading images
bat=pygame.image.load("bat.jpg")
pum_rect = pim.get_rect()

screen.blit(pim,(75,100))    #blitting images to present it on the screen
#screen.blit(bat,(75.100))

pygame.display.flip()     #To load a new screen each time during execution so that the image is displayed

print (pum_rect.x)

while(1):     #This is to loop the window display infinite times till the event is displayed on the screen i.e. till the cross button is clicked
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
