#Non-parameterized function

def display():                  #fun defination
    print("hello World")        #fun body

display()                       #fun calling
display()
display()                       

def display():
    print("Pravin")
display()


#parameterized function
def add(a,b):       #parameter
    print(a+b)
add(10,20)    
add(100,200)      #arguments

#pallindrome

def para():
    num=int(input("Enter any Number: "))
    rev=0
    temp=num
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if temp==rev:

        print("pallindrome")
    else:
        print("not pallindrome")

para()



    