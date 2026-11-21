'''collection of character enclosed by single , dobule and triple quotes '''

# #double quotes
str1="python"

# #single quotes
str2='janni'

# #Triple qutoes
str3='''This is 
myltiline 
python string
'''

print(str1)
print(str2)
print(str3)


str4="Gajuu"
print(str4[:4])

# #find the character by its index
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


# #slicing in string

str="Hello World"
print(str[1:4])
print(str[4:8])
print(str[7:])
print(str[3:7])

print(str[0:7:3])
print(str[6:10:3])
print(str[6: :4])
print(str[4:10:5])



# #capitalize ()
str="hello world"
str2=str.capitalize()

# #if we want every world first letter capital
str2=str.title()

# print(str2)
print(id(str))
print(id(str2))

# ## isupper ##
str="WELCOME"
str2=str.isupper()
str3=str.lower()
print(str2)  #return value (true or false)
print(str3)  #convert a string

# # lower to upper case
str3="gajanan"
str4=str3.upper()
print(str4)

# #capitalize
str="welcome"
str2=str.capitalize()
print(str2)

# #islower()
str="welcome"
str2=str.islower()
print(str2)

# #isupper()
str="WELCOME"
str2=str.isupper()
print(str2)

# #len()
str="welcome"
print(len(str))

#replace()
str1="java is a programming language"
str2=str1.replace("java","python")
print(str2)

#join
str=""
list=['h','e','l','l','o']
str2=str.join(list)
print(str2)

##index
str="Welcome"
str2=str.index("c")
print(str2)

#rfind   '''last wala same character find krto
str="communication"
str2=str.rfind("c")
print(str2)

# #index
str="Welcome to the python"
str2=str.index("p",14,17)
print(str2)

# #find   '''if character not found it gives -1'''
str="communcication"
str2=str.find("z")
print(str2)

# #partition()
str="python is a programming language"
str2=str.partition("is")
print(str2)

#split()
str="python is a programming language"
str2=str.split()
print(str2)

#count              '''same element kiti vela aala te count krte
str="Hello welcome"
str2=str.count('e')
print("occurences",str2)

# #count-r
txt="I love apples, aaple is my favorite fruit"
x=txt.count("are",10,24)
print(x)



#Count  the number of vowels in given string
s="programming"
count=0
for ch in s:
    if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print(count)

#pallindrome using string 
l="racecar"
reverse=""
for i in l:
    reverse=i+reverse
if reverse==l:
    print("pallindrome")
else:
    print("not pallindrome")


##count using built in method
# s="python is programming language"
# print(s.count(" "))

# st="programming language"
# print(st.count("a"))





##using programming logic
#1)count white spaces
s = "hello world python"
count = 0
for i in s:
    if i == " ":
        count += 1
print(count)

#2)find particular character
q="programming language"
count=0
for i in q:
    if i=="a":
        count+=1
print(count)


#3)find vowels
s="programming"
for ch in s:
    if ch=='a' or ch=='e' or ch=='o' or ch=='e' or ch=='u':
        print(ch)


#4)count vowels
vowel="developer"
count=0
for ch in vowel:
    if ch=='a' or ch=='e'or ch=='i'or ch=='o' or ch=='u':
        count+=1
print(count)

#5)pallindrome using another method
str1="mom"
str2=str1[: :-1]
if str1 == str2:
    print(" string is pallindrome")
else:
    print("string is not pallindrome")


#6)Reverse character
str="python"
reverse=""
for ch in str:
    reverse=ch+reverse
print(reverse)

#or 
# string="python"
# for i in string:
#     print(string[::-1])

#7)reverse word
name = "Hello How Are You"
word = ""
result = ""

for ch in name:
    if ch != " ":
        word = word+ch
    else:
        result = word+" " +result
        word = ""
result = word + " " + result
print(result)

#8)krishna
word="krishna"
count=0
for ch in word:
   count+=1
   if count<len(word):
      print(ch,"|",end="",sep="")
   else:
      print(ch)

#OR
#KRISHANA
name="KRISHNA"
for ch in range(len(name)):
    print(name[ch],end="")
    if ch<len(name)-1:
        print("|",end="")


#9)character frequency
word="programming"
for ch in word:
   count=0

   for i in word:
      if ch==i:
         count+=1
   print(ch,"=",count)

#10)positive or negative indexing
word = "python"
for i in range(len(word)):
    print(word[i], "Positive:", i, "Negative:", i - len(word))

#11)lower to Upper case
name="hello"
for i in name:
    new=chr(ord(i)-32)
    print(new,end="")

print("")

#12)upper to lower case
l="HELLO"
for i in l:
    print(chr(ord(i)+32),end="")

#13)Anagram
str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagram")
else:
    for i in str1:
        if str1.count(i) != str2.count(i):
            print("Not Anagram")
            break
    else:
        print("Anagram")



#find out string's askey value
str10="python"
for i in str10:
    print(ord(i))

    

