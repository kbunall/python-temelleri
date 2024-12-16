liste=[1,2,3,4,5]

# iterator = iter(liste)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in liste:
#     print(i)

# for dögüsüyle liste elemanlarını yazdırmamız aşağıdaki gibi bir işlemi basitçe yapmamızı sağlıyor.

# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

# peki neden bunları yapıyoruz?

class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration
        
list=MyNumbers(10,20)

for x in list:
    print(x)