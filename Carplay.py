#CARPLAY ARABA YARIŞI OYUNU

import random
from turtle import st
from typing_extensions import Self

class Yaris:
    def __init__(self,Marka,Kalanbenzin,YakıtTüketimi,MaksimumHiz):
      self.Marka = Marka  
      self.KalanBenzin = Kalanbenzin
      self.MaksimumHiz = MaksimumHiz
      self.YakıtTüketimi = YakıtTüketimi

#Bu fonksiyonla nesnemizin özelliklerini ekrana yazdırıyoruz.

    def print(self):
        print("Marka  :",self.Marka,"\nKalan Benzin : ",self.KalanBenzin,"It \nMaksimumHiz  :" ,
        self MaksimumHiz,"km\h","\nYakıtTüketimi  :",self.YakıtTüketimi,"It")

#Bu fonksiyonla ana detaylar belirleniyor

    def yaris(self):
        Yol = 100
        print(self.Marka +"Piste Cikti.\nBugun Yarısagi Pist"+ Yol +"km uzunlugunda \nVE YARIISS BASLİYORR")

        self.sure =(int(Yol)/(self.MaksimumHiz)*60)
        self.sure = round(self.sure,2)

        print (str(self.Marka) "Yarisi " + str(self.MaksimumHiz) +" km\h hiz ile giderek Yarisi" +  str(self.sure) + "dakikada tamamladi...")

        harcananYakit =((int(Yol/100*int(self.YakıtTüketimi))))
        self.KalanBenzin = (int(self.KalanBenzin)-harcananYakit)

        print("Yarış sonunda depoda Kalan benzin"+ str(self.KalanBenzin) + "It")

        return self.KalanBenzin, self.sure


    def BenzinBittiMi (Self):
        if Self.KalanBenzin <=0:
          print ("Benzin Bitti")

          return False

        else:
          return True  

    def tablo(self):
        print(self.Marka +"-"*12 + str(self.sure)+"dakika"+ "-"*5)+str(self.KalanBenzin) + "It"

        arabalar = []

        i=0
        while(i<9):
            RandomYakit = random.randrange(40,70)
            RandomHiz = random.randrange(250,300)
            RandomTüketim = random.randrange(15,25)
            markalar = ("Ferrari    ","Lotus     ","Bmw       ","Aston Martin  ","Porsche   ","Tesla    ",
                        "Mclaren   ","Bugatti   ", "Tofaş    ","Mercedes ")
                            
            word =random.choice(markalar)
            yeniyarisci = Yaris (word+ str(i+1),RandomYakit,RandomYakit,RandomTüketim)
            arabalar.append(yeniyarisci)
            i+=1


        for i in arabalar:
            i.print()
            print("-"*20)+"\n"+ ("*"*20)
            i.yaris()
            i.BenzinBittiMi()
            print(("-"*20)+"\n"+ ("*"*20))
            i.print



        print("Yarisci        "+(" "*10))+ "Tur Suresi" + (" "*5)+"Kalan Yakit"
        
        for i in arabalar:
            i.tablo()

