import datetime
birthday = datetime.datetime(1990,10,17,12,45,0)
from dateutil.relativedelta import *
from datetime import date
import time
import pygame
import sys
def privet():
    error = pygame.init()
    if error[1] == 0:
        print("Hello! This will show your exact age.")
    else:
        print("Errors detected!")
        sys.exit()
privet()
window = pygame.display.set_mode((1280,100))
pygame.display.set_caption('Используй каждую секунду'.rjust(180, ' '))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
i = 1
window.fill(white)


escape = False

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			escape = True
			pygame.quit()
        
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_ESCAPE:
				escape = True	
	today = datetime.datetime.now()
	dob = datetime.datetime(1990, 10, 17,12,45,0)
	age = relativedelta(today, dob)
	text = pygame.font.SysFont('Segoe Script', 36)
	rend = text.render(str(age.years)+' лет '+str(age.months)+
		' месяцев '+str(age.days)+' дней '+str(age.hours)+
		' часов '+str(age.minutes)+' минут '+str(age.seconds) + 
		' секунд', True, white)
	gaORectangular = rend.get_rect()
	gaORectangular.midtop = (640, 25)
	window.fill(black)
	window.blit(rend,gaORectangular)
	i+=1
	#window.blit(screen,(0,0))
	pygame.display.flip()
	if escape:
		pygame.quit()
    
	time.sleep(1)
