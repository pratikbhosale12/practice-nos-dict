#Write a program in Python to -

print("######################################")
#1. Convert decimal numbers to octal numbers.

dec = int(input("Enter Decimal Number:"))
oct = oct(dec)
print("Number in Decimal:",dec)
print("Number in Octal:",oct)

print("######################################")

#2. Reverse an integer.

integer = int(input("Enter Integer:"))
str_int = str(integer)
rev_int = int(str_int[::-1])
print("Reversed Integer:",rev_int)

print("######################################")

#3. Print the Fibonacci series using the recursive method.

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input("Enter n :"))
print("Fibonacci Sequence till ",n,"elements is:")
for i in range(n):
    print(fibo(i))

print("######################################")

#4. Return the Nth value from the Fibonacci sequence

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input("Enter n :"))
fib_lst = []
for i in range(n):
    fib_lst.append(fibo(i))
print(fib_lst)
print(n,"th element in Fibonacci Sequence is:",fib_lst[n-1])

print("######################################")
