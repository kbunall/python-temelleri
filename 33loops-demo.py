'''
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile bulmaya çalışın.
** "random modülü" için "python random" şeklinde arama yapın.
** 100 üzerinden puanlama yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru bittiğinde belirtilen can sayısı üzerinden hesaplansın.

'''

import random
sayi = random.randint(1,100)
can = int (input('Kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0
while hak > 0:
    hak-=1
    sayac +=1
    tahmin = int(input('tahmin: '))
    if sayi == tahmin:
        print(f"Tebrikler {sayac}. Defada Bildiniz! Toplam Puanınız: {100 - (100/can)*(sayac-1)}")
        break
    elif tahmin < sayi: 
        print("Yukarı...")
    elif tahmin > sayi:
        print("Aşağı...")
    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}')