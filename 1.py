#Variable Declaration
x = 4
y = "Hello"
print(x,y)

#Explicit Type Casting
a = str(3)
b = int(3)
c = float(3)
print(a,b,c)
print(type(a), type(b), type(c))

x,y,z = "X","Y","Z"
print(x)
print(y)
print(z)

lst = ["X","Y","Z"]
x,y,z = lst
print(x)
print(y)
print(z)

x = y = z = "Pratik"
print(x)
print(y)
print(z)


import random
print(random.randrange(1,11))

#Slicing
x = "Hello World"
print(x)
print(x[2:7])
print(x[2:])
print(x[:7])
print(x[-7:-2])
print(x[::-1])
print(x[2:10:2])

print(x.upper())
print(x.lower())
print(x.split(" "))
print(x.replace("H","J"))

a= "Hello"
b = "World"
c = a + " " + b
print(c)

print(a.capitalize())
print(a.casefold())
print(a.swapcase())
print(a.center(10))
print(a.endswith("o"))
print(a.endswith("o",1,4))
print(a.find("l"))
print(a.find("l",1,4))



a = 12
b = "My age is" + " " + str(a)
print(b)

#Formatting
c = "My age is {}"
print(c)
print(c.format(a))

print(bool())
print(bool(1))
print(bool({}))

#Arithmatic Operations
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)
print("10" + "5")

a = ["Prat", 4, 6.3]
print(len(a))
print(type(a))

b = ("a",1,2)
print(type(b))

c = {"a" : 1,"b" : "Prat"}
print(len(c))
print(type(c))
print(c["a"])

a = ["Apple","Mango","Orange"]
print(a)

a[1] = "Banana"
print(a)

a[1:2] = ["Watermelon","Kiwi"]
print(a)

a.append("Muskmelon")
print(a)

a.insert(2,"Dragonfruit")
print(a)

b = ["Potato","Tomato"]
print(b)

a.extend(b)
print(a)

a.remove("Kiwi")
print(a)

a.pop()
print(a)

a.pop(3)
print(a)

for item in a:
    print(item)

for i in range(len(a)):
    print(a[i])

c = (1,2,3)
print(c)
del(c)  #Deletes complete structure not even empty tuple remains

b.clear()
print(b) #Empty list remains

#List Comprehension
newlst = [x for x in a if x != "Apple"]
print(newlst)

newlst = [x for x in range(10)]
print(newlst)

newlst = [x.upper() for x in a]
print(newlst)

x=0
while x < len(a):
    print(a[x])
    x += 1

#Find Largest Number
#Using built-in function
lst = [1,2,3,10,4,5]
greatest = lst[0]

for x in lst:
    if x > greatest:
        greatest = x
        x += 1
print(greatest)

#Using sort
lst.sort()
greatest = lst[-1]
print(greatest)

#Using max
greatest = max(lst)
print(greatest)

#Tuple
tuple1 = ("A","B","C")
print(tuple1)
print(type(tuple1))
print(len(tuple1))

tuple2 = ("D","E","F")
print(tuple2)

concattuple = tuple1 + tuple2
print(concattuple)
print(len(concattuple))
print(type(concattuple))

print(concattuple.count("A"))
print(concattuple.index("B"))

x=0
while x < len(concattuple):
    print(concattuple[x])
    x += 1

#Appending to tuple
temp = list(tuple1)
print(type(temp))
temp.append("D")
temp.append("E")
print(temp)

temptuple = tuple(temp)
print(temptuple)
print(type(temptuple))

#Assign variable to tuple values
(a,b,*c) = temptuple
print(temptuple)
print(a)
print(c)

(a,b,c,*d) = temptuple
print(a)
print(c)
print(d)

#Find frequency for each element
tuple1 = ("A","B","B","E","F","A","D","A")
print(tuple1)
freq_dict = {}
for ele in tuple1:
    if ele in freq_dict:
        freq_dict[ele] += 1
    else:
        freq_dict[ele] = 1
print(freq_dict)

set1 = {1,2,3,"p","r",False,2.6}
print(set1)
print(type(set1))
set1.add("apple")
print(set1)

tempset = {2,3,4,5,6}
templist = [7,8,9]

set1.update(tempset)
print(set1)

set1.update(templist)
print(set1)

set1.remove("r")
print(set1)

set1.discard(1)
print(set1)

set1.pop()
print(set1)

set1.pop()
print(set1)

tempset.clear()
print(tempset)

tempset = {99,66,69}

set2 = set1.union(tempset)
print(set2)

#Removes items that exist in both set, creates new set
set2 = set1.difference(tempset)
print(set2)

#Removes items that is not present in both set, creates new set
set2 = set1.intersection(tempset)
print(set2)

#Removes items that exist in both set, does not create a new set make changes to og set
set3 = set1.difference_update(tempset)
print(set3)

#Removes items that is not present in both set, makes changes to og set
set2 = set1.intersection_update(tempset)
print(set2)

del(tempset)

list1 =  [1,2,3,4,5]
list2 = [4,5,6,7,8]
set1 = set(list1)
set2 = set(list2)

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.intersection_update(set2))
print(set1.difference_update(set2))

#DICTIONARY
dict1 = {"Name":"Pratik","ID":12,1:20.7}
print(dict1)
print(dict1["Name"])

dict1["Name"] = "Wils"
print(dict1["Name"])
print(dict1.keys())
print(dict1.values())
