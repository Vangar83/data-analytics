# turtle_race

from turtle import Turtle
from random import randint

Max = Turtle()
Max.color ('red')
Max.shape('turtle')
Max.penup()
Max.goto(-160, 100)
Max.pendown()

Marine = Turtle()
Marine.color ('blue')
Marine.shape ('turtle')
Marine.penup()
Marine.goto (-160, 80)
Marine.pendown()

Chess = Turtle()
Chess.color ('green')
Chess.shape ('turtle')
Chess.penup()
Chess.goto (-160, 60)
Chess.pendown()

for movement in range (100):
    Max.forward(randint(1,5))
    Marine.forward(randint(1,5))
    Chess.forward(randint(1,5))

input ("Press Enter to close")    
    

