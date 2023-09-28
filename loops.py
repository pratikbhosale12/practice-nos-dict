a=5
b=9

#If-else

if (b>a):
    print("B")
elif (a>b):
    print("A")
else:
    print("Same")

#Shorthand
print("A") if a>b else print("B")

#While
i = 1
while i<5:
    print(i)
    i = i+1

#Break
i = 1
while i<5:
    print(i)
    if i == 3:
        break
    i += 1

#Continue
i = 1
while i<5:
    print(i)
    i += 1
    if i == 3:
        continue

#Lambda Function

x = lambda a: a+10
print(x(5))

x = lambda a,b : a*b
print(x(2,3))

def fun(n):
    return lambda a: a*n

trip = fun(3)    # n = 3
print(trip(9))   # a = 9

doub = fun(2)
print(doub(9))

car1 = "BMW"
car2 = "Audi"
car3 = "Porsche"
car4 = "Pagani"

cars = [car1,car2,car3,car4,"Mercedes"]
print(cars)

a = max(1,2,3,4,5,6)
b = min(1,2,3,4,5,6)
print(a,b)

x = abs(12)
y = abs(-12) #Make negative as positive
print(x,y)

x = pow(2,3) #2 raised to 3
print(x)

import math
x = math.sqrt(9)
print(x)

x = math.ceil(2.5)
y = math.floor(2.5)
print(x,y)

print(math.pi)





