#display list elements
l=[10,20.5,"hello",True,3+5j]
print(l)                #display element
print(l[2])             #display element at index 2
print(l[-4])            #display element on index no. -4
print(type(l))         #display the type of value
print(id(l))          #display the address


#Nested List
l=[10,20.5,"hello",[10,20,30],["Virat","Rohit"],True,3+5j]
print(l[3][1])
print(l[4][0][0])
print(l[4][1][0])  


#slicing
a=[10,20,30,40,50,60]
print(a[: : 2])
#reverse the string
print(a[: : -1])

#length of list
list=[1,2,3,4,5]
print(len(list))