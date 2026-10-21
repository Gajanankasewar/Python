f=open("demo.txt","w")
f.write("Hello My Name Is Gajanan")
f.close()

file=open("demo.txt","r")
print("File_name",file.name)
print("readable_mode",file.readable())
print("writable_mode",file.writable())
print("File_closed",file.writable())
file.close()

#read
f=open("demo.txt","r")
print(f.read())
f.close()

#write   '''wirte data into file using w mode, but existing data will be remove automatically'''
f=open("demo.txt","w")
f.write("Hello How are You\n")
f.close()

print("")

#append    '''write data into file using append method but existing data
f=open("demo.txt","a")
f.write("I am from Nanded") 
f.close()

import os
f=open("demo.txt","r")
print(f.readline())

import os
f=open("demo.txt","r")
print(f.readline())
print(f.readline())


import os
f=open("demo1.txt","x")





