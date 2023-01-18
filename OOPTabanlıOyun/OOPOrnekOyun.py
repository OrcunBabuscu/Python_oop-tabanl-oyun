import time,sys,random
#projemde kullandığım kütüphaneleri import ettim#
def hatalı_eksik():
    print("!Eksik ya da Hatalı Tuşlama!")
    #kullanıcı hatalı giriş yaparsa diye uyarı döndürdüm#

def nokta_ekle():
    print(".")
    time.sleep(.3)
    print("..")
    time.sleep(.3)
    print("...")
    time.sleep(.3)
    #Buradaki fonksiyonum 2 savaş arasındaki boşluk güzel gözüksün diye başlangılangıca  nokta ekledim#

class Oyuncu():
    def __init__(self,isim,can=10,power=100,puan=0):
        self.isim = isim
        self.can = can
        self.power = power
        self.puan = puan
#can , power ve puana default değerler atadım#
    def bilgileri_goster(self):
        print("""
        
        İsim: {}
        Can: {}
        Güç: {}
        Puan: {}
        """.format(self.isim,self.can,self.power,self.puan))
# oyuncu classında oluşturduğum bilgileri görebilmek için bu fonksiyonu oluşturdum #

    def saldir(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            print("Saldırı Başladı...")
            nokta_ekle()
            print("Saldırı Başarılı")
            self.power -= 8
            self.puan += 10
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
#saldırı başarılı olursa eğer kullanıcının gücünü 8 düşürdüm , puanı 10 arttı ve düşmanın canı 1 azaldı#
        else:
            print("Saldırı Başladı...")
            nokta_ekle()
            print("Saldırı Başarısız")
            self.power -= 8
            self.can -= 1
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
 #saldırı eğer başarısız olursa düşmana 10 puan ekledim ama kullanıcının canını ve gücünü azalttım#

    def savun(self,dusman):
        sonuc = self.saldir_savun_sayi()
        if (sonuc == 1):
            print("Savunma Başladı...")
            nokta_ekle()
            print("Savunma Başarılı")
            dusman.power -= 8
            self.puan += 10
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
    #savunmada ise kazanılırsa eğer düşmanın gücü 8 azaldı , kullanıcı puamı 10 arttı ve düşman canını 1 azalttım#
        else:
            print("Savunma Başladı...")
            nokta_ekle()
            print("Savunma Başarısız")
            dusman.power -= 8
            self.can -= 1
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()

  # savunmad kaybedilirse eğer düşmanın gücü 8 azaldı , düşman puamı 10 arttı ve kullanıcı canınını 1 azalttım#
    def saldir_savun_sayi(self):
        return random.randint(1,2)
#Buradan çıkan değere göre saldır yada savun seçeneği seçiliyor#
    def exit(self):
        print("Oyun Kapatılıyor...")
        nokta_ekle()
        sys.exit()
        #oyunumu sonlandırdım#

oyuncu1 = Oyuncu("Orçun")
oyuncu2 = Oyuncu("ASLI")
#Oyuncu isimlerimi tanımladım#
print("Oyun Başlatılıyor...")
nokta_ekle()

while True:
    hamle = input("""
    1-Saldır
    2-Savun
    3-Çık
    Hamle Seçimi:
    """)

    if(hamle=="1"):
        oyuncu1.saldir(oyuncu2)
    elif(hamle=="2"):
        oyuncu1.savun(oyuncu2)
    elif(hamle=="3"):
        oyuncu1.exit()
    else:
        hatalı_eksik()
#Kullanıcıdan hamlemi istedim ve 3 hamleden 1 ini seçmezse hata döndürdüm#
    if(oyuncu1.puan==100 or oyuncu2.can==0 or oyuncu2.power<=0):
        print("Oyunun Kazananı:", oyuncu1.isim)
        #oyuncu 2 nin gücü 0 ın altına indiğinde kazananı oyuncu 1 ilan ettim#
        break
    if(oyuncu2.puan==100 or oyuncu1.can==0 or oyuncu1.power<=0):
        print("Oyunun Kazananı:", oyuncu2.isim)
        # oyuncu 1 in gücü 0 ın altına indiğinde kazananı oyuncu 2 ilan ettim#
        break



