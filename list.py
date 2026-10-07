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


list1=[1,2,3]
list2=[4,5,6]
print(list1+list2)    #concatnation
print(list1*4)        #Repetation

l=[10,20,"Hi",3+5j]
l=tuple
print(l)


#Tuple
tup=(10,20,True,"Hi",30.5,3+5j)
print(tup[2])
print(tup[5])

print(tup[1:4])   #end-1
print(tup[0:5:2])


#Addition of list elements
list = [1,2,3,4]
sum = 0
for i in list:
    sum = sum + i
print(sum)

#Dictionary
d={}
print(type(d))

##set
s=set()                 #empty set
print(type(s))     

my_dict={1:10,2:55.5, 3:'x', 4:True, 5:[1,2,3], 6:"hi",7:10}
print(my_dict)
print(my_dict[1])
print(my_dict[4])
print(my_dict.keys())           #To access keys in dictionary
print(my_dict.values())         #To access values in dictionary



my_dict=dict({1:10, 2:55.5, 3:'x', 4:True, 5:[1,2,3], 6:"hi", 7:10})


mydict={
    "Id":101,
    "name":"Merry",
    "Age":19
}
i=mydict.items()
print(i)
print(mydict["Id"])


mydict={
    "Id":101,
    "name":"Mery",
    "Age":19
}
mydict.setdefault("City","Pune")
print(mydict)

mydict["City"]="mumbai"
print(mydict)



##set
s={3,6,2,8,4,7,4,9,3}
print(s)
s.add(99)
print(s)
s.remove(4)
print(s)

##Update
a={"lotus","rose","lily"}
b={"Python","java","DSA"}
a.update(b)
print(a)

