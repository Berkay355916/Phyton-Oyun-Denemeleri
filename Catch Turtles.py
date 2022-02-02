


import turtle
import random

win = turtle.Screen()
win.screensize(600, 600)
win.title('Catch Turtles')
win.bgpic("underwater.gif")
win.bgcolor('black')
win.tracer(2)

player = turtle.Turtle()
player.color('white')
player.shape('triangle')
player.shapesize(3)
player.penup()

score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-200, 220)
pen.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))

speed = 1

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(200, 220)
pen2.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal"))

maxGoals = 5
goals = []
for i in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[i].penup()
    goals[i].color('yellow')
    goals[i].shape('turtle')
    goals[i].speed(0)
    goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))


def turnLeft():
    player.left(30)


def turnRight():
    player.right(30)


def increaseSpeed():
    global speed
    speed = speed + 1
    pen2.clear()
    pen2.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal"))


def decreaseSpeed():
    global speed
    speed = speed - 1
    pen2.clear()
    pen2.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal"))


win.listen()
win.onkey(turnLeft, 'Left')
win.onkey(turnRight, 'Right')
win.onkey(increaseSpeed, 'Up')
win.onkey(decreaseSpeed, 'Down')

while True:
    player.forward(speed)

    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    for i in range(maxGoals):
        goals[i].forward(1)

        if goals[i].xcor() > 500 or goals[i].xcor() < -500:
            goals[i].right(random.randrange(150, 250))
        if goals[i].ycor() > 500 or goals[i].ycor() < -500:
            goals[i].right(random.randrange(150, 250))

        if player.distance(goals[i]) < 40:
            goals[i].setposition(random.randint(-290, 290), random.randint(-290, 290))
            goals[i].right(random.randint(0, 360))
            score = score + 1
            pen.clear()
            pen.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))