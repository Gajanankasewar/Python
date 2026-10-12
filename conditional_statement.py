## if ###

age=19
if(age>=18):
    print("Eligible for vote")


age=9
if(age>=18):
        print("you are eligible")
print("Ghari ja ghari")

a=2
if(a%2==0):
        print("even number")


## if-else ###

age=18
if(age>=18):
    print("you are eligible")
else:
    print("you are not eligible")



## INPUT AND OUTPUT STATEMENT ###

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
sum=a+b
sub=a-b
mul=a*b
div=a/b
print("Addition:",sum)
print("substraction: ",sub)
print("multiplication: ",mul)
print("divisionn: ",div)


## convert int into string AND string into int ###



## Ladder ###

marks=int(input("Enter Student Marks: "))
if(marks>100):
    print("Invalid entry")
elif(marks>95 and marks<=100):
    print("A+ Grade")
elif(marks>83 and marks<=95):
    print("B+ grade")
elif(marks>65 and marks<=83):
    print("C+ grade")
elif(marks>35 and marks<=65):
    print("D+ grade")
else:
    print("Fail")


a=int(input("Enter first Number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

if(a>b and a>c):
    print("A is Greater")
elif(b>a and b>c):
    print("B is greater")
elif(c>a and c>b):
    print("C is greater")
else:
     print("values are same")


## Nested If ###

num=7
if(num>0):
    print("positive Number")
    if(num%2==0):
        print("Even Number")
    else:
        print("odd number")

else:
    print("Negative Number")

    
#authentication
username=input("Enter Username: ")
password=int(input("Enter Password: "))
if username=="pass123" and password==1234:
    print("Login Successfull")
else:
    print("Invalid Credentials")