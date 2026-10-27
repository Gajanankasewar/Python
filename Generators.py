#print given alphabet
def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

#To print 1 To 5 numbers
def mygen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

g = mygen()

for i in g:
    print(i)

print(" ")

#To print 5 To 1 numbers (Reverse)
def mygen1():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

k=mygen1()
for i in k:
    print(i)


#print 1 to 5 numbers using for loop in Generators
def simple():
    for i in range(1,6):    #range is used to print sequence of numbers 
        yield i

r=simple()
for g in r:
    print(g)


#print 1 to 6 numbers using while in Generators
def simple():
    i=1
    while(i<6):
        yield i
        i+=1
r=simple()

for g in r:
    print(g)


##comprehsion 
#normal
a=[x*x for x in range(1,1000001)]
print(a[0])

#using Generator
g=(x*x for x in range(100))
print(next(g))