##find the number greater than 10
numbers = [12, 7, 15, 4, 9, 20, 3]
count=0
for n in numbers:
    if n>10:
        count+=1
print(count)


#largest number between list
numbers = [4, 7, 2, 9, 6, 3]
largest=0
for i in numbers:
    if i>largest:
        largest=i
print(largest)


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