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


