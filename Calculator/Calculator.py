from math import *
from time import *

def toplama(a,b):
    return a+b

def cıkarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def dıkdortgen_alan():
    firstkenar = float(input("Birinci Kenarı Yazınız "))
    secondkenar = float(input("İkinci Kenarı Yazınız"))
    dıkdortgen_alan = (firstkenar * secondkenar)
    print("Dikdörtgeninizin Alanı:",dıkdortgen_alan)

def dık_prızma_hacım():
    firstkenar = float(input("İlk Kenarı Girniz:"))
    secondkenar = float(input("İkinci Kenarı Giriniz:"))
    thirdkenar = float(input("Üçüncü Kenarı Giriniz:"))
    hacım = (firstkenar * secondkenar * thirdkenar)
    print("Prizmanızın Hacmi:",hacım)

def kare_alan():
    firstkarekenar = float(input("İlk Kenarı Giriniz:"))
    secondkarekenar = float(input("İkinci Kenarı Giriniz:"))
    kare_alan = (firstkarekenar * secondkarekenar)
    print("Karenizin Alanı:",kare_alan)
def kare_cevre():
    kenar  = float(input("Kenarı Giriniz:"))
    karenın_cevre = (kenar * 4)
    print("Karenizin Çevresi:",karenın_cevre)

def daıre_alan():
    yarıcap = float(input("Yarıçapı Giriniz:"))
    daırenın_alanı = (yarıcap * yarıcap) * pi
    print("Dairenizin Alanı:",daırenın_alanı)

def daıre_cevre():
    yarıcap = float(input("Yarıçapı Giriniz:"))
    daırenın_cevresı = ( (yarıcap * yarıcap) * 2) * pi
    print("Dairenizin Çevresi:",daırenın_cevresı)

def oklıd_yukseklık():
    oklıdfirstkenar = float(input("İlk Kenarı Giriniz:"))
    oklıdsecondkenar = float(input("İkinci Kenarı Giriniz:"))
    oklıt = (oklıdfirstkenar * oklıdsecondkenar) ** 0.5
    print("Öklid:",oklıt)

def hıpo():
    ilkkenar = float(input("İlk Kenarı Giriniz:"))
    ikincikenar = float(input("İkinci Kenarı Giriniz:"))
    hıpotenus = (ilkkenar * ilkkenar) + (ikincikenar * ikincikenar)
    print("Hipotenüs:",hıpotenus)

def ucgen_alan():
    ucgen_taban = float(input("Tabanı Giriniz:"))
    ucgen_yukseklık = float(input("Yüksekliği Giriniz:"))
    ucgenın_alanı = (ucgen_taban * ucgen_yukseklık) / 2
    print("Üçgeninizin Alanı:",ucgenın_alanı)

def ucgen_cevre():
    ucgen_ılk_kenar = float(input("İlk Kenarı Giriniz:"))
    ucgen_ıkıncı_kenar = float(input("İkinci Kenarı Giriniz:"))
    ucgen_ucuncu_kenar = float(input("Üçüncü Kenarı Girinizç:"))
    ucgenın_cevre = (ucgen_ılk_kenar + ucgen_ıkıncı_kenar + ucgen_ucuncu_kenar)
    print("Üçgeninizin Çevresi:",ucgenın_cevre)

def kup_hacım():
    kup_kenar = float(input("Kupun Kenar Değerini Giriniz"))
    kupun_hacmı = (kup_kenar * kup_kenar * kup_kenar)
    print("Küpün Hacmi:",kupun_hacmı)

def dık_yamuk_alanı():
    alt_taban = float(input("Taban Değerini Giriniz:"))
    ust_taban = float(input("Taban Değerini Giriniz:"))
    yamuk_yukseklık = float(input("Yükseklik Değerini Giriniz:"))
    yamugun_alanı = ((alt_taban + ust_taban) / 2) * yamuk_yukseklık
    print("Yamuğun Alanı:",yamugun_alanı)

def kare_alma():
    karesı_alınacak_sayı = int(input("Karesi Alınacak Sayıyı Giriniz:"))
    karesı = karesı_alınacak_sayı ** 2
    print("Girdiğiniz Sayının Karesi:",karesı)

print("""
    GELİŞMİŞ HESAP MAKİNESİ PROGRAMI 

    Gerçekleştirmek İstediğiniz İşlemi Seçiniz...
        
    1. Toplama İşlemi
    2. Çıkarma İşlemi
    3. Çarpma İşlemi
    4. Bölme İşlemi
    5. Dikdörtgen Alanı Bulma
    6. Prizma Hacmini Bulma
    7. Kare Alanı Bulma
    8. Kare Çevresi Bulma
    9. Daire Alanı Bulma
   10. Daire Çevresi Bulma
   11. Öklit Bulma
   12. Hipotenüs Bulma
   13. Üçgen Alanı Bulma
   14. Üçgen Çevresi Bulma
   15. Küp Hacmi Bulma
   16. Yamuk Alanı Bulma
   17. Bir Sayının Karesini Bulma
   18. Bir Sayının Sinüsünü Bulma
   
   Programdan Çıkmak İçin q'ya Basınız! 
""")

islem = input("İşlem Seçiniz:")
while True:
    if (islem == "q"):
        print("Programda Çıkıyorsunuz...")
        sleep(1)
        print("Program Sonlandı...")
    elif (islem == "1"):
        a = int(input("Birinci Sayı:"))
        b = int(input("İkinci Sayı:"))
        print(toplama(a,b))
        break
    elif (islem == "2"):
        a = int(input("Birinci Sayı:"))
        b = int(input("İkinci Sayı:"))
        print(cıkarma(a,b))
        continue
    elif (islem == "3"):
        a = int(input("Birinci Sayı:"))
        b = int(input("İkinci Sayı:"))
        print(carpma(a,b))
    elif (islem == "4"):
        a = int(input("Birinci Sayı:"))
        b = int(input("İkinci Sayı:"))
        print(bolme(a,b))
    elif (islem == "5"):
        dıkdortgen_alan()
    elif (islem == "6"):
        dık_prızma_hacım()
    elif (islem == "7"):
        kare_alan()
    elif (islem == "8"):
        kare_cevre()
    elif (islem == "9"):
        daıre_alan()
    elif (islem == "10"):
        daıre_cevre()
    elif(islem == "11"):
        oklıd_yukseklık()
    elif (islem == "12"):
        hıpo()
    elif (islem == "13"):
        ucgen_alan()
    elif (islem == "14"):
        ucgen_cevre()
    elif (islem == "15"):
        kup_hacım()
    elif (islem == "16"):
        dık_yamuk_alanı()
    elif (islem == "17"):
        kare_alma()
    else:
        sleep(0.8)
        print("Geçersiz İşlem Yaptınız!")
    break