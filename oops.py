#parameterized constructor
class Student:
    def __init__(self,name,age,marks):
        self.name=name     #instance varible
        self.age=age
        self.marks=marks

    def talk(self):  #instance method
        print("Hello My name is: ",self.name)
        print("My Age is: ",self.age)
        print("My marks are: ",self.marks)

s1=Student("janni",24,98)
s1.talk()


