# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişim_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
# **Dosyayı konumda oluşturur.
# ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file=open("newfile.txt","w")
# file.close()

# file=open("C:/users/gfb_k/masaüstü/newfile.txt","w")
# print(file)

# file=open("newfile.txt","w",encoding='utf-8') # encoding kodu bir çok karakteri tanımaya yarıyor.
# file.write("Kadir Burak Ünal")
# file.close()


# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.

# file=open("newfile.txt","w",encoding='utf-8')
# file.write("Kadir Burak Ünal\n")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.

file=open("newfile.txt","w",encoding='utf-8')

# "r": (Read) okuma. Varsayılan dosya konumda yoksa hata verir.