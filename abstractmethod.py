#Abstract class method
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print("Paid using UPI",amount)

class CreditCard(Payment):
    def pay(self,amount):
        print("Paid using Credit Card: ",amount)

class NetBanking(Payment):
    def pay(self,amount):
        print("paid using netbanking",amount)

u=UPI()
u.pay(500)

c=CreditCard()
c.pay(1000)

N=NetBanking()
N.pay(2000)


# #practice question Abstractmethod
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

d=Dog()
d.sound()


###practice question

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Starts")

class Bike(Vehicle):
    def start(self):
        print("Bike Start")

c=Car()
c.start()

b=Bike()
b.start()


# ###Abstract method with Parameters
from abc import ABC, abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

class Addition(Calculator):
    def add(self,a,b):
        print("Addition of a & b is: ",a+b)

a=Addition()
a.add(10,20)



#### Abstract Method – Area Calculation ####
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self,length,width):
        print("area of Rectangle is: ",length*width)

class Square(Shape):
    def area(self,side):
        print("Area of Square is: ",side*side)

r=Rectangle()
r.area(10,5)

s=Square()
s.area(4)


#### Abstract Method – Calculate Salary ####
from abc import ABC , abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 30000

class Part_timeEmployee(Employee):
    def calculate_salary(self):
        return 15000

f=FullTimeEmployee()
result1=f.calculate_salary()
print("Full time salary is : ",result1)

f=Part_timeEmployee()
result2=f.calculate_salary()
print("Part time employee salary is: ",result2)






