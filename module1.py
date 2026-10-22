#palindrome
def pal(num):
    rev=0
    temp=num 
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print("Reverse Number: ",rev)

    if temp==rev:
        print("pallindrome Number")
    else:
        print("Not pallindrome")


##armstrong
def arm(number):
    sum=0
    temp=number
    while number>0:
        rem=number%10
        sum=sum+rem**3
        number=number//10
    print("Sum of Armstrong Number is: ",sum)

    if temp==sum:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")