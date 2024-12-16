# decorators fonksiyonları neden kullanıyoruz?
# bir fonksiyona bir özellik eklemek istediğimizde kullanıyoruz.
# bir özelliği birden fazla yerde kullanmak istiyorsak bunun için bir decorators fonksiyonu
# oluşturup birçok fonksiyon ile ilşkilendirebiliyoruz.
# amacımız daha az kod kullanmak.

# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator # bu işlem ile sayHello fonksiyonunu direk decoratorun içine iletiyor
# def sayHello(name):
#     print("hello",name)

# sayHello("ali")

#******************************************

import time
import math

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish=time.time()
        print("fonksiyon "+func.__name__+" "+str(finish-start)+"saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

    

usalma(2,3)
faktoriyel(4)