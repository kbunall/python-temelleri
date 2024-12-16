# error handling => hata yönetimi

# try:
#     x= int(input('x: '))
#     y= int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError): # gelebilecek hata türlerini yazıyoruz ve o hata ile karşılaşınca önlem alıyoruz.
#     print('Yanlış bilgi girdiniz.')

# try:
#     x= int(input('x: '))
#     y= int(input('y: '))
#     print(x/y)
# except: # hata türünü tespit edemiyoruz ama hataya önlem alıyoruz.
#     print('Yanlış bilgi girdiniz.') # çok kullanılmayan bir yöntem

while True:
    try:
        x= int(input('x: '))
        y= int(input('y: '))
        print(x/y)
    except Exception as ex: # genel bir hata türü bunu kullanarak alabileceğimiz hataları genelleyip hata türünü öğrenebiliriz.
        print('Yanlış bilgi girdiniz.', ex)
    else: 
        break  # eğer try bölümünden her hangi bir hata gelirse exept yazılır ancak yoksa else kısmında bu yazılır.
    # bizden doğru bilgiyi alana kadar devam eder ve doğru bilgi aldığında döngüden çıkar ve biter.
    finally:  # her zaman çalışır. amaç kaynakların kapatılması aşamasında. örneğin dosya açtığımızda okuması bittiğinde dosyayı kapatmak için.
        print('try except sonlandı.')