import fix
import turtle
import random
from time import sleep
from datetime import datetime as dt
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('bouncing ball simulator')
wn.tracer(0)


balls = []
for i in range(20):
	balls.append(turtle.Turtle())
for ball in balls:
	ball.shape(random.choice(['circle','square','triangle']))
	colour = '#' 
	for i in random.choices('1234567890abcdef',k=6):
		colour+=i
	ball.color(colour)

	ball.penup()
	ball.speed(0)
	x=random.randint(-290,290)
	y=random.randint(200,400)
	ball.goto(x, y)
	ball.dy = 0
	ball.dx = random.randint(-3,3)
	ball.da = 2


gravity=0.1
def slowmo():
	global time
	b = dt.now()

	if (b - a).seconds > 5 and (b - a).seconds < 15 :
		time += 0.02
	else:
		while time > 0.005:
			time -= 0.02	
a = dt.now()

while 1:
	wn.update()
	for ball in balls:
		ball.rt(ball.da)
		ball.dy -= gravity
		ball.sety(ball.ycor() + ball.dy)
		ball.setx(ball.xcor() + ball.dx)
		#проверка столкновений со стенами
		if ball.xcor() > 300:
			ball.dx *= -1
			ball.da *= -1
		if ball.xcor() < -300:
			ball.dx *= -1
			ball.da *= -1
		#проверка столкновений с полом
		if ball.ycor() < -300:
			ball.sety(-300)
			ball.dy *= -1
			ball.da *= -1
		
	time = 0.005
	slowmo()
	sleep(time)