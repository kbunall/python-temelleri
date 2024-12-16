# try:
#     file=open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")
#     file.close()

file=open("newfile.txt","r", encoding='utf-8')

# *******for döngüsü*******

# for i in file:
#     print(i, end="")  # end parametresi print yazıldıktan sonra boş satır ekleme diyebilriz.

# *******read() fonksiyonu********

# content1=file.read()
# print("içerik 1")
# print(content1)


# file=open("newfile.txt","r", encoding='utf-8')
# content2=file.read()
# print("içerik 2")
# print(content2)

# content=file.read(5) # 5 bit olarak adlandırabiliriz.
# content=file.read(3)
# content=file.read(3)
# print(content)

# *********** readline() fonksiyonu ***************
# Her seferinde 1 satırı okur.

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

# ********** readlines() fonskiyonu **************

liste = file.readlines()
print(liste[0])
print(liste[1])
print(liste[2])

# her bir satır bilgiyi bir dizi liste elemanı olarak karşımıza çıkarır.


file.close()