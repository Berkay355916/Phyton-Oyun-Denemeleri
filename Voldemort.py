import random
import time

def Intro():
    print("Vaktiyle çok yüksek surları olan ve  Voldemort  tarafından yönetilen bir şehir devleti varmış."
          " Halk çok mutsuzmuş halk çile ve acı içinde yaşıyormuş..."
          "Ülkenin gençleri bu ülkeden kaçmak için yollar ve çareler arıyormuş."
          "Ülkeden kaçmanın tek yolu surların iki tarafında bulunan koruyucu ejderhalardan geçmekmiş.")
        

    time.sleep(3)     
    print('''Önünde iki tane yol var.
    Ejdarhalardan birisi arkadaş canlısı ve seni kurtarıp sana hazineler vermek istiyor.
    Diğer ejderha ise tam bir cani. Herkesi parçalayarak yemek istiyor''', '\n')

   
def yolusec():
    yol = ""
    yol = str(input("Hangi yolu tercih edeceksin ? Bir (1) mi ? yoksa İki (2) mi ?\nLütfen Yolu Seç "))

    return yol

def  yol(yol):
     print("Yola Doğru İlerliyorsun !!!")
     time.sleep(3)
     print("Karanlık ve Sisli Bir Hava Var ..")
     time.sleep(2)
     print("KOSKOCA Bir Ejderha Karşına Atladı\nAğzını Açtı\nSalyaları Akıyor\nVeeeeee")
     time.sleep(2)
     dogruyol = random.randint(1,2) 
     print(dogruyol)


     if yol == str(dogruyol):
        print("Kurtuldun. Ejderha Seni Kurtardı. Hazineler ve Ejderha Senin Oldu")

     else :
        print("Ejderha Bir Pençe ile Seni Yere Serdi. Parçalanarak Öldün.. ")


TekrarOyna = "evet"

while TekrarOyna == "evet" or TekrarOyna =="e":
 Intro()
 yolno = yolusec()
 yol(yolno)
 print("Tekrar Oynamak İster Misiniz ? Evet mi Hayır mı ? ")
 TekrarOyna = input("Cevabınız\n>>>>")