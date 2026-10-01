#Print 1 To 10 Numbers
for i in range(1,11):
    print(i)

#Print Name 1 to 5 times
for i in range(1,6):
    print("Gajanan")

#print square from 1 To 10
for i in range(1,11):
    print(i*i)

# print cube from 1 to 10
for s in range(1,11):
    print(s*s*s)

#print odd no. betwn 1 to 10
for o in range(1,11):
    if o%2 !=0:
        print(o)


#sum of 1 to 10 numbers
sum=0
for i in range(1,11):
    sum=sum+ i
print(sum)

even no.& thier sum
sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
        sum = sum + i

print("Sum =", sum)

#odd no. & thier sum
sum=0
for i in range(1,11):
    if i%2!=0:
        print(i)
        sum=sum+i
print("Sum=",sum)

#print any Table
num=int(input("Enter any number: "))
for i in range(1,11):
    print("Table:",num*i)



## While Loop ###
#1)print 1 to 10
i=1
while(i<=10):
    print(i)
    i+=1

#2)print reverse 1 to 10
i=10
while(i>=1):
    print(i)
    i-=1

3)Reverse The Number
num=int(input("Enter any Number: "))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10   # '//' floor division
print(rev)

#4)square numbers
i=2
while(i<=10):
    print(i*i)
    i+=1

#5)cube 1 to 10
i=2
while(i<=10):
    print("cube is: ",i*i*i)
    i+=1
    

#6)Even number
i=1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
        
       
#7)Odd Number
i=1
while(i<=20):
    if i%2!=0:
        print(i)
    i+=1

#8)sum of 1 to 10 even numbers
sum=0
i=1
while(i<=10):
    if i%2==0:
        sum=sum+i
    i+=1
print(sum)
    

#9)sum of 1 to 10 odd numbers
sum=0
i=1
while i<=10:
    if i%2!=0:
        sum=sum+i
    i+=1
print(sum)

   #even no.& thier sum
sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum = sum + i
print(sum)
        