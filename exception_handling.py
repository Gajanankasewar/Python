'''Exception Handling: An unwanted and unexpected event that distrubs normal flow of program is called exception'''
#Q.what is Exception
#Q.purpose
#Q.what is  meaning of exception


##without try except
print("stmt-1")
print(10/0)
print("stmt-3")


##With try-exception
print("stmt-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("stmt-3")


#Run time exception Handling
try:
    a=int(input("Enter first Number: "))
    b=int(input("Enter Second Number: "))
    print(a/b)
except ZeroDivisionError:
    print("Can't Divide with Zero")

except ValueError:
    print("proper value provide karo")


try:
    x=int(input("Enter First Number:"))
    y=int(input("Enter Second Number: "))
    print(x/y)
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("zeroDivisionError")



#custome exception
class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg

age = int(input("Enter Age: "))

if age > 60:
    raise TooOldException("Your age already crossed marriage age... no chance of getting married")

elif age < 18:
    raise TooYoungException("Please wait some more time. You will get the best match soon")

else:
    print("You are eligible for marriage")


#Decorator
def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner


@decor
def wish(name):
    print("Hello",name,"Good Morining")
wish("Ravi")
wish("Himanshu")
wish("Sunny")


#without using @ symbol decorator
def decor(func):
    def inner(name):
        if name=="sunny":
            print("HELLO sunny Bad Morining")
        else:
            func(name)
    return inner
def wish(name):
    print("hello",name,"Good Morning")

decorfunction=decor(wish)

wish("Durva")
wish("sunny")

decorfunction("Durva")  #decorator wont be executed
decorfunction("sunny")   #decorator will be executed


