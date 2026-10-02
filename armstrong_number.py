#armstrong no.
num=int(input("Enter any number: "))
sum=0
# rev=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
print("Reverse Number Is: ",sum)

if temp==sum:
    print("Given Number is Armstrong Number: ")
else:
    print("Given Number is Not Armstrong Number ")


