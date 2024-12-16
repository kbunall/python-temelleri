# x = 10

# if x > 5:
#     raise Exception("x 5 den büyük değer alamaz.")

# def check_password(psw):
#     import re # Regular Expreption ismindeki modülü import ediyoruz ve bunun aracılığıyla kontrol ediyoruz.
#     if len(psw) < 8:
#         raise Exception("parola en az 8 karakter olmalıdır.")
#     elif not re.search("[a-z]",psw): # true değeri aldığında raise çalışacak ve o cümleyi ekrana yazdırıcak.
#         raise Exception("parola küçük harf içermelidir.") # not diyerek soruyu tersten sorduğumuz için küçük harf bulamazsa yazdırıcak
#     elif not re.search("[A-Z]",psw):
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[0-9]",psw):
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("parola alpha numeric karakter içermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("parola boşluk içermemelidir.")
#     else:
#         print("geçerli parola")
   
# password = "1234567aA_"

# try:
#     check_password(password) # burada try ile kontrol ediyoruz.
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola: else")
# finally:
#     print("validation tamamlandı")


class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name=name

p=Person("Aliiiii",1989)