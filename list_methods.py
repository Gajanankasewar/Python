##append() method
list=[1,2,3,4]
print(list)
list.append(5)
print(list)

##sort() method
##ascending order
numbers=[30,20,10,40]
numbers.sort()
print(numbers)

##sort in descending order
list=[1,2,3,4]
list.sort(reverse=True)
print(list)

# ##Reverse() method
list=[40,10,30,20]
print(list)
list.reverse()
print(list)

##insert() method
'''Adds an element at a specific index'''
number=[1,2,3,5]
print(number)
number.insert(3,4)
print(number)

##extend() method
add=[10,20,30]
print(add)
add.extend([40,50,60])
print(add)

##Remove() method
list=[12,15,12,20,25,]
list.remove(12)
print(list)

##pop() method
list=[1,2,3,4,5,6]
list.pop(2)
print(list)

#returns the value
num=[10,20,30,40,50]
x=num.pop(1)
print(num)
print(x)

##clear
num=[10,20,30,40]
num.clear()
print(num)

##index() method
list=[10,20,30,40,50]
print(list[4])
print(list[2])

##count() method
number=[10,20,20,30,20,40,20,30]
print(number.count(30))

##copy() method
number=[10,20,30,40,50]
new_list=number
print(new_list)
