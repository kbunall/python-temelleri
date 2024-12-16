# 1- Girilen 2 sayıdan hangisi büyüktür?
# x=input('1. Sayıyı giriniz: ')
# y=input('2. Sayıyı giriniz: ')

# result=x>y
# print(f"1. Sayı {x}, 2. Sayı {y} 'dan büyüktür: {result}")

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#     Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# vize1=float(input('1. Vize: '))
# vize2=float(input('2. Vize: '))
# final=float(input('Final: '))
# ortalama=(((vize1+vize2)/2)*0.6) + (final*0.4)
# result= ortalama>=50
# print (f"not ortalamanız:{ortalama}, dersten geçme durumunuz: {result}")


# 3- Girilen birsayının tek mi çift mi olduğunu yazdırın.
# sayi=int(input('sayi: '))
# tekcift= (sayi%2==0)
# print(f"Girilen sayı çift olma durumu: {tekcift}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# sayi=int(input('sayi: '))
# pozitifmi=(sayi>0)
# print(f"Girilen sayının pozitif olma durumu{pozitifmi}")

# 5- Parola ve e mail bilgisini isteyip doğrulunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

email='email@sadikturan.com'
password='abc123'
girilenEmail=input('email: ')
girilenPassword=input('parola: ')
isEmail= (email==girilenEmail.strip()) # boşlukları silmek için strip() çalıştırılır
isPassword=(password==girilenPassword.lower()) # büyük küçük harf önemsenmiyorsa .lower() yazılır
print(f"Email bilgisi doğrumu: {isEmail} ve parola doğru mu: {isPassword}")