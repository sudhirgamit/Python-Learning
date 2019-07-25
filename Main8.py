# Functions

def add_multi(a,b):
    sum = a + b
    multi = a * b
    sub = a - b
    div = a / b
    mod = a % b
    return sum,multi,sub,div,mod

#print("Arithmetic Oparetion : ",add_multi(10,2))
add,multi,sub,div,mod=add_multi(10,4)
print("Sum : ",add,"\t Multi : ",multi,"\t Sub : ",sub,"\t Div : ",div,"\t Mod : ",mod)

def add(a,b):
    c=a+b
    print("The Sum Is : ",c)
def sub(a,b):
    c=a-b
    print("The Sub Is : ",c)
def multi(a,b):
    c=a*b
    print("The Multi Is : ",c)
def div(a,b):
    c=a/b
    print("The Div Is : ",c)
def mod(a,b):
    c=a%b
    print("The Mod Is : ",c)

choice = input("Enter A Choice : ")
if choice=="sum":
    a = int(input("Enter Value One : "))
    b = int(input("Enter Value Two : "))
    add(a,b)
elif choice=="sub":
    a = int(input("Enter Value One : "))
    b = int(input("Enter Value Two : "))
    sub(a,b)
elif choice=="multi":
    a = int(input("Enter Value One : "))
    b = int(input("Enter Value Two : "))
    multi(a,b)
elif choice=="div":
    a = float(input("Enter Value One : "))
    b = float(input("Enter Value Two : "))
    div(a,b)
elif choice=="mod":
    a = int(input("Enter Value One : "))
    b = int(input("Enter Value Two : "))
    mod(a,b)
else:
    print("No Found..!")