### arithmetic operator
a=10
b=34.5
#result=a+b
#print(result)
print("Addition:",a+b)
print("Substraction:",a-b)
print("multiplication:",a*b)
print("division: ",a/b)
print("floor",a//b)
print("exponential: ",a*b)
print("exponential: ",a**b)


### Relational operator
x=10
y=5
print("Equals to optr: ",x==y)
print("not equals to optr: ",x!=y)
print("less than optr: ",x<y)
print("greater than optr: ",x>y)
print("less than equal to optr: ",x<=y)
print("greater than equal to optr: ",x>=y)


###Logical operator

#and operatoer
a=10>5 and 10>8
print(a)

# #OR operator
b=10>5 or 10<7
print(b)

# #NOT operator
c=10!=7
c=10==5
print(c)

#task question
print(10 and 20)
print(-10 or -20)
print("" or "hi")
print("True" and "False")
print("-3" and 0)
print("_" or 12)
print("str" or "str1")
print("Hello" and "hello jii")
print(True or False)
print(True and False)


###Assignment operatoer/shorthand operator
x=10
x+=5
print(x)

x=10
x-=5
print(x)

x=10
x*=5
print(x)

x=10
x/=5
print(x)

x=10
print(x)

x=10
x%=5
print(x)

x=10
x**=5
print(x)

x=10
x//=5
print(x)


#Membership operator       // ' in ' number/string list madhye ahe ki nahi check krto
s=[1,2,3,4,5]
print(3 in s)
print('z' not in s)
print(33 in s) 

#identity operator
a=10
b=a
print(a is b)
print(a is not b)