import turtle 
from random import randint 
import time

turtle.speed(0)
turtle.bgcolor('black')

x = 1
time.sleep(15)
while x < 300:
    r = randint(0,255) #makes variables r,g,b whose value is an integer,
    g = randint(0,255) # which is between 0 and 255. It is random, and
    b = randint(0,255) # changes every time the loop runs

    turtle.colormode(255) 
    turtle.pencolor(r,g,b) 
    turtle.fd(50 + x)
    turtle.rt(90.911)
    x = x+1 

turtle.exitonclick() 

