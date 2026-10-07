#len()method
tup=(99,2,3,4,5,6,7,4,9,3)
print(len(tup))    #Returns the number of element present in tuple.

#min()
tup1=(10,100,54,78,45,5,91)
print(min(tup1))

#max()
tup2=(10,45,100,25,79)
print(max(tup2))

#sum() method
tup3=(99,2,3,4,5,6,78)
print(sum(tup3))

#count() 
tup4=(10,25,26,25,4,25,78,25)
print(tup4.count(25))               #count the similar elements

#index()
tup5=(10,20,40,100,25,78)
print(tup5.index(20))               #find the index Number of an element

##reversed()
#1st way to reveresed tuple
tup6=(20,40,25,10,5,4,1,30)
print(tuple(reversed(tup6)))

#2nd way to reverese the tuple
tupp=(40,20,60,20)
print(*reversed(tupp))

##sorted()
#1st method to sort element
tup7=(40,20,10,50,25)
y=tuple(sorted(tup7))
print(y)

#2nd method to sorted element
tup8=(30,10,40,20)
print(sorted(tup8))

#slice
t=(10,20,30,40,50)
print(t[1:3])


tuple=(10,20,True,"Hi",30.5,3+5j)
print(tuple[2])
print(tuple[5])

print(tuple[1:4])   #end-1
print(tuple[0:5:2])


