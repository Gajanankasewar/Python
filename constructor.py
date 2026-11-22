class Mobile():
    def __init__(self):
        print("Mobile object created")
m1=Mobile()


##constructor
class Laptop():
    def __init__(self):
        self.brand="Lenovo"
        self.price="50000"
        
l1=Laptop()
print(l1.brand)
print(l1.price)


###Passing parameter to a constructor
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
emp1=Employee("Rahul",30000)
emp2=Employee("Priya",45000)

print(emp1.name,emp1.salary)
print(emp2.name,emp2.salary)


class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

n1=Student("Amit",85)
n2=Student("Sneha",92)

print(n1.name,n1.marks)
print(n2.name,n2.marks)

print(" ")

###create a class named Bank
class Bank():
    bank_name="SBI"
    def __init__(self,account_holder,balacne):
        self.account_holder=account_holder
        self.balacne=balacne

Account1=Bank("Rahul",5000)
Account2=Bank("janni",100000)

print(Account1.account_holder,Account1.balacne,Account1.bank_name)
print(Account2.account_holder,Account2.balacne,Account2.bank_name)



###display Student Details using Instance Method
class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display_details(self):
        print("Student Name: ",self.name)
        print("Student Marks: ",self.marks)

s1=Student("Amit",85)
s2=Student("Priya",92)

s1.display_details()
print("")
s2.display_details()


#### Calculate Employee Annual Salary Using Instance Method
class Employee():
    def __init__(self,name,monthly_salary):
        self.name=name
        self.monthly_salary=monthly_salary

    def calculate_annual_salary(self):
        annual_salary=self.monthly_salary*12

        
        print("Name: ",self.name)
        print("Annual salary: ",annual_salary)

d1=Employee("Rahul",30000)
d2=Employee("Priya",45000)

d1.calculate_annual_salary()
d2.calculate_annual_salary()


        