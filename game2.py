import sys
import pygame
import random
import time
from pygame.locals import *   #for importing keyword and mouse button presses

pygame.init()   #initializing pygame
pygame.font.init()

screen=pygame.display.set_mode((700,1010))    #Sets the dimensions of our game screen, size uses tuples, measured in terms of pixels

pygame.display.set_caption("Shoot the Pumpkin")

clock = pygame.time.Clock()
black = 0,0,0
collisionNumber = 0

pum=pygame.image.load("pum.jpg")   #loading images
shot=pygame.image.load("shot.jpg")

x=random.randint(0,700)
y=random.randint(0,700)

directionX=random.choice([-1,1])
directionY=random.choice([-1,1])

mouseX=0
mouseY=0
copyMouseY=[]
copyMouseY.append(0)
copyMouseX=[]
copyMouseX.append(0)
shotCounter=0

shotColNumber=0
counterTimer=0

points=0
pointAdder=0

pointctr=0
setFPS=150


def detectCollision(right,left,top,bottom):
	global directionX,directionY,collisionNumber

	if right>=699:
		collisionNumber = 1
		if directionX==1:
			directionX=-1
		else:
			directionX=1
	if left<=0:
		collisionNumber = 2
		if directionX==1:
			directionX=-1
		else:
			directionX=1
	if top<=0:
		collisionNumber = 3
		if directionY==1:
			directionY=-1
		else:
			directionY=1
	if bottom>=849:
		collisionNumber = 4
		if directionY==1:
			directionY=-1
		else:
			directionY=1
		
	return [collisionNumber, directionX, directionY]


def shotCollision(shotTop):
	global shotColNumber
	#if shotTop<=2:
	#	shotColNumber=1
	if shot_rect.colliderect(pum_rect)==True:  #for detecting collision between rectangles
		shotColNumber=2
	return shotColNumber


def myText(myLine,size):
	displayFont=pygame.font.SysFont("monospace",size)    #Takes up system font, (Font name, size)
	text=displayFont.render(myLine,True,(255,255,255),(0,0,0))  #Displays text, (Text, for anti-aliasing-->to remove jagged lines, colur of text, colour of text rectangle background)	
	text_rect=text.get_rect()
	return [text,text_rect]

def score(pointer):
	global pointAdder
	if pointer>=770 and pointer<850:
		pointAdder=1
	if pointer>=690 and pointer<770:
		pointAdder=2
	if pointer>=610 and pointer<690:
		pointAdder=3
	if pointer>=530 and pointer<610:
		pointAdder=4
	if pointer>=460 and pointer<530:
		pointAdder=5
	if pointer>=380 and pointer<460:
		pointAdder=6
	if pointer>=300 and pointer<380:
		pointAdder=7
	if pointer>=220 and pointer<300:
		pointAdder=8
	if pointer>130 and pointer<220:
		pointAdder=9
	if pointer<=130:
		pointAdder=10
	return pointAdder


def speed():
	setFPS=setFPS+75
	clock.tick(setFPS)   #Speed in terms of fps


while 1:
	for event in pygame.event.get():
		if event.type==pygame.QUIT or event.type==KEYDOWN and event.key==K_ESCAPE:
			sys.exit()

	screen.fill(black)

	screen.blit(pum,(x,y))    #blitting images to present it on the screen
	pum_rect = pum.get_rect()   #for image to get image rectangle
	pum_rect.move_ip(x,y)   #To move the image rectangle along with the image

	clock.tick(setFPS)

	pygame.draw.line(screen,(255,255,255),(0,850),(699,850))    #to draw a line on the screen,(colour),(start co-ordinates),(end co-ordinates)
	pygame.draw.line(screen,(255,255,255),(0,130),(699,130))    
	pygame.draw.line(screen,(255,255,255),(0,0),(0,1009))
	pygame.draw.line(screen,(255,255,255),(699,0),(699,1009))
	pygame.draw.line(screen,(255,255,255),(0,0),(699,0))
	pygame.draw.line(screen,(255,255,255),(0,1009),(699,1009))

	
	right=pum_rect.right     #The next few lines is for detecting position of object rectangle
	left=pum_rect.left
	top=pum_rect.top
	bottom=pum_rect.bottom

	
	listReturn = detectCollision(right,left,top,bottom)
	collisionNumber=listReturn[0]
	directionX=listReturn[1]
	directionY=listReturn[2]

	if collisionNumber==1:
		x-=1
		y+=directionY
	if collisionNumber==2:
		x+=1
		y+=directionY
	if collisionNumber==3:
		x+=directionX
		y+=1
	if collisionNumber==4:
		x+=directionX
		y-=1
	if collisionNumber==0:
		x+=directionX
		y+=directionY


	if event.type==MOUSEBUTTONDOWN: #and copyMouseY==0:
		mouseX,mouseY = pygame.mouse.get_pos()
		if mouseY>850:
			if copyMouseY[0]==0:
				copyMouseY[0]=mouseY
				copyMouseX[0]=mouseX
				shotCounter=1
			else:
				copyMouseX.append(mouseX)
				copyMouseY.append(mouseY)
				shotCounter+=1

	if copyMouseY[0]>0:			
		if counterTimer%2==0:
			for i in range(shotCounter):
				screen.blit(shot,(copyMouseX[i],copyMouseY[i]))
				shot_rect=shot.get_rect()
				shot_rect.move_ip(copyMouseX[i],copyMouseY[i])
				shotTop=shot_rect.top
				shotColNumber=shotCollision(shotTop)


				if shotColNumber==0:
					screen.blit(shot,(copyMouseX[i],copyMouseY[i]))
					shot_rect.move_ip(copyMouseX[i],copyMouseY[i])


				if shotColNumber==2:
					pointAdder=score(copyMouseY[i])
					points+=pointAdder
					print(i)
					copyMouseY.pop(i)
					copyMouseX.pop(i)
					#print(copyMouseY[i])
				#	copyMouseY=1
					counterTimer=0
					shotColNumber=0
					#print(points)
			
			
				if shotColNumber==1:
					copyMouseY.pop(i)
					copyMouseX.remove(i)
					counterTimer=0
			'''	
				time.sleep(1)

				listReturn2=myText("You Lost!",60)
				text=listReturn2[0]
				text_rect=listReturn2[1]

				text_rect.center=(350,505)   #adjusts the rectangle at the center
				screen.blit(text,text_rect)   #blits the text on top of the text rectangle
				pygame.display.flip()    #Flip here also because program comes to an end

				time.sleep(2)  #taken in seconds
				break
			'''
		copyMouseY=[a-1 for a in copyMouseY]
		#copyMouseY-=1			
		counterTimer+=1


	listReturn3=myText("Score: ",25)  
	bottomText=listReturn3[0]
	screen.blit(bottomText,(5,980))

	listReturn4=myText("Click to Shoot...",30)
	instructionText=listReturn4[0]
	screen.blit(instructionText,(200,920))

	pointSTR=str(points)

	listReturn5=myText(pointSTR,25)
	pointText=listReturn5[0]
	screen.blit(pointText,(100,980))

			
	pygame.display.flip()	 #To load a new screen each time during execution so that the image is displayed

	