"""
1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

Müşteri adı
Müşteri soyadı
Müşteri ad + soyad
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı

"""

musteriAdı = "Kadir Burak"
musteriSoyadı = " Ünal"
musteriAdSoyad = musteriAdı+" "+musteriSoyadı
musteriCinsiyet = "Erkek"
musteriTc = "54628690730"
musteriDogumYili = 1998
musteriAdres = "Ankara Keçiören"
musteriYası = 2022 - musteriDogumYili

"""
2- aşağıdaki siparişlerin toplam bilgisini hesaplayınız

Sipariş 1 => 110 TL
Sipariş 2 => 1100.5 TL
Sipariş 3 => 356.95 TL

"""

siparis1= 110
siparis2= 1100.5
siparis3=356.95
toplam=siparis1+siparis2+siparis3
print ("Toplam=",toplam)