#write()

f=open("demo.txt","w")
f.write("Hello My Name Is Gajanan")
f.close()

#perfrom file operations
file=open("demo.txt","r")
print("File_name",file.name)
print("readable_mode",file.readable())
print("writable_mode",file.writable())
print("File_closed",file.close())
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

#readline
import os
f=open("demo.txt","r")
print(f.readline())

#print 2 line using readline
import os
f=open("demo.txt","r")
print(f.readline())
print(f.readline())

#creating new file using X
import os
f=open("demo1.txt","x")

#delete a file
import os
os.remove("demo.txt")

#remove file if exist
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("The file does not exist")

#write file
f=open("demo.txt","w")
f.write("Hello My Name Is Gajanan")
f.close()


#with statement
with open("demo.txt","r")as f:
    content=f.read();
    print(content)


    





