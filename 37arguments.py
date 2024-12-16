# def changeName(n):
#     n='ada'
# name = 'yiğit'
# changeName(name)
# print(name)

# def change (n):
#     n[0]='istanbul'
# sehirler=['ankara','izmir']

# change(sehirler[:])
# print(sehirler)

# def add(*params):
#     return sum((params))

# print(add(10,20,50))
# print(add(10,30,50,40))
# print(add(10,40,50,50,70,60,10,20))

#Tuple listesi istiyorsak tek '*' yıldız kullanıcaz Dictionary kullanmak istiyorsa '**' çift yıldız kullanıcaz.

def displayUser(**args):
    for key, value in args.items():
        print(f'{key} is {value}')
displayUser(name='çınar',age=2,city='istanbul')
displayUser(name='Ada',age=12,city='kocaeli',phone='123123123')
displayUser(name='kadir',age=24,city='ankara',phone='123123123',email='kadirburakunal@gmail.com')

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70,key1='value 1',key2='value 2')