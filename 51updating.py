# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(10)
#     file.write("deneme")
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# ********** Sayfa sonunda güncelleme ***************

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nSerpil ünal")

# ********** Sayfa başında güncelleme ***************

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="efe turan\n"+content
#     file.seek(0)
#     file.write(content)

# ********** Sayfa ortasında güncelleme ***************

with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"yılmaz aygün\n")
    file.seek(0)
    file.writelines(list) 
    # listeyi direk metoda verebiliriz. bu yöntem ile direk ekler.
    

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())