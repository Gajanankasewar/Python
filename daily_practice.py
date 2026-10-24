# #find the number greater than 10
numbers = [12, 7, 15, 4, 9, 20, 3]
count=0
for n in numbers:
    if n>10:
        count+=1
print(count)


# #largest number between list
numbers = [4, 7, 2, 9, 6, 3]
largest=0
for i in numbers:
    if i>largest:
        largest=i
print(largest)


#find second-largest
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



# #file handling practice
#write
import os
f=open("demo1.txt","w")
f.write("Hi hello Godd Morning bro\n")
f.close

# #read
import os
f=open("demo1.txt","r")
print(f.read())
f.close()

# #append
f=open("demo1.txt","a")
f.write("Today is 23rd October")
f.close()

# #readline
f=open("demo1.txt","r")
print(f.readline())
print(f.readline())

# #readlines
f=open("demo1.txt","r")
print(f.readlines())
f.close()

# #Create new file using X if exist give's error
f=open("demo1.txt","x")

# #with statement
with open("demo1.txt","r") as f:
    print(f.read())




# ###creating and removing file 
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

# #remove file if exist other wise gives print statement
import os
if os.path.exists("document2.txt"):
    os.remove("document2.txt")
else:
    print("file not exists")


##numpy
import numpy
arr=numpy.array([1,2,4,5,6])
print(arr)

#2d array
import numpy
arr=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

# #multidimensionaly array
import numpy
arr=numpy.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)

import numpy
arr=numpy.array([1,2,3,4])
print(arr.dtype)

import numpy
arr1=numpy.array([43.2,54.7])
print(arr1.dtype)

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)


##Comparison in numpy
import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])

print("original Number")
print(x)
print(y)

# #greater than
print("greater than")
print(np.greater(x,y))

# #greater than equal
print("greater than equal")
print(np.greater_equal(x,y))

# #less than
print("less than")
print(np.less(x,y))

# #less than equal
print("less than equal to")
print(np.less_equal(x,y))

#Conversion
import numpy as np
arr=np.array([11,22,33,44,55,66,77,88,99,10,20,30])
a=arr.reshape(3,4)
print(a)

# #multideminsional
aa=arr.reshape(2,3,2)
print(aa)

# #print directly
print(arr.reshape(3,4))

#print directly multi-dimensional
print(arr.reshape(3,2,2))


##print each element in arr
for x in arr:
    print(x)

import numpy as np
arr=np.array([[1,2,3],[1,2,3],[1,2,3]])
for i in arr:
    print(i)

for i in np.nditer(arr):
    print(i)

#find index
a=np.array([1,2,3,4,5,4,4])
a=np.where(a==4)
print(a)

#print 1-D array elements
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,0])
for i in arr:
    print(i)


#print 2-d array element using for loop
import numpy as np
a=np.array([[11,22,33,44,55,66],[77,88,99,10,11,12]])
for x in a:
    for y in x:
        print(y)


#print 3-d array elements using for loop
import numpy as np
arr1=np.array([[[1,2,3],
                [1,2,3],
                [1,2,3]]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)


import numpy
a=numpy.array([32,55,67,39,69,77,76,94,88,22])
b=numpy.where(a%2==0)
print(b)

print(numpy.sort(a[b]))

