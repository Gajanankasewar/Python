#method overriding
class Animal():
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d=Dog()
d.sound()

print("")


class Shape():
    def area(self):
        print("Calculating area")

class Circle(Shape):
    def area(self):
        print("Area of Circle")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")

c=Circle()
c.area()

r=Rectangle()
r.area()

class Employee():
    def work(self):
        print("employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

class Designer(Employee):
    def work(self):
        print("Designer is creating designs")

e=Employee()
e.work()

d=Developer()
d.work()

d1=Designer()
d1.work()


