#Catch Turtles Oyunu


import turtle
import random

pencere = turtle.Screen()
pencere.screensize(600,600)
pencere.title("Tosbağa kovalamaca")
pencere.bgcolor("blue")
pencere.tracer(2) 


oyuncu=turtle.Turtle()
oyuncu.color("red")
oyuncu.shape("triangle")
oyuncu.shapesize(3)
oyuncu.penup() 


score = 0

yaziPuan=turtle.Turtle
yaziPuan.speed(0)
yaziPuan.shape("square")
yaziPuan.color("white")
yaziPuan.penup()
yaziPuan.hideturtle()
yaziPuan.goto(-200,200)
yaziPuan.write("Puan: {}" .format(score), align="center",  font = ('Courier',24,"normal"))



speed =1 
hizPuan=turtle.Turtle
hizPuan.speed(0)
hizPuan.shape("square")
hizPuan.color("white")
hizPuan.penup()
hizPuan.hideturtle()
hizPuan.goto(200,-200)
hizPuan.write("Hız: {}" .format(score), align="center",  font = ('Courier',24,"normal"))

def solaDon():
    oyuncu.left(30)

def sagaDon():
    oyuncu.right(30)

def hiziArtir():
     global speed 
     speed=speed+1
     hizPuan.clear()
     hizPuan.write("Hız: {}" .format(score), align="center",  font = ('Courier',24,"normal"))


def hiziAzalt():
    global speed
    speed=speed-1
    hizPuan.clear()
    hizPuan.write("Hız: {}" .format(score), align="center",  font = ('Courier',24,"normal"))




pencere.listen()
pencere.onkey(solaDon,'Left')
pencere.onkey(sagaDon,'Right')
pencere.onkey(hiziArtir,'Up')
pencere.onkey(hiziAzalt,'Down') 


maxHedef= 5
hedefler =[]
for i in range (maxHedef):
    hedefler.append=turtle.Turtle()
    hedefler[i].penup()
    hedefler[i].color("purple")
    hedefler[i].shape("turtle")
    hedefler[i].speed(5)
    hedefler[i].setposition(random.randint(-300,300)),random.randint(-300,300)








while True :
    oyuncu.forward(1)

    if oyuncu.xcor() > 400 or oyuncu.xcor() < -400:
       oyuncu.right(180)
    if oyuncu.ycor() > 400 or oyuncu.ycor() < -400:
       oyuncu.right(180)
    

    for i in range (maxHedef):
        hedefler[i]. forward (1)
        if hedefler[i].xcor() > 500 or hedefler[i].xcor() <-500: 
           hedefler[i].right(random.randint(150,200))
        if hedefler[i].ycor() > 500 or hedefler[i].ycor() <-500:
           hedefler[i].right(random.randint(150,200))
            



    if oyuncu.distance(hedefler[i]) <40:
        hedefler[i].setposition(random.randint(-300,300)),random.randint(-300,300)
        hedefler[i.right(random.randint(0,360))]
        score= score + 1
        yaziPuan.clear()
        yaziPuan.write("Puan: {}" .format(score), align="center",  font = ('Courier',24,"normal"))