#class

class Person:
    # class attributes
    address='no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):   # self clastan türetilen parametler demek
        
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı')
    # instance methods
    def intro(self):
        print('Hello There. I am '+self.name)
    def calculateAge(self):
        return 2019-self.year
# object (instance)
p1 = Person(name='ali',year=1990)
p2 = Person('yağmur',1998)

p1.intro()
p2.intro()

print(f"Adım {p1.name} ve Yaşım: {p1.calculateAge()}")
print(f"Adım {p2.name} ve Yaşım: {p2.calculateAge()}")

class Circle:
    # Class object attribute
    pi=3.14
    def __init__(self, yaricap=1):
        self.yaricap=yaricap

    # methods
    
    def cevre_hesaplama(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)    

    
c1 = Circle() # yaricap=1
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesaplama()}")
print(f"c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesaplama()}")