# t=(1,2,3)
# print(t)
# t[2]=22
# print(t)

# l=[10,20,"Hi",3+5j]
# l=tuple
# print(l)


###TUPLE###
#indexing
# colors=("red","green","blue")
# print(colors)
# print(type(colors))
# print(colors.index("green"))
# print(colors[1])

# #negative indexing
# subjects = ("Python", "Java", "C", "SQL")
# print(subjects[-1])
# #slicing
# print(subjects[1:3])

# scores=[10,20,10,30,10,40,50]
# print(scores.count(10))

#index position
fruits = ("apple", "banana", "mango", "banana", "orange")
print(fruits.index("banana"))

#Tuple len()
animals = ("cat", "dog", "lion", "tiger", "elephant")
print(len(animals))

#Tuple  min max()
marks = (75, 90, 65, 88, 95, 70)
print(max(marks))
print(min(marks))

#Tuple SUM()
prices = (100, 250, 150, 300, 200)
print(sum(prices))

#in operator   TUPLE
languages = ("Python", "Java", "C", "JavaScript", "SQL")
print("Python" in languages)
print("smartwatch" not in languages)

#sorted()
numbers=(45,12,89,34,67)
print(sorted(numbers))
print(sorted(numbers, reverse=True))


#Tuple concatnation (+)
a=(100,200,300)
b=(40,50,60)
total=a+b
print(total)

#TUPLE  Repetition(*)
values=(1,2,3)
print(values*3)

#TUPLE  loop()
cities = ("Pune", "Mumbai", "Nanded", "Nagpur")
for i in cities:
    print(i)


#TUPLE unpacking
person = ("Gajanan", 24, "Pune")
name,age,city=person
print(name)
print(age)
print(city)

#ex2
student = ("Rahul", 22, "MCA")
name,age,course=student
print(name)
print(age)
print(course)

#ex3
product = ("Laptop", 55000, "Lenovo")
item,price,brand=product
print(item)
print(price)
print(brand)


##TUPLE MEMBERSHIP + CONDITION
devices = ("Laptop", "Mobile", "Tablet", "Desktop")
if "smartwatch" not in devices:
    print("Smartwatch not found")
else:
    print("found")

#example2
fruits = ("Apple", "Mango", "Banana", "Orange")
if "Mango" in fruits:
    print("Mango Found")
else:
    print("Not Found")

#example 3
subjects = ("Python", "SQL", "HTML", "CSS")
if "Java" in subjects:
    print("Found")
else:
    print("Java not found")

#not in example
colors = ("Red", "Blue", "Green", "Yellow")
if "Black" not in colors:
    print("Black not found")
else:
    print("Black found")


##for loop + condition
#even number
numbers = (10, 15, 20, 25, 30, 35, 40)
for i in numbers:

    if i%2==0:
        print(i)

#odd number
values = (11, 14, 17, 20, 23, 26, 29, 32)
for i in values:
    if i%2!=0:
        print(i)

#sum of even number
data = (10, 15, 20, 25, 30, 35, 40)
sum=0
for i in data:
    if i%2==0:
        sum+=i
print(sum)