#ARABUL SAYI TAHMİN ETME OYUNU 
# Leveller ->  KOLAY ORTA ZOR İMKANSIZ

from pickle import TRUE
import random #Rastgele şeçim yapabilmek için  bir kütüphane belirliyoruz.

alt_sinir = 1  #Alt sınırımızı belirliyoruz.

ust_sinir = int(input("Üst Sınırı Giriniz => ")) #Üst sınırı belirlerken leveller ve isteğe göre bir üst sınır belirlenebilmesi için int(input) komutundan yardım alıyoruz.

sayi=random.randint(alt_sinir, ust_sinir) #Alt ve üst sınır arasında rastgele bir tam sayı şeçimi için random kütüphanesindeki randint komutundan yardım alıyoruz.

oyun_devam_ediyor_mu = True  #Oyunun devamının doğruluğunu kontrol edip oyun kodlarını yazmaya devam ediyoruz.Üst sınırı oyuncu belirleyeceğinden dolayı for komutunu kullanmıyoruz.
while oyun_devam_ediyor_mu:  #Döngü başlatmak için while komutunu kullanıyoruz.
      tahmin=input("Tahminin nedir ? ") #Programı tek taraflı olmaktan kurtarmak ve oyun ekranının başında yazının gerekmesi için komutumuzu işliyoruz.

      if tahmin.isdigit(): #Girilen input sayılardan mı oluşuyor yoksa harflerden mi oluşuyor onu belirlemek için isdigit komutunu kullanıyoruz.
         tahmin= int(tahmin) 


         if tahmin == sayi: #Eğer tahminimiz doğruysa bunu belirtmek için if komutunu kullanıyoruz.
            print("Tebrikler,Sayıyı Buldun") #Tahmimizin doğru olmasından sonra ekranda ortaya çıkacak yazımızı belirliyoruz ve print komutuyla işlemi tamamlıyoruz.
            oyun_devam_ediyor_mu == False #Tahmin doğru olduğundan dolayı oyun sonlanmıştır. Bu durumdan kaynaklı olarak artık True değil False bildirgesini kullanıyoruz.
         elif tahmin < sayi : #Eğer tahminimiz yanlışssa ve yazdığımız sayı tahminden küçükse olucak durumları belirtiyoruz.
            print("Girdiğin Sayı Tuttuğum Sayıdan Küçük.Daha Yükseklere Uçmalısın.") #Tahminimiz küçükse ortaya çıkacak olan yazımızı yazıyoruz.
         else: 
            print("Girdiğin Sayı Tuttuğum Sayıdan Büyük.Küçük Düşünmelisin.") #Eğer tahminimiz yanlış ve tuttuğumuz sayıdan daha büyükse ortaya çıkıcak durumları belirtiyoruz.
        
      else:
          if tahmin == "pes": #Eğer Arabul Robotunun tuttuğu sayıyı bulamıyor ve pes etmek istiyorsanız oyunu sonlandırmak için gerekli olan pes yazısını oyunumuz içerisine işliyoruz.
            print("Demek Pes Ediyorsun! Tuttuğum sayı :", sayi) #Pes ettiğimizde ekrana belirecek olan yazıyı gösteriyor ve arabul robotunun tahmin etmiş olduğu sayıyı ekranda gösteriyoruz.
            oyun_devam_ediyor_mu = False #Oyunun sonlandığını gösteriyoruz.
          else: #Oyun devam eder ve oyunda olmayan herhangi bir komut girildiğinde oluşabilecek sorunları önlemek için bu komutun hatalı olduğunu gösterip tekrardan oyunun başlamasını sağlıyoruz.
            print("Dostum Böyle Bir Komut Yok Tekrar Dene")
          
        
         

        