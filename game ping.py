# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:55:05 2020

@author: Aya S Mostafa
"""


import turtle 
#import os

wn = turtle.Screen()
wn.title("Ping pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #speed game

score_a = 0
score_b = 0

#paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260) #tall 300 pixel so it's in the up
pen.write("Player A: 0 Player B: 0", align="center", font=("monospace",22,"normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20 #move by 20 pixel
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20 #move by 20 pixel
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20 #move by 20 pixel
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20 #move by 20 pixel
    paddle_b.sety(y)
    
#keyboard buttons
wn.listen() 
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"e")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



while True:
    wn.update()
    
    
    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy*= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor()>390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}" .format(score_a, score_b),align="center", font=("monospace",22))
        ball.goto(0, 0)
        ball.dx *= -1
        
        #os.system("afplay wallhit.wav&")
        
    if (ball.xcor())< -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}" .format(score_a, score_b),align="center", font=("monospace",22))
        ball.goto(0, 0)
        ball.dx *= -1
       # os.system("afplay wallhit.wav&")
      
    #paddle and ball collisions
    if (ball.xcor() < -340) and(ball.xcor()> -350)and  (ball.ycor() < paddle_b.ycor()+40) and ball.ycor() > paddle_b.ycor() -40:
        ball.dx *= -1
        ball.setx(-340)
       # os.system("afplay wallhit.wav&")
        
    elif (ball.xcor() >340) and(ball.xcor()< 350)and  (ball.ycor() < paddle_b.ycor()+40) and ball.ycor() > paddle_b.ycor() -40:
        ball.dx *= -1
        ball.setx(340)
       # os.system("afplay wallhit.wav&")
        