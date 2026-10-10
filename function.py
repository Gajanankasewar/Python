#Non-parameterized function

def display():                  #fun defination
    print("hello World")        #fun body

display()                       #fun calling
display()
display()                       

def display():
    print("Pravin")
display()


#parameterized function
def add(a,b):       #parameter
    print(a+b)
add(10,20)    
add(100,200)      #arguments

#pallindrome

def para():
    num=int(input("Enter any Number: "))
    rev=0
    temp=num
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if temp==rev:

        print("pallindrome")
    else:
        print("not pallindrome")

para()




#Pallindrome
def pall():
    a=int(input("Enter any number: "))
    rev=0
    temp=a
    while a>0:
        rem=a%10
        rev=rev*10+rem
        a=a//10
    print("Reverse: ",rev)

    if temp==rev:
        print("Pallindrom")
    else:
        print("Not Pallindrom")
pall()


#Reverse
def janni():
    r=int(input("Enter any Number: "))
    rev=0
    temp=r
    while r>0:
        rem=r%10
        rev=rev*10+rem
        r=r//10
    print(rev)
janni()

#Armstrong
def doremon():
    x=int(input("Enter a number: "))
    sum=0

    temp=x
    while x>0:
        rem=x%10
        sum=sum+rem**3
        x=x//10

    if temp==sum:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
doremon()

#Addition 
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
def add():
    sum=a+b
    print(sum)
add()
add()
add()

def sub():
    c=int(input("Enter 1st Number: "))
    d=int(input("Enter 2nd Number: "))
    dif=c-d
    print(dif)
sub()

##Multiplication
def mul():
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number"))
    multiplication=num1*num2
    print(multiplication)
mul()
mul()

#division
def div():
    e=int(input("enter 1st Number: "))
    f=int(input("Enter 2nd Number: "))
    division=e/f
    print(division)
div()
div()


# Factorial using Function

n = int(input("Enter a number: "))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("Factorial =", factorial(n))


