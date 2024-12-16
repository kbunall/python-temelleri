# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
#    Ehliyet alma koşunu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

# name = input ('İsminizi giriniz: ')
# age = int(input ('Yaşınızı giriniz: '))
# egitim = input ('Eğitim durumunu giriniz: ')
# if (age>=18):
#     if(egitim.lower()=='üniversite','lise'):
#         print(f"{name} ehliyet alabilirsin.")
#     else:
#         print(f"{name} eğitim durumunuzdan dolayı ehliyet alamazsın.")
# else:
#     print(f"{name} Ehliyet alamazsın!")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not
#    aralığına karşılık gelen not bilgisini yazdırınız.
#    0-24 => 0
#    25-44 => 1
#    45-54 => 2
#    55-69 => 3
#    70-84 => 4
#    85-100 => 5

# yazılı1=int(input('1. Yazılı sınavını giriniz: '))
# yazılı2=int(input('2. Yazılı sınavını giriniz: '))
# sozlu=int(input('Sözlü sınavını giriniz: '))
# ortalama = (yazılı1+ yazılı2+sozlu)/3
# if(0<ortalama<25):
#     print('0')
# elif(25<=ortalama<45):
#     print('1')
# elif(45<=ortalama<55):
#     print('2')
# elif(55<=ortalama<70):
#     print('3')
# elif(70<=ortalama<85):
#     print('4')
# elif(85<=ortalama<=100):
#     print('5')
# else:
#     print('YANLIŞ BİLGİ GİRDİNİZ!')


# 3- trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    *** datetime modülünü kullanmanız gerekiyor.

import datetime

tarih = input ('Aracınız hangi tarihte trafiğe çıktı (yıl/ay/gün): ')

tarih=tarih.split('/')
trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days

if days<365:
    print('1. servis aralığı')
elif days>365 and days<=365*2:
    print('2. servis aralığı')
elif days<365*2 and days<365*3:
    print('3. servis aralığı')
else:
    print('hatalı süre.')