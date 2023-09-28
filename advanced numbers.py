import math

print("--------------------------------------------------------")
#Problem 1: Convert 1024 to binary and hexadecimal representation

print("1024 in Binary:",bin(1024))
print("1024 in Hexadecimal:",hex(1024))

print("--------------------------------------------------------")
#Problem 2: Round 5.23222 to two decimal places
x = 5.23222
y = round(x,2)
z = format(x,".2f")
print("Float: ",x)
print("Rounded float :",y)
print("Rounded float using format:",z)

print("--------------------------------------------------------")
#Problem 3: Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling okay?'
if s.islower() == True:
    print("All letters in string s are in lower case")
else:
    print("All letters in string s are not in lower case")

print("--------------------------------------------------------")
#Problem 4: How many times does the letter 'w' show up in the string below?

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print("count of w in string s:",s.count('w'))

# Using Loop
count = 0
for i in s:
    if i == 'w':
        count += 1
print("count of w in string s:",count)

print("--------------------------------------------------------")
#Problem 5: Find the elements in set1 that are not in set2:

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print("Elements in set1 that are not in s2:",set1.difference(set2))

#Using Loop
diff = []
for i in set1:
    if i not in set2:
        diff.append(i)

print("Elements in set1 that are not in s2:",set(diff))

print("--------------------------------------------------------")
#Problem 6: Find all elements that are in either set:

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print("Elements in either set:",set1.union(set2))

#2nd Approach
print("Elements in either set:",set(list(set1) + list(set2)))

print("--------------------------------------------------------")
#Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.

data = [(0,0), (1,1), (2,8), (2,27), (4,64)]
dict_data = dict(data)
print("Dictionary:",dict_data)
print(type(dict_data))

cube_dict = {num: num*num*num for num in range(1, 5)}
print(cube_dict)

print(cube_dict)

print("--------------------------------------------------------")
#Problem 8: Reverse the list below:

list1 = [1,2,3,4]
print("Original List:",list1)

rev = list1[::-1]
print("Reversed List using slicing:",rev)

print("--------------------------------------------------------")

#Problem 9: Sort the list below:

list2 = [3,4,2,5,1]

print("Original List:",list2)
print("Sorted List in Asc:",sorted(list2))
print("Sorted List in Desc:",sorted(list2,reverse=True))

print("--------------------------------------------------------")

#Write a function that computes the volume of a sphere given its radius.

def volume(r):
    vol = 4/3*math.pi*(r**2)
    print("Radius:",r)
    print("Volume:",vol)

r = int(input("Enter radius of sphere:"))
x = volume(r)

print("--------------------------------------------------------")
#Write a function that checks whether a number is in a given range (inclusive of high and low)

def check_range(nos,start,end):
    if nos in range(start,end+1):
        return True
    else:
        return False

nos = int(input("Enter number to check:"))
start = int(input("Enter start :"))
end = int(input("Enter end :"))

x = check_range(nos,start,end)
if x == True:
    print("Number:"+str(nos)+" lies in range ("+str(start)+","+str(end)+")")
else:
     print("Number:"+str(nos)+" does not lie in range ("+str(start)+","+str(end)+")")

print("--------------------------------------------------------")

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def check_case(s):
    upper = 0
    lower = 0

    for i in s:
        if i.isupper() == True:
            upper += 1
        else:
            lower +=1

    print("Count of upper case characters:",upper)
    print("Count of lower case characters:",lower)

s = input("Enter string: ")

case = check_case(s)

print("--------------------------------------------------------")

#Write a Python function to multiply all the numbers in a list.

def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

lst =[]
n = int(input("Enter number of elements in list: "))
for i in range(0,n):
    ele = int(input("Enter Number:"))
    lst.append(ele)
print(lst)

x = multiply_list(lst)
print("Result of list multiplication: ",x)

print("--------------------------------------------------------")
#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#	Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#	For example : "The quick brown fox jumps over the lazy dog"

def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    unique_s = set(s.lower())
    for i in alphabet:
        if i not in unique_s:
            return False

    return True

s = input("Enter String:")
x = is_pangram(s)
if x == True:
    print("String is Pangram")
else:
    print("String is not a Pangram")


print("--------------------------------------------------------")
