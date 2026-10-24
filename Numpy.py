#without using As
import numpy
arr=numpy.array([1,2,3,4,5])
print(arr)

#with Using AS
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)


#Arrays
import numpy as np
arr1=np.array(42)
arr2=np.array([1,2,3,4,5])
arr3= np.array([[1, 2, 3],[4, 5, 6]])
arr4=np.array([[[1,2],[3,4],[5,6]]])
print(arr4)


Check type of data
import numpy as np
arr1=np.array([1,2,3,4])
arr=np.array([1.2,2.45,3.45,4.33])
print(arr1.dtype)
print(arr.dtype)


Comparison between Two numbers
import numpy as np 
x = np.array([3, 5])
y = np.array([2, 5]) 
print("Original numbers:")
print(x)
print(y) 

#greater Number
print("Comparison - greater") 
print(np.greater(x, y)) 

#greater than or equal number
print("Comparison - greater_equal") 
print(np.greater_equal(x, y)) 

#less than
print("Comparison - less") 
print(np.less(x, y)) 

#less than equal
print("Comparison - less_equal") 
print(np.less_equal(x, y))


#conversion of one array to other
import numpy as np
a=np.array([11,22,33,44,55,66,77,88,99,10,11,12])
na=a.reshape(4,3) #4 rows, 3-columns
print(na)

naa=a.reshape(2,2,3)   # 2-block, 2-rows, 3-columns
print(naa)

for x in a: #for 1-D array
    print(x)




import numpy as np
a=np.array([[1,2,3],[1,2,3],[1,2,3]])

#access 1-D array
for i in a:
    print(i)

#access n-dimension of array
for i in np.nditer(a):
    print(i)


#search element
a=np.array([1,2,3,4,5,4,4])
n=np.where(a==4)
print(n)


#where method
import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
x=np.where(a%2==0)  #(array([1,3,5,7])) return index of even number
print(x)

print(np.sort(a))   #[1 2 3 4 5 6 7 8]
