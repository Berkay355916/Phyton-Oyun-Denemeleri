import random     
import time

def Intro():    #Giriş kısmında önümüze çıkacak olan yazılar için bir sınıf oluşturup print komutu ile yazılarımızı yazıyoruz.
    print("Vaktiyle çok yüksek surları olan ve  Voldemort  tarafından yönetilen bir şehir devleti varmış."
          " Halk çok mutsuzmuş halk çile ve acı içinde yaşıyormuş..."
          "Ülkenin gençleri bu ülkeden kaçmak için yollar ve çareler arıyormuş."
          "Ülkeden kaçmanın tek yolu surların iki tarafında bulunan koruyucu ejderhalardan geçmekmiş.")
        

    time.sleep(3)     #Giriş kısmında çıkıcak olan yazılardan sonra gelicek olan yazıların ekranda 3 saniyelik bekleme ile çıkması için time.sleep komutunu kullanıyoruz.
    print('''Önünde iki tane yol var.    
    Ejdarhalardan birisi arkadaş canlısı ve seni kurtarıp sana hazineler vermek istiyor.
    Diğer ejderha ise tam bir cani. Herkesi parçalayarak yemek istiyor''', '\n')    #Primt komutu ile yazılarımızı yazıyoruz.

   
def yolusec():    #Yol belirlemesi için def komutuyla bir fonksiyon atıyoruz.
    yol = ""
    yol = str(input("Hangi yolu tercih edeceksin ? Bir (1) mi ? yoksa İki (2) mi ?\nLütfen Yolu Seç ")) #Sınıf belirlemesine ihtiyaç olmadan fonksiyonu atayabilmek için str fonksiyonunu kullanıyoruz.Ve yol için şeçim yapma şansı tanıyoruz.

    return yol #Seçtiğimiz yola göre oyunumuzun devam etmesi için return komutundan yararlanıyoruz.

def  yol(yol): #Yol için def komutuyla bir sınıf,fonksiyon ataması yapıyoruz.
     print("Yola Doğru İlerliyorsun !!!")  # Print komutuyla ekranda belirecek yazımızı yazıyoruz.
     time.sleep(3)  #Ekranda belirecek yazıların ortama gerilim katması için 3 saniyelik bekleme süresi ile ekrana düşmesini sağlıyoruz.
     print("Karanlık ve Sisli Bir Hava Var ..") #Print komutuyla ekranda belirecek olan yazımızı yazıyoruz.
     time.sleep(2) #Ekranda belirecek olan yazının 2 saniyelik fark ile ekrana düşmesini sağlıyoruz.
     print("KOSKOCA Bir Ejderha Karşına Atladı\nAğzını Açtı\nSalyaları Akıyor\nVeeeeee") #Print komutuyla ekrana gelecek olan yazımızı yazıyoruz.
     time.sleep(2) #Ekrana gelecek olan yazının 2 saniyelik fark ile ekrana düşmesini sağlıyoruz.
     dogruyol = random.randint(1,2) #Doğru yolumuz için sınır belirledik randint komutu ile 
     print(dogruyol) # Doğru yol için tanımlama yapmaya başlıyoruz.


     if yol == str(dogruyol): #Eğer doğru yolu şeçmiş isek önümüze çıkıcak yazıyı belirliyoruz.Eğer kısmını kullanabilmek için if komutunu kullanıyoruz.
        print("Kurtuldun. Ejderha Seni Kurtardı. Hazineler ve Ejderha Senin Oldu") #Doğru yol sonucunda ortaya çıkacak yazımızı yazıyoruz.

     else : #Eğer yanlış yolu şeçmişsek önümüze gelicek olan şeçimini belirtiyoruz.Yolun yanlış olma durumunu belirtmek için else komutunu kullanıyoruz.
        print("Ejderha Bir Pençe ile Seni Yere Serdi. Parçalanarak Öldün.. ")#Yanlış yol sonucunda ortaya çıkacak yazımızı belirtiyoruz.


TekrarOyna = "evet" #Tekrar oynamak için kodumuzu yazıyoruz.

while TekrarOyna == "evet" or TekrarOyna =="e": #Tekrar oynamak istersek yapmamız gerekenleri belirtiyoruz.
 Intro()
 yolno = yolusec()
 yol(yolno)                                                          #Oyunu tekrar oynamak için gerekli komutları girdik.Oyun bittiğinde önümüze çıkacak olan ekranın şablonunu belirledik.
 print("Tekrar Oynamak İster Misiniz ? Evet mi Hayır mı ? ")
 TekrarOyna = input("Cevabınız\n>>>>")