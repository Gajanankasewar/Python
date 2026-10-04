#### If #####
#1)positive number
a=10
if(a>=0):
    print("positive number")

#2)user-input positive number
a=int(input("Enter any number: "))
if(a>=0):
    print("Positive number")    

#3)negative number
a=-5
if(a<0):
    print("negative number")

#4)voting eligibility
age=int(input("Enter Your Age: "))
if age>=18:
    print("Eligible for vote")


#5)Pass Student
marks=int(input("Enter Students Marks: "))
if marks>=35:
    print("Pass")


#6)Number divisible by 5
num=int(input("Enter any number: "))
if num%5==0:
    print("Divisible by 5")


#7)Temperature
temp=int(input("Enter Temperature: "))
if temp>=40:
    print("Temprature is to Hot")


#8)Salary check
salary=int(input("Enter Your Salary: "))
if salary>=50000:
    print("High Salary")

#9)Age check
age=int(input("Enter Your age: "))
if age>=60:
    print("Senior citizen")


#10)Password Length
password=(input("Enter Your Password: "))
if len(password)>=8:
    print("Strong Password")


##### if_else ######
#1)user input negative number

a=int(input("Enter any number"))
if(a<0):
    print("Positive Number")
else:
    print("Negative Number")


#2)even odd progrm
a=int(input("Enter any number: "))
if(a%2==0):
    print("Even number")
else:
    print("odd number")

#2)voting 
age=int(input("Enter any number: "))
if(age>=18):
    print("You are eligible for voting")
else:
    print("Not Eligible for Voting")

#3)pass or fail
result=int(input("Enter marks: "))
if(result>=35):
    print("pass")
else:
    print("Fail")


#4)Large number
a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
if(a>b):
    print("A is greater")
else:
    print("B is greater")    

#5) divisible by 5
a=int(input("enter any number: "))
if(a%2!=0):
    print(a is divisible)
else:
    print("A is not divisible by 5")


#6)authentication
password=int(input("Enter password: "))
if(password==1234):
    print("Login Successful")
else:
    print("login failed")


#7)temperature if-else
temp=int(input("Enter Today's temperature: "))
if(temp>40):
    print("Hot Temperature")
else:
    print("Normal Temperature")

#8)username
username=(input("ENter username: "))
if(username=="pass"):
    print("login successfull")
else:
    print("failed")


#9)greater than or equal to 10 or not
num=int(input("enter any number: "))
if(num>=10):
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")


#10)shopping free Delivery
amount=int(input("Enter Shopping Amount: "))
if amount>=1000:
    print("Free Delivery")
else:
    print("Delivery Charges Applicable")


#11)ATM PIN
pin=int(input("Enter Your PIN: "))
if pin==1234:
    print("ATM Acess Granted")
else:
    print("Incorrect PIN")






        
##### ELIF ######
#1)POSITIVE, NEGATIVE OR ZERO
num=int(input("Enter any Number: "))
if num>0:
    print("Positive Number")
elif num<0:
    print("Negative Number")
else:
    print("Zero")


#2)Grade
marks=int(input("Enter Student Marks: "))
if marks>=90 and marks<=100:
    print("A grade")
elif marks>=75 and marks<=89:
    print("B grade")
elif marks>=60 and marks<=74:
    print("C grade")
elif marks>=40 and marks<=59:
    print("D grade")
else:
    print("Fail")


#3)Age category
age=int(input("Enter Age: "))
if age>0 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior Citizen")


#4)Elictricity bill
units=int(input("Enter Electricity units: "))
if units>=0 and units<=100:
    print("Low Usage")
elif units>=101 and units<=300:
    print("Medium usage")
elif units>=301 and units<=500:
    print("High Usage")
else:
    print("Very High Usage")


#5)Number Divisibility
num=int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print("Divisible by 3 and 5")
elif num%3==0:
    print("Divisible by 3")
elif num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")


#6)Temperature Category
temp=int(input("Enter Today's Temperature: "))
if temp>=40:
    print("Very Hot Temperature: ")
elif temp>=30 and temp<=39:
    print("Hot")
elif temp>=20 and temp<=29:
    print("Normal")
elif temp>=10 and temp<=19:
    print("Cold")
else:
    print("Very Cold")


#7)Shopping Discount
amount=int(input("Enter Shopping Amount: "))
if amount>=5000:
    print("20% Discount")
elif amount>=3000 and amount<=4999:
    print("15% Dicount")
elif amount>=1000 and amount<=2999:
    print("10% Discount")
else:
    print("No Discount")


#8)Day number
num=int(input("Enter any number between 1 To 7: "))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Invalid Input")


#9)calculator operation
num1=int(input("Enter first number: "))
num2=int(input("Enter Second Number: "))
operation=input("choose operation: ")
if  operation=="+":
    print("Addition ",num1+num2)
elif operation=="-":
    print("Substraction ",num1-num2)
elif operation=="*":
    print("Multiplication: ",num1*num2)

elif operation=="/":
    print("Division: ",num1/num2)
else:
    print("invalid operation")


#10) Leap Year
year=int(input("Enter Year: "))
if year%400==0:
    print("Leap Year")
elif year%100==0:
    print("Not a Leap Year")
elif year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# student score distinction
marks=int(input("Enter student marks:" ))
if(marks>=75):
    print("First Class")
elif(marks>=50 and marks<75):
    print("Second class")
elif(marks>=35 and marks<50):
    print("C class")
else:
    print("Fail")






## Nested If ###

#1)positive/Negative  even/odd
num=int(input("Enter any Number: "))
if(num>=0):
    print("Positive Number")
    if(num%2==0):
        print("Even number")
    else:
        print("odd number")
elif num<0:
    print("Negative number")
    if num%2==0:
        print("Even Number")
    else:
        print("odd number")
else:
    print("zero")

      
#2)Age & Driving License
age=int(input("Enter Your Age: "))
if age>=18:
    license=input("Do you Have License? Yes/No:")
    if license=="Yes":
        print("You are eligible to drive and you have driving license")
    else:
        print("you are  eligible to drive but you dont have driving license")
else:
    print("You are not eligible to drive")


#3)Student pass or fail & grade
marks=int(input("Enter Student's Marks "))
if marks>=35:
    print("Student Pass")
    if marks>=75:
        print("A grade")
    elif marks>=60 and marks<75:
        print("B grade")
    else:
            print("C grade")
else:
    print("Student Fail")



#4)ATM Withdrawal
balance=int(input("Enter Your Account Balance: "))
amount=int(input("Enter Withdrawn Amount: "))
if amount<=balance:
    print("Balance Is sufficient")

    if amount%100==0:
     print("withdrawn Successfull")
    else:
        print("Amount must be a multiple of 100")
else:
   print("Insufficent balance")


#5)username & password
username=input("Enter Your Username: ")
password=input("Enter Your Password: ")
if username=="pass":
    if password=="pass@123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


#6)Exam Eligibility
attendance=int(input("Enter your Attendance: "))
marks=int(input("Enter Your Marks: "))
if attendance>=75:
    if marks>=40:
        print("Eligible and Passed")
    else:
        print("Eligible but Failed")
else:
    print("Not Eligible")


#7)shopping Discount
amount=int(input("Enter Amount: "))

if amount>=2000:
    customer=input("Do you are having our Membership Yes/No: ")
    if customer=="Yes":
        print("20% Discount")
    else:
        print("10% Discount")
else:
    print("No Discount")


#8)Mobile Recharge
balance=int(input("Enter Your Balance: "))
amount=int(input("Enter Recharge Amount: "))
if amount<=balance:
    if amount>=100:
        print("Recharge Successful")
    else:
        print("Minimum Recharge is 100")
else:
    print("Insufficient Balance")


#9)College Admission
marks=int(input("Enter Studets Marks: "))
age=int(input("Enter Students Age: "))

if marks>=50:
    if age>=18:
        print("Eligible for Admission")
    else:
        print("Age requirement not met")
else:
    print("marks requirement not met")


#10)online shopping payment
amount=int(input("Enter Order Amount: "))
status=(input("payment done? Yes/No: "))

if amount>=1000:
    if status=="Yes":
        print("Order Confirmed")
    else:
        print("payment Pending")
else:
    print("minimum Order Amount Not Met")


#11) movie Ticket
age=int(input("Enter Your Age: "))
if age>=18:
    id=input("Do You have Id card Yes/No: ")
    if id=="Yes":
        print("Booking Allowed")
    else:
        print("ID Required")
else:
    print("Not Eligible")


#12)Student result + scholership
marks=int(input("Enter Your marks: "))
if marks>=75:
    income=int(input("Enter Your Parent's Income: "))
    if income<=50000:
        print("Eligible for Scholorship")
    else:
        print("income is to high")
else:
    print("Marks is to low")