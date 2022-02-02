#ARABUL SAYI TAHMİN ETME OYUNU 
# Leveller ->  KOLAY ORTA ZOR İMKANSIZ

from pickle import TRUE
import random

alt_sinir = 1

ust_sinir = int(input("Üst Sınırı Giriniz => "))

sayi=random.randint(alt_sinir, ust_sinir)

oyun_devam_ediyor_mu = True
while oyun_devam_ediyor_mu:
      tahmin=input("Tahminin nedir ? ")

      if tahmin.isdigit():
         tahmin= int(tahmin) 


         if tahmin == sayi:
            print("Tebrikler,Sayıyı Buldun")
            oyun_devam_ediyor_mu == False
         elif tahmin < sayi :
            print("Girdiğin Sayı Tuttuğum Sayıdan Küçük.Daha Yükseklere Uçmalısın.")
         else:
            print("Girdiğin Sayı Tuttuğum Sayıdan Büyük.Küçük Düşünmelisin.")
        
      else:
          if tahmin == "pes":
            print("Demek Pes Ediyorsun! Tuttuğum sayı :", sayi)
            oyun_devam_ediyor_mu = False
          else:
            print("Dostum Böyle Bir Komut Yok Tekrar Dene")
          
        
         

        