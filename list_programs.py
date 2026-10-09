##Programs Using LIST

#find the sum of all elements
number=[1,2,3,4,5]
sum=0
for i in number:
    sum+=i
print(sum)

number=[10,20,30,40,50]
sum=0
for i in number:
    sum+=i
print(sum)

#find the largest number
l=[25,10,45,5,30]
largest=0
for i in l:
    if i>largest:
        largest=i
print(largest)

#2nd way
number=[20,10,70,25,-87]
largest=number[0]
for i in number:
    if i>largest:
        largest=i
print(largest)


#find the smallest element in a list
number=[23,5,69,45,33,21]
smallest=number[0]
for i in number:
    if i<smallest:
        smallest=i
print(smallest)

#2nd way
s=[29,3,40,22,17]
smallest=40
for i in s:
    if i<smallest:
        smallest=i
print(smallest)


#smallest number without built-in funtion
l=[10,40,6,23,45]
smallest=l[0]
for i in l:
    if i<smallest:
        smallest=i
print(smallest)   


#find the difference betwn all elements,starting from 1st element
l=[10,12,17,22,27]
difference=10
for i in l:
    a= i-difference
print(a)
