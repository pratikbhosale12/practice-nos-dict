

print("-------------------------------------------------")
def sample():
    try:
        x = int(input("Enter:"))
    except:
        print("You did not enter int")
        x = int(input("Enter:"))

y = sample()
print("-------------------------------------------------")

def sample2():
    try:
        x = int(input("Enter:"))
    except:
        print("You did not enter int")
        x = int(input("Enter:"))
    finally:
        print("Always executed")
    print(x)

y = sample2()
print("-------------------------------------------------")

try:
    f = open("testfile",'w')
    f.write("Test write this")
except IOError:
    #Check for IO error exception
    print("could not find file or read data")
else:
    print("Content written successfully")
    f.close()
print("-------------------------------------------------")

try:
    f = open("testfile",'w')
    f.write("Test write this")
    f.close()
finally:
    print("Always execute")

print("-------------------------------------------------")

def askint():
    while True:
        try:
            val = int(input("Enter int:"))
        except:
            print("Looks like u did not enter int ")
            continue
        else:
            print("Yup,its an integer")
            break
        finally:
            print("Finally executed")
        print(val)
x = askint()

print("-------------------------------------------------")
for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("Incorrect Data Type")
        continue
print("-------------------------------------------------")

x=5
y=0

try:
    print("X = ",x)
    print("Y = ",y)
    z=x/y
    print(z)
except ZeroDivisionError:
    print("Division by Zero not possible")

finally:
    print("All Done")

print("-------------------------------------------------")

def ask():
    while True:
        try:
            val = int(input("Enter int:"))
        except:
            print("Oops!! Looks like you did not enter integer")
            continue
        else:
            print("Value:",val)
            print("Square:",val**2)
            break
        finally:
            print("Execution Successfull")
x = ask()
print("-------------------------------------------------")





