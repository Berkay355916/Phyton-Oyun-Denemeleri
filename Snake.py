#Snake Adlı Oyun Başlangıcı

import random
import turtle  #Oyun modülleri için kütüphanelerimizi ekliyoruz
import time
delay = 0.16 # Gecikme süresini Bursada yaşadığımız için plakamız olarak veriyoruz :)
 
pencere = turtle.Screen()
pencere.title('Snake') #Ekran Başlığı olarak oyun adını veriyoruz.
pencere.bgcolor('lime') #Ekran rengini misket limonu yeşili yapıyoruz.
pencere.setup(width=600, height=600) #Ekran büyüklüğünü ayarlıyoruz
pencere.tracer(0) #Pencere güncellemesini engelliyoruz.Güncellemeyi ilerleyen kodlarda yapacağız.
 
kafa = turtle.Turtle() #Yılanımızın kafasını oluşturuyoruz
kafa.speed(0) #Kafanın başlangıç hızını 0 veriyoruz.İlk hareketi biz vereceğiz.
kafa.shape("square") #Kafamızın şeklini kare olarak belirledik.
kafa.color("cyan") #Kafamızın rengini cyan olarak belirledik.
kafa.penup() #Kafa hareket ederken herhangi bir yazı çıkmayacağı için penup modülünü kullanıyoruz.
kafa.goto(0, 90) 
kafa.direction = "stop" #ilk hareketimiz durağan olacak.Bunu kodladık
 
yemek = turtle.Turtle()
yemek.speed(0) #Yemimizin ilk hızını 0 olarak belirledik.
yemek.shape("triangle") #Yemimizin şeklini üçgen olarak belirledik.
yemek.color("purple") #Yemimizin rengini mor yaptık
yemek.penup()
yemek.shapesize(0.60, 0.60)#Yemimizin boyutunu 0.60 a 0.60 olarak belirledik fazla büyük olmasını istemiyoruz.
yemek.goto(0, 0) # Yemimizin ilk konumu orijin olarak belirledik.
 
kuyruklar = [] #Kuyruk için bir liste oluşturduk.
puan = 0
 
yaz = turtle.Turtle()  #Puan göstergemizi belirliyoruz.
yaz.speed(0)
yaz.shape("square") 
yaz.color("white") #Rengi beyaz olarak şeçtik
yaz.penup() 
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal")) 
 
def move():
    if kafa.direction == "up": #Kafamızın yukarı doğru hareketi için gerekli kodlarımızı yazıyoruz
        y = kafa.ycor()
        kafa.sety(y + 20) #Önceki koordinatın 20 piksel fazlasına doğru bir hareket oluşturuyoruz.
    if kafa.direction == "down":
        y = kafa.ycor() #Önceki koordinatın 20 aşağısını yazıyoruz eğer aşağı yönlü bir hareketimiz olacaksa
        kafa.sety(y - 20)
    if kafa.direction == "right": #Sağa hareket için gerekli komutları veriyoruz.
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left": #Sola hareket için gerekli komutları veriyoruz.
        x = kafa.xcor()
        kafa.setx(x - 20)
 
def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"
def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"
 
 
 
 
 
def go_right(): #Sağa hareket için klavye ile yapabilceğimiz iki şeçeneği veriyoruz.Sağ ve sol yön tuşları ile hareket sağlayabiliriz.
    if kafa.direction != "left":
        kafa.direction = "right"
def go_left():   #Sola hareket için ya sola devam ya da sağa doğru geçiş için klavye tuşlarımızı tanımlıyoruz.
    if kafa.direction != "right":
        kafa.direction = "left"
 
pencere.listen()
pencere.onkey(go_up, "Up") #Yukarı hareket için yukarı yön tuşu.
pencere.onkey(go_down, "Down")#Aşağı hareket için aşağı yön tuşu.
pencere.onkey(go_right, "Right")#Sağa hareket için sağ yön tuşu.
pencere.onkey(go_left, "Left") #Sola hareket için sol yön tuşu.
 
while True:
    pencere.update()
 
    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300: #Kafamızın kenarlara çarptığında oyunun sonlanabilmesi için gerekli olan komutlarımızı yazıyoruz.
        time.sleep(2) #Eğer kenara çarpar isek 2 saniyelik bekleme sonucunda yılanımızın kafası yine başlangıç noktasına gönderiyoruz.
        kafa.goto(0, 0)
        kafa.direction = "stop"
 
        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []
 
        puan = 0
        delay = 0.16 # Gecikme süremiz Bursa plakasından devam etmekte :)
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
    if kafa.distance(yemek) < 20: #Yılanımızın başı yemin önüne geldiğinde yemi yiyip yemin rastgele yer değiştirmesi için sınırlayıcı bileşen olarak randint komutundan yardım alıyoruz.
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)
 
        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)#Kuyruğumuzun ilk hızı 0
        yeni_kuyruk.shape("square")#Kuyruğumuzun şekli kare olarak belirledik.
        yeni_kuyruk.color("white")#Rengi beyaz olarak şeçtik
        yeni_kuyruk.penup()#Kuyruğumuz hareket etmeyecek ve arkasından herhangi bir yazı vb.çıkmayacak.
        kuyruklar.append(yeni_kuyruk)
 
        delay -= 0.0016
 
        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
    for index in range(len(kuyruklar) - 1, 0, -1): #Kuyruk listemizi geliştiriyoruz.
        x = kuyruklar[index - 1].xcor() #Kuyruğun hareket etmesi ve kuyruğun değişebilmesi için gerekli komutları yazıyoruz.
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y) #Kuyruğumuzun hareket doğrultusunu belirliyor ve ona göre yavaştan mesafe kısımlarını incelemeye başlıyoruz.
 
    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)
 
    move()
 
    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.5
 
    time.sleep(delay)