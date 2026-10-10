# #display list elements
# l=[10,20.5,"hello",True,3+5j]
# print(l)                #display element
# print(l[2])             #display element at index 2
# print(l[-4])            #display element on index no. -4
# print(type(l))         #display the type of value
# print(id(l))          #display the address


# #Nested List
# l=[10,20.5,"hello",[10,20,30],["Virat","Rohit"],True,3+5j]
# print(l[3][1])
# print(l[4][0][0])
# print(l[4][1][0])  


# #slicing
# a=[10,20,30,40,50,60]
# print(a[: : 2])
# #reverse the string
# print(a[: : -1])

# #length of list
# list=[1,2,3,4,5]
# print(len(list))


# list1=[1,2,3]
# list2=[4,5,6]
# print(list1+list2)    #concatnation
# print(list1*4)        #Repetation

# l=[10,20,"Hi",3+5j]
# l=tuple
# print(l)


# #Tuple
# tup=(10,20,True,"Hi",30.5,3+5j)
# print(tup[2])
# print(tup[5])

# print(tup[1:4])   #end-1
# print(tup[0:5:2])


# #Addition of list elements
# list = [1,2,3,4]
# sum = 0
# for i in list:
#     sum = sum + i
# print(sum)

# #Dictionary
# d={}
# print(type(d))

# ##set
# s=set()                 #empty set
# print(type(s))     

# my_dict={1:10,2:55.5, 3:'x', 4:True, 5:[1,2,3], 6:"hi",7:10}
# print(my_dict)
# print(my_dict[1])
# print(my_dict[4])
# print(my_dict.keys())           #To access keys in dictionary
# print(my_dict.values())         #To access values in dictionary



# my_dict=dict({1:10, 2:55.5, 3:'x', 4:True, 5:[1,2,3], 6:"hi", 7:10})


# mydict={
#     "Id":101,
#     "name":"Merry",
#     "Age":19
# }
# i=mydict.items()
# print(i)
# print(mydict["Id"])


# mydict={
#     "Id":101,
#     "name":"Mery",
#     "Age":19
# }
# mydict.setdefault("City","Pune")
# print(mydict)

# mydict["City"]="mumbai"
# print(mydict)



# ##set
# s={3,6,2,8,4,7,4,9,3}
# print(s)
# s.add(99)
# print(s)
# s.remove(4)
# print(s)

# ##Update
# a={"lotus","rose","lily"}
# b={"Python","java","DSA"}
# a.update(b)
# print(a)



s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

print(s1.symmetric_difference(s2))


# a={"lotus","rose","lily"}
# b={"lily"}
# print(b.issubset(a))

#intersection_update   similar data 
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)


#count similar elements
numbers=[10,20,10,30,10,40]
print(numbers.count(10))

#index (find out index number)
print(numbers.index(30))
print(numbers.index(40))
print(numbers.index(10,1))

#sort (ascending)
marks=[45,12,89,34,67,23]
marks.sort()
print(marks)
#descending
marks.sort(reverse=True)
print(marks)

#reverse
values=[10,20,30,40,50]
values.reverse()
print(values)

#copy
items=[10,20,30,40,50]
new_items=items.copy()
print(items)

#extendex add more than 1 values at the end
a=[10,20,30]
a.extend({40,50,60})
print(a)

#length
cities=["Pune","Nanded","Mumbai","Delhi","Nagpur"]
print(len(cities))

#max,min,sum
prices=[120,450,80,300,250]
print(max(prices))
print(min(prices))
print(sum(prices))


#sorted
scores=[45,12,89,34,67]
print(sorted(scores))

print(sorted(scores,reverse=True))


#in operator
colors=["red","blue","green","yellow"]
print("blue" in colors)
print("green" in colors)
print("purple"in colors)
print("red" in colors)
#not in
print("purple" not in colors)


#tuple to list conversion
numbers=(10,20,30,40,50)
print(type(numbers))
my_list=list(numbers)
print(my_list)
print(type(my_list))

#delete fun
animal=["cat","dog","lion","tiger","horse"]
del(animal[2])
del(animal[3])
del(animal[1])
print(animal)

#delete using slicing
num1=[10,20,30,40,50,60]
del(num1[1:3])
print(num1)

#pop
p=[1,2,3,4,5]
x=p.pop(1)
print(x)
print(p)

##pop simple method
p1=[1,2,3,5,6]
print(p1.pop(3))
print(p1)


#List concatnation
first=[10,20,30]
second=[40,50,60]
total=first+second
print(total)

#List Repetition(*)
digits=[1,2,3]
print(digits*3)

values=[5,10]
new_val=values*4
print(new_val)


##Nested-list
mark=[[45,60],[70,85],[90,95]]
print(mark[1][1])


students = [["Amit", 80], ["Rahul", 90], ["Sneha", 85]]
print(students[2][0])

#value change
products = [["Pen", 10], ["Book", 50], ["Bag", 500]]
products[1][1]=60
print(products)

#nested-append
teams = [["Amit", "Rahul"], ["Sneha", "Priya"]]
teams[1].append("Vijay")
print(teams)

teams[0].append("janni")
print(teams)

#nested list len()
departments = [["HR", "Sales"], ["IT", "Support"], ["Finance"]]
print(len(departments[1]))


#nested list loop
#print every list in new line
groups = [[10, 20], [30, 40], [50, 60]]
for i in groups:
    print(i)

##list comprehension
#cube
cubes=[i*i*i for i in range(1,6)]
print(cubes)

#square
square=[i*i for i in range(1,6)]
print(square)

#even num
even_num=[i for i in range(1,11) if i%2==0]
print(even_num)

#double the number
double_values=[i*2 for i in range(1,6)]
print(double_values)

#odd values
odd=[i for i in range(1,11) if i%2!=0]
print(odd)



