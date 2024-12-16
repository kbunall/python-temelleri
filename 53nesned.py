# def greeting(name):
#     print('hello',name)

# print(greeting('ali'))
# print(greeting)

# sayHello=greeting

# print(sayHello)
# print(greeting)

# del sayHello

# print(sayHello)
# print(greeting)

# encapsulation - kapsülleme yapma

# def outer(num1):
#     print('outer')
#     def inner_increment(num1): # burada ilk başta inner fonksiyonunu çağırmadığımız çalışmaz
#         print('inner')
#         return num1 + 1
#     num2=inner_increment(num1) # bundan dolayı buraya bu fonksiyonu ekliyoruz ve içeride olan fonksiyonu da çalıştırıyoruz.
#     print(num1,num2 )

# outer(10)

def factorial(number):
    if not isinstance(number,int): # gönderdiğimiz değerleri hata kontrol etme ile kontrol edebiliriz.
        raise TypeError("number must be an integer")
    
    if not number >=0:
        raise ValueError("number must be zero or positive")


    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)

try:
    print(factorial(4))
except Exception as ex:
    print(ex)