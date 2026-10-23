#find the number greater than 10
numbers = [12, 7, 15, 4, 9, 20, 3]
count=0
for n in numbers:
    if n>10:
        count+=1
print(count)


#largest number between list
numbers = [4, 7, 2, 9, 6, 3]
largest=0
for i in numbers:
    if i>largest:
        largest=i
print(largest)


numbers = [4, 7, 2, 9, 6, 3]
largest=0
seclarge=0
for i in numbers:
    if i>largest:
        seclarge=seclarge
        largest=i
for j in numbers:
    if j>largest and seclarge<largest:
        seclarge=j
print(seclarge)



#file handling practice
#write
import os
f=open("demo1.txt","w")
f.write("Hi hello Godd Morning bro\n")
f.close

#read
import os
f=open("demo1.txt","r")
print(f.read())
f.close()

#append
f=open("demo1.txt","a")
f.write("Today is 23rd October")
f.close()

#readline
f=open("demo1.txt","r")
print(f.readline())
print(f.readline())

#readlines
f=open("demo1.txt","r")
print(f.readlines())
f.close()

#Create new file using X if exist give's error
f=open("demo1.txt","x")

#with statement
with open("demo1.txt","r") as f:
    print(f.read())




###creating and removing file 
import os
f=open("document2.txt","w")
f.write("hello janni")
f.close

import os
f=open("document2.txt","r")
print(f.read())
f.close()

import os
f=open("document2.txt","w")
f.write("Now i'am practicing on File handling in python\n")

import os
f=open("document2.txt","a")
f.write("This is append")

#remove file if exist other wise gives print statement
import os
if os.path.exists("document2.txt"):
    os.remove("document2.txt")
else:
    print("file not exists")




