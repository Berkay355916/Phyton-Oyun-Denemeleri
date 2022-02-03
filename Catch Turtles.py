


import turtle #Bu oyun için Turtle ve Random kütüphanesinden yardım alıyoruz.
import random

win = turtle.Screen() #Oyunumuzun arka planını oluşturuyoruz.
win.screensize(600, 600) #Oyunumuzun ekran boyutunu giriyoruz.
win.title('Catch Turtles') #Ekran üstünde oyunun adının belirmesini sağlıyoruz.
win.bgpic("underwater.gif") #Ekranın arkasında gözükücek olan arka planımızı giriyoruz.
win.bgcolor('black')   #Ekran tonunu siyaha ayarlıyoruz.
win.tracer(2)

player = turtle.Turtle()
player.color('white')   #Oyuncumuzun imlecinin rengini veriyoruz.
player.shape('triangle') #Oyuncu imlecinin şeklini üçgen yapıyoruz.
player.shapesize(3) #Oyuncu imlecinin boyutunu belirledik.
player.penup() #Oyuncu sadece hareket edicek bunu sağlıyoruz.

score = 0

pen = turtle.Turtle()
pen.speed(0) #Puan göstergemizi oluşturuyoruz.
pen.shape("square") 
pen.color("white") #Puan göstergesinin rengini oluşturuyoruz.
pen.penup()
pen.hideturtle() #Puan göstergesini sabitleyip saklıyoruz.
pen.goto(-200, 220)
pen.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal")) #Puan göstergesindeki yazılarının puntosunu belirledik.

speed = 1

pen2 = turtle.Turtle()
pen2.speed(0) #Hız göstergemizi oluşturduk.
pen2.shape("square") #Hız göstergemizin yerini oluşturduk.
pen2.color("white") #Hız yazısı rengini beyaz yaptık.
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


def turnLeft(): #Sola dönüş açısını 30 derece olarak veriyoruz.
    player.left(30)


def turnRight():
    player.right(30) #Sağa dönüş açışını 30 derece olarak veriyoruz.


def increaseSpeed(): #Hızı arttırmak için komut veriyoruz.
    global speed  # speed fonksiyonununu globalleştiriyoruz.
    speed = speed + 1
    pen2.clear()
    pen2.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal"))


def decreaseSpeed(): #Hızı azaltmak için komut veriyoruz.
    global speed
    speed = speed - 1
    pen2.clear() #Değişen hız durumunu silip yukardaki fonksiyona göre otomatik olarak yeniliyoruz.
    pen2.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal"))


win.listen()   #Klavye komutlarını oluşturuyoruz.
win.onkey(turnLeft, 'Left') #Sola dönüşte sol yön tuşunu kullanacağız.
win.onkey(turnRight, 'Right')# Sağa dönüşte sağ yön tuşunu kullanacağız.
win.onkey(increaseSpeed, 'Up')#Hız arttırmak için yukarı yön tuşunu kullanacağız.
win.onkey(decreaseSpeed, 'Down')#Hız azaltmak için aşağı yön tuşunu kullanacağız.

while True:
    player.forward(speed)

    if player.xcor() > 300 or player.xcor() < -300: #Oyuncumuz ekranın yatay ekseninin köşelerine çarptığında sağa doğru 180 derecelik açıyla otomatik dönüş yapacak.
        player.right(180)
    if player.ycor() > 300 or player.ycor() < -300: #Oyuncumuz ekranın düşey ekseninin köşelerine çarptığında sağa doğru 180 derecelik açıyla otomatik olarak dönüş yapacak.
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


            #Turtle modülünü anlayabilmek için TokyoEdtech Kanalının videoları izlenmiştir.