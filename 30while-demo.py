sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesini while ile ekrana yazdırın.

# x = 0
# while x<len(sayilar):
#     print(sayilar[x])
#     x += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

# baslangic = int(input("Başlangıç değerini giriniz: "))
# bitis = int(input("Bitiş değerini giriniz: "))
# while (baslangic<=bitis):
#     if(baslangic%2==1):
#         print("Sayınız: ",baslangic)
#     baslangic+=1

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

# i=100
# while i>=0:
#     print(i)
#     i-=1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# numbers=[]
# i=1
# while i<=5:
#     sayi=int(input(f"{i}. Sayıyı giriniz: "))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapın (name,price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet=int(input('Kaç adet ürün eklemek istiyorsunu: '))

i=0

while i<adet:
    name=input('Ürün İsmi: ')
    price=input('Ürün fiyatı: ')
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
for urun in urunler:
    print(f"Ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")