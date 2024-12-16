with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read(10)
    print(content)
    file.seek(10) # tekrardan 10. konuma gönderiyoruz.
    print(file.tell())
    content2=file.read()
    print(content2)

# with ile blok komut oluştururuz.
# Bundan sonrasında close yazmamıza gerek kalamz