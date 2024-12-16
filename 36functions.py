def sayHello (name = 'user'):
    return 'Hello'+name

msg = sayHello ('Çınar')
msg = sayHello ('Ada')

print(msg)

def total (num1,num2):
    return num1 + num2

result=total(10,20)
result=total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2019- dogumYili

ageCinar=yasHesapla(2017)
ageSena=yasHesapla(2010)
ageAda=yasHesapla(1999)

print(ageAda,ageCinar,ageSena)

def emekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: Doğum Yılı
    OUTPUT: Hesaplanan yıl bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik=65-yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('zaten emekli oldunuz')

emekliligeKacYilKaldi(1983,'Ali')
emekliligeKacYilKaldi(1950,'Ahmet')
emekliligeKacYilKaldi(1974,'Yağmur')

print(help(emekliligeKacYilKaldi))