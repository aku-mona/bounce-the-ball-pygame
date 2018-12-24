import pygame
import random 
pygame.init()
width=500
height=500
Green=(0,255,0)
Red=(255,0,0)
black=(0,0,0)
screen=pygame.display.set_mode([width,height])
pygame.display.set_caption("bounce the ball")
bg=pygame.image.load("scene.jpg")
st=pygame.image.load("santa.png")
dx=1
dy=2
y=height-21
x1=100
y1=200
dx1=1
dy1=3
lead_x=200
x=lead_x+20
run=True
hit=pygame.mixer.Sound('hit.wav')
mus=pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play(-1)
num1=random.randint(1,490)
num2=random.randint(1,490)
num3=random.randint(1,490)
num4=random.randint(1,490)
num5=random.randint(1,490)
num6=random.randint(1,490)
num10=random.randint(1,490)
num12=random.randint(1,490)
num11=random.randint(1,490)
num9=random.randint(1,490)
num8=random.randint(1,490)
num7=random.randint(1,490)
n1=num1
n2=num2
dy2=0
h=40
while run:
	#screen.fill(black)
	screen.blit(bg,(0,0))
	x=x+dx
	y=y+dy
	x1=x1+dx1
	y1=y1+dy1
	n2=n2+dy2
	pygame.draw.circle(screen,Green,[x,y],10)
	pygame.draw.circle(screen,Red,[x1,y1],10)
	screen.blit(st,(n1+10,n2-20))
	pygame.draw.rect(screen,black,[num1,num2,30,10])
	pygame.draw.rect(screen,black,[num3,num4,30,10])
	pygame.draw.rect(screen,black,[num5,num6,30,10])
	pygame.draw.rect(screen,black,[num7,num8,30,10])
	pygame.draw.rect(screen,black,[num9,num10,30,10])
	pygame.draw.rect(screen,black,[num11,num12,30,10])
	
	
	if x>width-10 or x<0:
		dx*=-1
	if y<0:
		dy*=-1
	if x1>width-10 or x1<0:
		dx1*=-1
	if y1<0 :
		dy1*=-1
	for event in pygame.event.get():
		
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				if lead_x>0:
					lead_x-=10
			if event.key==pygame.K_RIGHT:
				if lead_x<=width-40:
					lead_x+=10
				
	if x+10>=lead_x and x-10<=lead_x+h and y+10>490 and y+10<500:
		dy*=-1
	if x1+10>=lead_x and x1-10<=lead_x+h and y1+10>490 and y1+10<500:
		dy1*=-1
#	for xcor1 in (lead_x,lead_x+40):
#		for x3 in (x1-10,x1+10):
#			if x3==xcor1 and y1+10>=490 and y1+10<=500:
		#		dy1*=-1
			
			#if x+10==xcor and y==ycor:
			#	print('hhh')
			#	dy*=-1
	if x+10>=num1 and x-10<=num1+30 and y+10>num2 and y+10<num2+10:
		hit.play()
		pygame.draw.rect(screen,black,[num1-10,num2+10,10,10])
		pygame.draw.rect(screen,black,[num1+30,num2+10,10,10])
		num1=600
		num2=600
		dy2=5
			
	if x+10>=num3 and x-10<=num3+30 and y+10>num4 and y+10<num4+10:
		hit.play()
		pygame.draw.rect(screen,black,[num3-10,num4+10,10,10])
		pygame.draw.rect(screen,black,[num3+30,num4+10,10,10])
		num3=700
		num4=700
	if x+10>=num5 and x-10<=num5+30 and y+10>num6 and y+10<num6+10:
		hit.play()
		pygame.draw.rect(screen,black,[num5-10,num6+10,10,10])
		pygame.draw.rect(screen,black,[num5+30,num6+10,10,10])
		num5=800
		num6=800
	if x+10>=num7 and x-10<=num7+30 and y+10>num8 and y+10<num8+10:
		hit.play()
		pygame.draw.rect(screen,black,[num7-10,num8+10,10,10])
		pygame.draw.rect(screen,black,[num7+30,num8+10,10,10])
		num7=900
		num8=900
	if x+10>=num9 and x-10<=num9+30 and y+10>num10 and y+10<num10+10:
		hit.play()
		pygame.draw.rect(screen,black,[num9-10,num10+10,10,10])
		pygame.draw.rect(screen,black,[num9+30,num10+10,10,10])
		num9=950
		num10=950
	if x+10>=num11 and x-10<=num11+30 and y+10>num12 and y+10<num12+10:
		hit.play()
		pygame.draw.rect(screen,black,[num11-10,num12+10,10,10])
		pygame.draw.rect(screen,black,[num11+30,num12+10,10,10])
		num11=1000
		num12=1000
	if n2>=490 and n2<=500:
		h=h+20
	if y>500:
		screen.blit(bg,(0,0))
		
	pygame.draw.rect(screen,Green,[lead_x,height-10,h,10])
	pygame.display.flip()		
	pygame.time.Clock().tick(180)
	
pygame.quit()

