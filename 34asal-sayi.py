'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

'''
sayi = int(input('Bir sayı giriniz: '))
# i=0
# if sayi==1:
#     print ('1 Sayısı asal değildir.')
# while i < 100:
#     if sayi%2==0:
#         print('Girdiğiniz sayı asal bir sayı değildir.')
#     elif sayi%3==0:
#         print('Girdiğiniz sayı asal bir sayı değildir.')
#     elif sayi%5==0:
#         print('Girdiğiniz sayı asal bir sayı değildir.')
#     else:
#         print('Tebrikler girdiğiniz sayı asal bir sayıdır!')
#     break
    
asalmi = True

if sayi == 1:
    asalmi=False
for i in range(2,sayi):
    if (sayi%i==0):
        asalmi=False
        break

if asalmi:
    print('sayı asaldır')
else:
    print('sayı asal değildir.')