numbers=[]

for x in range (10):
    numbers.append(x)
print(numbers)
numbers=[x for x in range (10)]
print (numbers)
for x in range(10):
    print(x**2)
numbers=[x**2 for x in range(10)]
print (numbers)

numbers=(x*x for x in range(10) if x%3==3)
print(numbers)

myString='Hello'
myList=[]
for letter in myString:
    myList.append(letter)
print(myList)

myList=[letter for letter in myString]
print(myList)

years=[1983,199,2008,1986]
ages = [2022-year for year in years]
print (ages)

result= [x if x%2==0 else 'TEK' for x in range(1,10)]
print(result)

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))

print((x,y))

numbers=[(x,y,z) for x in range(3) for y in range (3) for z in range(3)]
print(numbers)
