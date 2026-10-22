import test_module;
name=input("What is Your Name ?")
test_module.show(name)


import test_module
a=test_module.person1["age"]
print(a)


##from-import
#if all functions want to work write:- from test_module import*

from test_module import addition
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Addition= ",addition(a,b)) 


##Renaming a module##
import test_module as cal;
a=int(input("Enter a: "))
b=int(input("Enter b:"))
print("Addition= ",cal.addition(a,b))