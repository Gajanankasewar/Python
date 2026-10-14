#factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


'''same funtion same function la call krto'''

''' ADVANTAGE

code optimization
    save time
    save memory
    improve performance
'''

#1 to 5 numbers
def janni(n):
    if n==6:
        return
    print(n)
    janni(n+1)

janni(1)

#sum of 5 natural numbers
def natural(n):
    if n==1:
        return 1
    else:
        return n+natural(n-1)

print(natural(5))

#user input factorial program
num=int(input("Enter any number: "))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(num))




