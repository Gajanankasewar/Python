# # #find the number greater than 10
# numbers = [12, 7, 15, 4, 9, 20, 3]
# count=0
# for n in numbers:
#     if n>10:
#         count+=1
# print(count)


# # #largest number between list
# numbers = [4, 7, 2, 9, 6, 3]
# largest=0
# for i in numbers:
#     if i>largest:
#         largest=i
# print(largest)


# #find second-largest
# numbers = [4, 7, 2, 9, 6, 3]
# largest=0
# seclarge=0
# for i in numbers:
#     if i>largest:
#         seclarge=seclarge
#         largest=i
# for j in numbers:
#     if j>largest and seclarge<largest:
#         seclarge=j
# print(seclarge)



# # #file handling practice
# #write
# import os
# f=open("demo1.txt","w")
# f.write("Hi hello Godd Morning bro\n")
# f.close

# # #read
# import os
# f=open("demo1.txt","r")
# print(f.read())
# f.close()

# # #append
# f=open("demo1.txt","a")
# f.write("Today is 23rd October")
# f.close()

# # #readline
# f=open("demo1.txt","r")
# print(f.readline())
# print(f.readline())

# # #readlines
# f=open("demo1.txt","r")
# print(f.readlines())
# f.close()

# # #Create new file using X if exist give's error
# f=open("demo1.txt","x")

# # #with statement
# with open("demo1.txt","r") as f:
#     print(f.read())




# # ###creating and removing file 
# import os
# f=open("document2.txt","w")
# f.write("hello janni")
# f.close

# import os
# f=open("document2.txt","r")
# print(f.read())
# f.close()

# import os
# f=open("document2.txt","w")
# f.write("Now i'am practicing on File handling in python\n")

# import os
# f=open("document2.txt","a")
# f.write("This is append")

# # #remove file if exist other wise gives print statement
# import os
# if os.path.exists("document2.txt"):
#     os.remove("document2.txt")
# else:
#     print("file not exists")


# ##numpy
# import numpy
# arr=numpy.array([1,2,4,5,6])
# print(arr)

# #2d array
# import numpy
# arr=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)

# # #multidimensionaly array
# import numpy
# arr=numpy.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr)

# import numpy
# arr=numpy.array([1,2,3,4])
# print(arr.dtype)

# import numpy
# arr1=numpy.array([43.2,54.7])
# print(arr1.dtype)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)


# ##Comparison in numpy
# import numpy as np
# x=np.array([1,2,3])
# y=np.array([4,5,6])

# print("original Number")
# print(x)
# print(y)

# # #greater than
# print("greater than")
# print(np.greater(x,y))

# # #greater than equal
# print("greater than equal")
# print(np.greater_equal(x,y))

# # #less than
# print("less than")
# print(np.less(x,y))

# # #less than equal
# print("less than equal to")
# print(np.less_equal(x,y))

# #Conversion
# import numpy as np
# arr=np.array([11,22,33,44,55,66,77,88,99,10,20,30])
# a=arr.reshape(3,4)
# print(a)

# # #multideminsional
# aa=arr.reshape(2,3,2)
# print(aa)

# # #print directly
# print(arr.reshape(3,4))

# #print directly multi-dimensional
# print(arr.reshape(3,2,2))


# ##print each element in arr
# for x in arr:
#     print(x)

# import numpy as np
# arr=np.array([[1,2,3],[1,2,3],[1,2,3]])
# for i in arr:
#     print(i)

# for i in np.nditer(arr):
#     print(i)

# #find index
# a=np.array([1,2,3,4,5,4,4])
# a=np.where(a==4)
# print(a)

# #print 1-D array elements
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,0])
# for i in arr:
#     print(i)


# #print 2-d array element using for loop
# import numpy as np
# a=np.array([[11,22,33,44,55,66],[77,88,99,10,11,12]])
# for x in a:
#     for y in x:
#         print(y)


# #print 3-d array elements using for loop
# import numpy as np
# arr1=np.array([[[1,2,3],
#                 [1,2,3],
#                 [1,2,3]]])
# print(arr1)
# print(arr1.ndim)
# print(arr1.shape)


# import numpy
# a=numpy.array([32,55,67,39,69,77,76,94,88,22])
# b=numpy.where(a%2==0)
# print(b)

# print(numpy.sort(a[b]))






# #### Generator #####

# #print 1 to 5 using while
# def sequence():
#     i=1
#     while i<=5:
#         yield(i)
#         i+=1
# for i in sequence():
#     print(i)


# #print 1 to 5 by 
# def football():
#     i=1
#     while i<=5:
#         yield i
#         i+=1
# k=football()
# for i in k:
#     print(i)


# #print given yeild
# def counting():
#     yield 5
#     yield 10
#     yield 15

# k=counting()
# for i in k:
#     print(i)

# #Generate Even Numbers Using while Loop and yield
# def even_numbers():
#     i=2
#     while i<=10:
#         if i%2==0:
#             yield i
#         i+=1   
            
# for i in even_numbers():
#     print(i)

# print("")

# #Generate Odd Numbers Using a Generator
# def odd_number():
#     i=1
#     while i<=9:
#         if i%2!=0:
#             yield i
#         i+=1
# k=odd_number()
# for i in k:
#     print(i)

# print("")


# #Generate Multiples of 5 Using a Generator
# def multiples():
#     i=5
#     while i<=25:
#         if i%5==0:
#             yield i
#         i+=1
# j=multiples()
# for i in j:
#     print(i)

# print("")


# #Generate Numbers in Reverse Order
# def reverse_count():
#     i=5
#     while i>=1:
#         yield i
#         i-=1
# p=reverse_count()
# for i in p:
#     print(i)

# print("")

# #Generate Squares of Numbers Using a Generator
# def squares():
#     i=1
#     while i<=5:
#         yield i*i
#         i+=1
# for i in squares():
#     print(i)

# print("")

# #Generate Cubes Using a Generator
# def cubes():
#     i=1
#     while i<=5:
#         yield i*i*i
#         i+=1
# for i in cubes():
#     print(i)

# print("")



# #multiple of 5 
# def multiple():
#     i=1
#     num=3
#     while i<=5:
#         yield num*i
#         i+=1
# for i in multiple():
#     print(i)

# print("")


# #Generate Even Numbers Using a Generator
# def ev_num():
#     i=2
#     while i<=20:
#         if i%2==0:
#             yield i
#         i+=1
# even=ev_num()
# for i in even:
#     print(i)


# #factorial of 5
# def factorial():
#     i=1
#     fact=1
#     while i<=5:
#         fact=fact*i
#         yield fact
#         i+=1
# k=factorial()
# for i in k:
#     print(i)

# print("")


# #Generate Running Sum Using a Generator
# def running_sum():
#     i=1
#     sum=0
#     while i<=5:
#         sum=sum+i
#         yield sum
#         i+=1

# for i in running_sum():
#     print(i)

# print("")


# def power_of_two():
#     i=0
#     num=2
#     power=1
#     while i<6:
#         yield power 
#         power=power*num
#         i+=1
# p=power_of_two()
# for i in p:
#     print(i)

# print(" ")


# #Write a generator using while and yield that generates numbers from 1 to 20 that are divisible by 3 but not divisible by 2.
# def generator_numbers():
#     i=1
#     while i<=20:
#         if i%3==0 and i%2!=0:
#             yield i
#         i+=1
# w=generator_numbers()
# for i in w:
#     print(i)

# print("")


# #Write a generator using while and yield that generates numbers from 15 down to 5, including both 15 and 5.
# def reverse_no():
#     y=15
#     while y>=5:
#         yield y
#         y-=1
# for i in reverse_no():
#     print(i)

# print("")

# #Write a generator using while and yield that generates the first 10 multiples of 7, starting from 7.
# def multiple_of_seven():
#     i=1
#     num=7
#     while i<=10:
#         yield num*i
#         i+=1
# r=multiple_of_seven()
# for i in r:
#     print(i)

# print("")


# def generate_words():
#     a="Python is easy to learn"
#     i=0
#     temp=""
#     while i<len(a):
#         if a[i]==" ":
#             yield temp
#             temp=""
#         else:
#             temp=temp+a[i]
#         i+=1
#     if temp:
#         yield temp
# for word in generate_words():
#     print(word)
    

# ##### SQlite database-connectivity ######
# import sqlite3 as sq
# con=sq.connect("demo4.db")
# cur=con.cursor()
# cur.execute("create table if not exists student1(id int, Name text,contact varchar)")
# cur.execute("insert into student1 values(?,?,?)",(1,'janni',1234567789))

# sunny=[(2,"jann2",1234567890),(3,"janni3",45959794847),(4,"janni4",47383944739)]
# cur.executemany("insert into student1 values(?,?,?)",sunny)

# '''add new column'''
# cur.execute("alter table student1 add column 'address'")

# '''add values to new column'''
# cur.execute("update student1 set address='nanded' ")

# demo=cur.execute("select * from student1")
# for row in demo:
#     # print(row)

#     ##OR
#     print(row[0],row[1])

# ####Fetchall()
# cur.execute("select * from student1")
# demo=cur.fetchall()
# print("Total Rows: ",len(demo))

# for row in demo:
# #     print(row)

#     ##OR
#     print(row[0],row[1])


# ####Fetchone()
# cur.execute("select * from student1")
# demo=cur.fetchone()
# print(demo)

# '''Add New Column'''
# cur.execute("alter table student1 add column 'newcity'")


# # '''Drop particular column'''
# cur.execute("alter table student1 drop column 'newcity' ")

# '''delete particular value'''
# cur.execute("UPDATE student1 SET contact = NULL WHERE id = 4")


# # '''delete data from table'''
# cur.execute("delete from student1 where id=4")

# '''drop table'''
# # cur.execute("drop table student1")
# con.rollback()


# con.commit()
# con.close()
    
# ##### OOPS #####
# ### Class and Object ###
# class car:
#     color="Red"
#     brand="BMW"
# car1=car()
# print(car1.color)
# print(car1.brand)


# ##### Constructor #####
# ##constructor
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

# s1=Student("janni",97)
# print(s1.name,s1.marks)

# s2=Student("Pravin_bhai",99)
# print(s2.name,s2.marks)


# ##task
# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account=acc

#     def get_balance(self):
#         return self.balance

#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs",amount,"was debited")
#         print("Total balance= ",self.get_balance())

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs",amount,"was credited")
#         print("total balance= ",self.get_balance())

    

# acc1=Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)

# #polymorphism
# class Dog:
#     def sound():
#         print("Dog barks")

# class Cat:
#     def sound():
#         print("Cat meows")

# d1=Dog
# c1=Cat

# d1.sound()
# c1.sound()


# class UPI:
#     def __init__(self,amount):
#         self.amount=amount

#     def payment(self):
#         print("payment by UPI: ",self.amount)

# class Card:
#     def __init__(self,amount):
#         self.amount=amount

#     def payment(self):
#         print("Payment by Card: ",self.amount)

# class Cash:
#     def __init__(self,amount):
#         self.amount=amount

#     def payment(self):
#         print("Payment by CAsh: ",self.amount)

# p1=UPI(400)
# p2=Card(200)
# p3=Cash(500)

# p1.payment()
# p2.payment()
# p3.payment()


# #inheritance
# class Parent():
#     def house(self):
#         print("parent house")

# class Child(Parent):
#     def bike(self):
#         print("child bike")

# c=Child()

# c.house()
# c.bike()


# class Parent():
#     def Display(self):
#         print("Parent Class")

# class Child(Parent):
#     def show(self):
#         print("child class")

# c=Child()
# c.Display()
# c.show()


    
# class Student:
#     def __init__(self):
#         print("Constructor called")

# s1=Student()


# class Student:
#     def __init__(self):
#         self.name = "janni"

# s1 = Student()
# print(s1.name)


# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print("Name of Student is: ",self.name)
#         print("Student Age: ",self.age)
#         print("Student Marks: ",self.marks)

# s1=Student("janni",24,98)
# s1.display()

# #Employee Details
# class Employee:
#     def __init__(self,name,salary,department):
#         self.name=name
#         self.salary=salary
#         self.department=department

#     def show_details(self):
#         print("Employee Name: ",self.name)
#         print("Employee Salary: ",self.salary)
#         print("Employee Department: ",self.department)

# e=Employee("Amit",30000,"IT")
# r=Employee("priya",40000,"Hr")
# e.show_details()
# print("")
# r.show_details()


# #Rectangle Area and Perimeter
# class Rectangle():
#     def __init__(self):
#         self.length=10
#         self.width=5

#     def area(self):
#         print("Area of Rectangle: ",self.length*self.width)

#     def perimeter(self):
#         print("Perimeter of Rectangle: ",2*(self.length+self.width))

# a1=Rectangle()
# a1.area()

# a2=Rectangle()
# a2.perimeter()


# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def talk(self):
#         print("student Name: ",self.name)
#         print("student age: ",self.age)
#         print("student marsk: ",self.marks)

# s1=Student("pravin",23,88)
# s2=Student("Arjun",23,76)
# s3=Student("shiv",23,90)
# s4=Student("gaurav",22,89)

# Student=[s1,s2,s3,s4]
# for i in Student:
#     print("")
#     i.talk()


# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def talk(self):
#         print("Student name: ",self.name)
#         print("Student age: ",self.age)
#         print("Student marks: ",self.marks)

# for i in range(3):
#     name=input("Enter Student Name: ")
#     age=int(input("Enter Student age: "))
#     marks=int(input("Enter Student Marks: "))

# s1=Student(name,age,marks)
# s1.talk()
# print("")


# #Employee details
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def display(self):
#         print("Student name: ",self.name)
#         print("Student age: ",self.age)
#         print("Student salary: ",self.salary)

# s1=Employee("pravin",24,40000)
# s1.display()

# print("")

# s2=Employee("Amit",28,30000)
# s2.display()
        
# #banck account
# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("Amount deposited: ",amount)

#     def withdraw(self,amount):
#         self.balance=self.balance - amount
#         print("Withdraw amount: ",amount)

#     def display(self):
#         print("Current balance:",self.balance)


# b=BankAccount("pravinkalale",1000)
# b.deposit(500)
# b.withdraw(200)
# b.display()


# #product details and discount
# class Product:
#     def __init__(self,product_name,price,quantity):
#         self.product_name=product_name
#         self.price=price
#         self.quality=quantity

#     def total_price(self):
#         total=self.price*self.quality
#         print("Total price: ",total)

#     def discount(self):
#         total=self.price*self.quality
#         discount=total*10/100
#         print("Discount: ",discount)
#         return discount

#     def final_price(self):
#         total=self.price*self.quality
#         discount=total*10/100
#         final=total-discount
#         print("Final Price: ",final)


# s1=Product("Laptop",50000,3)
# print("product Name: ",s1.product_name)
# s1.total_price()
# s1.discount()
# s1.final_price()


# class Mobile:
#     def __init__(self):
#         self.brand="Samsung"
#         self.model="S24"
#         self.price=75000

#     def display_details(self):
#         print("brand: ",self.brand)
#         print("model: ",self.model)
#         print("price: ",self.price)

# d=Mobile()
# d.display_details()



# class Mobile:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price

#     def display_details(self):
#         print("brand: ",self.brand)
#         print("model: ",self.model)
#         print("price: ",self.price)

# d=Mobile("Samsung","S24",75000)
# d.display_details()



# ##Constructor parameterized
# class Book:
#     def __init__(self,book,author,price):
#         self.book=book
#         self.author=author
#         self.price=price

#     def display(self):
#         print("Book Name: ",self.book)
#         print("Author: ",self.author)
#         print("price: ",self.price)

# d=Book("Python Basics","janni",450)
# d.display()
# print("")
# d1=Book("java programming","james",550)
# d1.display()



##### Inheritance Practice #####
##Single Inheritance
#one parent & one child
class Parent:
    def house(self):
        print("Parent Have House")

class Child(Parent):
    def bike(self):
        print("Child Have Bike")

c=Child()
c.house()
c.bike()


##Multiple Inheritance
#Two parent & one Child

class father:
    def house(self):
        print("Father Have House")

class Mother(father):
    def jwellary(self):
        print("Mother Have jwellary")

class child(Mother):
    def bike(self):
        print("child have Bike")

f=child()
f.house()
f.jwellary()
f.bike()


##Multi-levle Inheritance
#chain of inheritance
class grandparent():
    def farm(self):
        print("Grandparent have farm")

class parent(grandparent):
    def house(self):
        print("parent have House")

class uncle(parent):
    def car(self):
        print("Uncle Have Car")

class child(uncle):
    def bike(self):
        print("child have Lot's of Bikes")

c1=child()
c1.farm()
c1.house()
c1.car()
c1.bike()

print("")

## Hierarchical Inheritance
#One parent & Two Child
class parent:
    def house(self):
        print("parent have house")

class son(parent):
    def bike(self):
        print("son have bike")

class daughter(parent):
    def car(self):
        print("Daughter have Car")


s=son()
s.house()
s.bike()

d=daughter()
d.house()
d.car()    

print("")


##Hybrid Inheritance
#combine two or more type of inheritance
class Parent:
    def house(self):
        print("parent have House")

class Son(parent):
    def bike(self):
        print("Son have BMW bike")

class Daughter(parent):
    def car(self):
        print("Daughter have car")

class grandchild(Son, Daughter):
    def mobile(self):
        print("Grandchild have Mobiles")

g=grandchild()
g.house()
g.bike()
g.car()
g.mobile()


##Non-parameterized Constructor   
class Student:
    def __init__(self):
        print("Constructor called")

s=Student()



#python program to define
#abstract class
from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def speed(self):
        pass

class BMW(Car):
    def speed(self):
        print("BMW has 200 km/hr")

class Audi(Car):
    def speed(self):
        print("Audi has 220km/hr")

class Farrari(Car):
    def speed(self):
        print("Farrari has 250km/hr")

t=BMW()
t.BMW()

a=Audi()
a.Audi()

f=Farrari()
f.Farrari()




    
    
    
        


