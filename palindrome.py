##palindrome
num=int(input("Enter Any Number: "))
rev=0
temp=num

while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("reverse Number is: ",rev)
if temp==rev:
    print("given Number is pallindrome")
else:
    print("Given Number is Not pallindrome")