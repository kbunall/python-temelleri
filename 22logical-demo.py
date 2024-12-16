# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# x=int(input('Bir sayı giriniz: '))
# result=0<x<100
# print(f"Girilen sayı 0-100 arasında mıdır: {result}")


# 2- Girilen bir sayının pozirif çift sayı olup olmadığını kontrol ediniz.
# x=int(input('Bir sayı giriniz: '))
# result=(x>0) and (x%2==0)
# print(f"Girilen pozitif ve çift bir sayıdır: {result}")


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
# email='kadirburakunal@gmail.com'
# password='5155078kadir'
# girilenEmail=input('E mail giriniz: ')
# girilenPassword=input('Şifre giriniz: ')
# sonucEmail=(email==girilenEmail.strip())
# sonucPassword=(password==girilenPassword)
# sonuc=sonucEmail and sonucPassword
# print(f"Girdiğiniz e mail ve şifre: {sonuc}")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# x=int(input('1. sayıyı giriniz: '))
# y=int(input('2. sayıyı giriniz: '))
# z=int(input('3. sayıyı giriniz: '))

# result = (x>y) and (x>z)
# print(f"x Sayısı en büyük sayıdır: {result}")
# result = (y>x) and (y>z)
# print(f"y Sayısı en büyük sayıdır: {result}")
# result = (z>x) and (z>y)
# print(f"z Sayısı en büyük sayıdır: {result}")




# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 aldığında ortalamanın önemi olmasın.
# vize1 = float(input('1. vize sınav notu: '))
# vize2 = float(input('2. vize sınav notu: '))
# final = float(input('Final sınav notu: '))
# ortalama = (((vize1 + vize2)/2)*0.6) + (final * 0.4)
# result = (ortalama >= 50) and (final >=50)
# print (f"Dersten geçtiniz mi: {result}")



# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo/ boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name = input('Adınızı Giriniz: ')
kilo = float(input('Kilonuzu giriniz: '))
boy = float(input('Boyunuzu giriniz: '))
index = (kilo) / (boy**2)

zayıf = (index>0) and (index<=18.4)
normal = (index>=18.5) and (index<=24.9)
fazlakilolu = (index>=25.0) and (index<=29.9)
obez = (index>30.0) and (index<=34.9)

print (f"{name} kilo indexin: {index} ve kilo değerlendirmen zayıf: {zayıf}")
print (f"{name} kilo indexin: {index} ve kilo değerlendirmen normal: {normal}")
print (f"{name} kilo indexin: {index} ve kilo değerlendirmen fazla kilolu: {fazlakilolu}")
print (f"{name} kilo indexin: {index} ve kilo değerlendirmen obez: {obez}")