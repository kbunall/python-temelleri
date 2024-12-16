# inheritance (kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)
# öğrenci ve öğretmende bir insan olduğundan o sınıfı bir alt sınıflarda
# kullanabiliriz ya da miras alabiliriz.

# Animal => Dog(Animal), Cat(Animal) 
# Aynı şekilde kedi ve köpek de bir hayvan olduğundan miras yolu ile alt
# sınıflarda kullanabiliriz.

class Person():
    def __init__(self, fname, lname):
        self.firstName=fname
        self.lastName=lname
        print('Person Created')
    
    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('ı am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber=number
        print('Student Created')
    
    # override
    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)  # super yazdığımız zaman tekrardan self kullanmamız gerekmiyor.
        self.branch=branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')
p1=Person('Kadir','Ünal')
s1=Student('Serpil','Ünal',1256)
t1=Teacher('Serkan','Yılmaz','Math')

print(p1.firstName+' '+p1.lastName)
print(s1.firstName+' '+s1.lastName+' '+str(s1.studentNumber))
print(t1.firstName+' '+t1.lastName+' '+t1.branch)

p1.eat()
s1.eat()

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

s1.sayHello()