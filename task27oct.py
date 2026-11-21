###EXCEPTION HANDLING
#1)Handle division by zero
# num1=int(input("Enter first number: "))
# num2=int(input("Enter Second number: "))
# try:
#     result=num1/num2
#     print(result)
# except ZeroDivisionError as zd:  #exception defination
#     print("Zero division by error:",zd)
# finally:
#     print("end of program")


# #2)Handle invalid input (Value Error)

# try:
#    num=int(input("Enter any number: "))
# except ValueError as ve:
#     print("value Erorr:",ve)
# finally:
#     print("end of program")


#3)Handle multiple exceptions

# try:
#     a=int(input("Enter first number: "))
#     b=int(input("Enter Second Number: "))
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print("Zero division Error")
# except ValueError:
#     print("Value Error")


# #4)use else and finallly block
# try:
#     a1=int(input("Enter First Number: "))
#     a2=int(input("Enter second number: "))
#     result=a1/a2
#     print(result)
# except ZeroDivisionError:
#     print("Zero divsion error")
# else:
#     print("no error occurs")
# finally:
#     print("end of programs")


# #5)Handle a list index error  ( find the number using its index)
# try:
#     numbers=[1,2,3,4,5]
#     user=int(input("choose index: "))
#     print(numbers[user])
# except IndexError:
#     print("index error")
# except ValueError:
#     print("value error")
# finally: 
#     print("End of Program")


# #6)raise ValueError
# try:
#     age=int(input("Enter Your Age: "))
#     if age<0:
#         raise ValueError("Age cannot be negative")

#     print("your age is ",age)
# except ValueError as ve:
#     print(ve)

# #7)custom Exception
# class insufficientBalanceError(Exception):
#     pass
# balance=5000
# withdrawn=6000
# if withdrawn>balance:
#     raise insufficientBalanceError("Insuffficient balance")


# #8)CUSTOM EXCEPTION - bank withdrawal 
# class InsufficientBalanceError(Exception):
#     pass
# balance=5000
# try:
#     withdrawal=int(input("Enter Withdraw Amount: "))

#     if withdrawal>balance:
#         raise InsufficientBalanceError("insufficient balacne")
    
# except InsufficientBalanceError as e:
#     print(e)

# else:
#     balance=balance-withdrawal
#     print("Withdrawal Successful: ")
#     print("Remaining balance: ",balance)
# finally:
#     print("end of program")


# #9)Student Marks Validation
# try:
#     marks=int(input("Enter Student Marks: "))
#     if marks<0 or marks>100:
#         raise ValueError("Marks must be between 0 and 100")
# except ValueError as ve:
#     print(ve)
# else:
#     print("Valid Marks")
# finally:
#     print("Checking completed")


# #10) File Handling + Exception Handling
# try:
#     f=open("dem.txt","r")
#     print(f.read())
# except FileNotFoundError as fe:
#     print(fe)
# finally:
#     print("end of program")


# #11)Login Validation
# try:
#     age=int(input("Enter Your Age: "))
#     if age<18:
#         raise ValueError("Access denied:You must be 18 or older")
# except ValueError as ve:
#     print(ve)
# else:
#     print("Access granted")
# finally:
#     print("Login check completed")



###decorators
# #1)To execute a message before calling the original function.
# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#     return wrapper

# def hello():
#     print("Hello, Python")

# hello=decorator(hello)
# hello()


#2)Add a message before a function executes
# def decorator(func):
#     def wrapping():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapping

# @decorator
# def msg():
#     print("hello Good morning")

# msg()


#3)create a decorator that prints a message before a calculator function runs.
# def decorator(func):
#     def wrapping():
#         print("Calculator started")
#         func()
#     return wrapping

# @decorator
# def add():
#     a=10
#     b=20
#     result=a+b
#     print("The Sum is: ",result)

# add()


# #4)Create a decorator using @decorator that prints a message after the original function finishes.
# def decorator(func):
#     def wrapping():
#         func()
#         print("Download Completed")
#     return wrapping
    
# @decorator
# def download():
#     print("Downloading file...")
# download()


# #5)A decorator can check a condition before allowing a function to execute.
# is_logged_in=True
# def decorator(func):
#     def wrapping():
#         if is_logged_in:
#             func()
#         else:
#             print("Access denied! Please log in first")
#     return wrapping

# @decorator
# def profile():
#     print("Welcome to your profile!")

# profile()


#6)Create a decorator that measures how long a function takes to execute.
import time
def decorator(func):
    def wrapping():
        start=time.time()   #record the current time.
        # time.sleep(2)    #pauses the program for about 2 seconds.
        func()
        end=time.time()     #calculates the time taken.
        print("time taken",end-start,"seconds")
    return wrapping


@decorator
def task():
    print("Task started")
    print("Task Completed")
task()



    