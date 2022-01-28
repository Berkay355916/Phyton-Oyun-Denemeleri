#CARPLAY ARABA YARIŞI OYUNU

import random

class Yaris:
    def __init__(self,Marka,Kalanbenzin,YakıtTüketimi,MaksimumHiz):
      self.Marka = Marka  
      self.KalanBenzin = Kalanbenzin
      self.MaksimumHiz = MaksimumHiz
      self.YakıtTüketimi = YakıtTüketimi

#Bu fonksiyonla nesnemizin özelliklerini ekrana yazdırıyoruz.

    def print(self):
        print("Marka  :",self.Marka,"\nKalan Benzin : ",self.KalanBenzin,"It \nMaksimumHiz  :",
        self MaksimumHiz,"km\h","\nYakıtTüketimi  :",self.YakıtTüketimi,"It")

#Bu fonksiyonla ana detaylar belirleniyor

    def yaris(self):
        Yol = 100
        print(self.Marka +"Piste Cikti.\nBugun Yarısagi Pist"+ Yol +"km uzunlugunda \nVE YARIISS BASLİYORR")

        self.sure =((Yol)/(self.MaksimumHiz)*60)
        self.sure = round(self.sure,2)

        print(self.Marka "Yarisi   " + self.MaksimumHiz +"km\h hiz ile giderek Yarisi" + self.sure + "dakikada tamamladi...")

        harcananYakit =((int(Yol/100*int(self.YakıtTüketimi))))