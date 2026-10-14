'''collection of character enclosed by single , dobule and triple quotes '''

#double quotes
str1="python"

#single quotes
str2='janni'

#Triple qutoes
str3='''This is 
myltiline 
python string
'''

print(str1)
print(str2)
print(str3)


str4="Gajuu"
print(str4[:4])

#find the character by its index
str="Hello World"
print(str[1])
print(str[4])
print(str[7])
print(str[10])
print(str[2])

print(str[-3])
print(str[-4])
print(str[-10])
print(str[-5])
print(str[-11])


#slicing in string

str="Hello World"
print(str[1:4])
print(str[4:8])
print(str[7:])
print(str[3:7])

print(str[0:7:3])
print(str[6:10:3])
print(str[6: :4])
print(str[4:10:5])



#capitalize ()
str="hello world"
str2=str.capitalize()

#if we want every world first letter capital
str2=str.title()

print(str2)
print(id(str))
print(id(str2))

## isupper ##
str="WELCOME"
str2=str.isupper()
str3=str.lower()
print(str2)  #return value (true or false)
print(str3)  #convert a string

# lower to upper case
str3="gajanan"
str4=str3.upper()
print(str4)

