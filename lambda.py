###LAMBDA function
#syntax:
'''lambda arguments : expression'''

#addition
sum=lambda x,y:x+y
print(sum(10,20))

#square of number
square=lambda x:x*x
print(square(4))

#cube of number
cube=lambda a:a*a*a
print(cube(3))

#largest number
largest=lambda a,b:a if a>b else b
print(largest(6,2))

#positive negative number
positive=lambda num:"positive" if num>0 else "negative"
print(positive(-1))


#1)even-odd
even_odd=lambda a:"Even" if a%2==0 else "Odd"
print(even_odd(4))
print(even_odd(5))
print(even_odd(7))

#2)largest of three numbers
largest=lambda a,b,c:"a is greater" if a>b and a>c else "b is greater" if b>a and b>c else "c is greater"
print(largest(10,50,3))
print(largest(10,20,30))

#3)voting
vote=lambda age:"eligible for voting" if age>=18 else "Not eligible for vote"
print(vote(18))

#4)Authentication
username=input("Enter your username: ")
password=input("Enter your Password: ")
log=lambda username,password:"Login Successful" if username=="pass" and password=="1234" else "Invalid Credentials"
print(log(username,password))


#2nd way
log2=lambda username,password:"login success" if username=="gaju" and password=="123" else "invalid credential"
print(log2("pass","123"))
print(log2("gaju","123"))


#5)leap year
leap=lambda year:"leap year" if year%4==0 else "Regular year"
print(leap(2026))
print(leap(2012))

#6)profit loss
profit=lambda cash:"profit earn" if cash>25000 else "loss"
print(profit(200000))

#7)age category
category=lambda age:"teenager" if age>0 and age<18 else "young age" if age>=18 and age<30 else "adult"
print(category(12))
print(category(25))
print(category(40))
print(category(29))

#8)pass fail
result=lambda marks:"A+ grade" if marks>=90 and marks<=100 else "B+ grade" if marks>=75 and marks<90 else "c+ grade" if marks>=35 and marks<75 else "fail"
print(result(55))
print(result(91))
print(result(76))

#9)length of string
length=lambda password:"Valid Password" if len(password)>6 else "invalid password"
print(length("Gajanan"))
print(length("janni"))

#10)divisible by 5 
div=lambda a:"divisible by 5" if a%5==0 else "Not divisible by 5"
print(div(10))
print(div(2))

#2nd way
leap = lambda year: "Leap Year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not a Leap Year"

print(leap(2026))
print(leap(2012))
print(leap(1900))
print(leap(2000))

#11)vowel or consonent
vowel=lambda a:"vowels" if a in "aeiou" else "consonent"
print(vowel('a'))


#square
num=lambda a:a*a 
print(num(7))

#fine out even number using filter function
num=[1,2,4,5,6,7,8,9,10,11,12,13,14,15]
result=list(filter(lambda a:a%2==0,num))
print(result)

#fine out odd number using filter function
num=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda a:a%2!=0,num))
print(result)

#another way
num=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda n:n%2==0,num)
print(result)



