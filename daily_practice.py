# # #find the number greater than 10
# numbers = [12, 7, 15, 4, 9, 20, 3]
# count=0
# for n in numbers:
#     if n>10:
#         count+=1
# print(count)


# # #largest number between list
# numbers = [4, 7, 2, 9, 6, 3]
# largest=0
# for i in numbers:
#     if i>largest:
#         largest=i
# print(largest)


# #find second-largest
# numbers = [4, 7, 2, 9, 6, 3]
# largest=0
# seclarge=0
# for i in numbers:
#     if i>largest:
#         seclarge=seclarge
#         largest=i
# for j in numbers:
#     if j>largest and seclarge<largest:
#         seclarge=j
# print(seclarge)



# # #file handling practice
# #write
# import os
# f=open("demo1.txt","w")
# f.write("Hi hello Godd Morning bro\n")
# f.close

# # #read
# import os
# f=open("demo1.txt","r")
# print(f.read())
# f.close()

# # #append
# f=open("demo1.txt","a")
# f.write("Today is 23rd October")
# f.close()

# # #readline
# f=open("demo1.txt","r")
# print(f.readline())
# print(f.readline())

# # #readlines
# f=open("demo1.txt","r")
# print(f.readlines())
# f.close()

# # #Create new file using X if exist give's error
# f=open("demo1.txt","x")

# # #with statement
# with open("demo1.txt","r") as f:
#     print(f.read())




# # ###creating and removing file 
# import os
# f=open("document2.txt","w")
# f.write("hello janni")
# f.close

# import os
# f=open("document2.txt","r")
# print(f.read())
# f.close()

# import os
# f=open("document2.txt","w")
# f.write("Now i'am practicing on File handling in python\n")

# import os
# f=open("document2.txt","a")
# f.write("This is append")

# # #remove file if exist other wise gives print statement
# import os
# if os.path.exists("document2.txt"):
#     os.remove("document2.txt")
# else:
#     print("file not exists")


# ##numpy
# import numpy
# arr=numpy.array([1,2,4,5,6])
# print(arr)

# #2d array
# import numpy
# arr=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)

# # #multidimensionaly array
# import numpy
# arr=numpy.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr)

# import numpy
# arr=numpy.array([1,2,3,4])
# print(arr.dtype)

# import numpy
# arr1=numpy.array([43.2,54.7])
# print(arr1.dtype)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)


# ##Comparison in numpy
# import numpy as np
# x=np.array([1,2,3])
# y=np.array([4,5,6])

# print("original Number")
# print(x)
# print(y)

# # #greater than
# print("greater than")
# print(np.greater(x,y))

# # #greater than equal
# print("greater than equal")
# print(np.greater_equal(x,y))

# # #less than
# print("less than")
# print(np.less(x,y))

# # #less than equal
# print("less than equal to")
# print(np.less_equal(x,y))

# #Conversion
# import numpy as np
# arr=np.array([11,22,33,44,55,66,77,88,99,10,20,30])
# a=arr.reshape(3,4)
# print(a)

# # #multideminsional
# aa=arr.reshape(2,3,2)
# print(aa)

# # #print directly
# print(arr.reshape(3,4))

# #print directly multi-dimensional
# print(arr.reshape(3,2,2))


# ##print each element in arr
# for x in arr:
#     print(x)

# import numpy as np
# arr=np.array([[1,2,3],[1,2,3],[1,2,3]])
# for i in arr:
#     print(i)

# for i in np.nditer(arr):
#     print(i)

# #find index
# a=np.array([1,2,3,4,5,4,4])
# a=np.where(a==4)
# print(a)

# #print 1-D array elements
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,0])
# for i in arr:
#     print(i)


# #print 2-d array element using for loop
# import numpy as np
# a=np.array([[11,22,33,44,55,66],[77,88,99,10,11,12]])
# for x in a:
#     for y in x:
#         print(y)


# #print 3-d array elements using for loop
# import numpy as np
# arr1=np.array([[[1,2,3],
#                 [1,2,3],
#                 [1,2,3]]])
# print(arr1)
# print(arr1.ndim)
# print(arr1.shape)


# import numpy
# a=numpy.array([32,55,67,39,69,77,76,94,88,22])
# b=numpy.where(a%2==0)
# print(b)

# print(numpy.sort(a[b]))






# #### Generator #####

# #print 1 to 5 using while
# def sequence():
#     i=1
#     while i<=5:
#         yield(i)
#         i+=1
# for i in sequence():
#     print(i)


# #print 1 to 5 by 
# def football():
#     i=1
#     while i<=5:
#         yield i
#         i+=1
# k=football()
# for i in k:
#     print(i)


# #print given yeild
# def counting():
#     yield 5
#     yield 10
#     yield 15

# k=counting()
# for i in k:
#     print(i)

# #Generate Even Numbers Using while Loop and yield
# def even_numbers():
#     i=2
#     while i<=10:
#         if i%2==0:
#             yield i
#         i+=1   
            
# for i in even_numbers():
#     print(i)

# print("")

# #Generate Odd Numbers Using a Generator
# def odd_number():
#     i=1
#     while i<=9:
#         if i%2!=0:
#             yield i
#         i+=1
# k=odd_number()
# for i in k:
#     print(i)

# print("")


# #Generate Multiples of 5 Using a Generator
# def multiples():
#     i=5
#     while i<=25:
#         if i%5==0:
#             yield i
#         i+=1
# j=multiples()
# for i in j:
#     print(i)

# print("")


# #Generate Numbers in Reverse Order
# def reverse_count():
#     i=5
#     while i>=1:
#         yield i
#         i-=1
# p=reverse_count()
# for i in p:
#     print(i)

# print("")

# #Generate Squares of Numbers Using a Generator
# def squares():
#     i=1
#     while i<=5:
#         yield i*i
#         i+=1
# for i in squares():
#     print(i)

# print("")

# #Generate Cubes Using a Generator
# def cubes():
#     i=1
#     while i<=5:
#         yield i*i*i
#         i+=1
# for i in cubes():
#     print(i)

# print("")



# #multiple of 5 
# def multiple():
#     i=1
#     num=3
#     while i<=5:
#         yield num*i
#         i+=1
# for i in multiple():
#     print(i)

# print("")


# #Generate Even Numbers Using a Generator
# def ev_num():
#     i=2
#     while i<=20:
#         if i%2==0:
#             yield i
#         i+=1
# even=ev_num()
# for i in even:
#     print(i)


# #factorial of 5
# def factorial():
#     i=1
#     fact=1
#     while i<=5:
#         fact=fact*i
#         yield fact
#         i+=1
# k=factorial()
# for i in k:
#     print(i)

# print("")


# #Generate Running Sum Using a Generator
# def running_sum():
#     i=1
#     sum=0
#     while i<=5:
#         sum=sum+i
#         yield sum
#         i+=1

# for i in running_sum():
#     print(i)

# print("")


# def power_of_two():
#     i=0
#     num=2
#     power=1
#     while i<6:
#         yield power 
#         power=power*num
#         i+=1
# p=power_of_two()
# for i in p:
#     print(i)

# print(" ")


# #Write a generator using while and yield that generates numbers from 1 to 20 that are divisible by 3 but not divisible by 2.
# def generator_numbers():
#     i=1
#     while i<=20:
#         if i%3==0 and i%2!=0:
#             yield i
#         i+=1
# w=generator_numbers()
# for i in w:
#     print(i)

# print("")


# #Write a generator using while and yield that generates numbers from 15 down to 5, including both 15 and 5.
# def reverse_no():
#     y=15
#     while y>=5:
#         yield y
#         y-=1
# for i in reverse_no():
#     print(i)

# print("")

# #Write a generator using while and yield that generates the first 10 multiples of 7, starting from 7.
# def multiple_of_seven():
#     i=1
#     num=7
#     while i<=10:
#         yield num*i
#         i+=1
# r=multiple_of_seven()
# for i in r:
#     print(i)

# print("")


# def generate_words():
#     a="Python is easy to learn"
#     i=0
#     temp=""
#     while i<len(a):
#         if a[i]==" ":
#             yield temp
#             temp=""
#         else:
#             temp=temp+a[i]
#         i+=1
#     if temp:
#         yield temp
# for word in generate_words():
#     print(word)
    

# ##### SQlite database-connectivity ######
# import sqlite3 as sq
# con=sq.connect("demo4.db")
# cur=con.cursor()
# cur.execute("create table if not exists student1(id int, Name text,contact varchar)")
# cur.execute("insert into student1 values(?,?,?)",(1,'janni',1234567789))

# sunny=[(2,"jann2",1234567890),(3,"janni3",45959794847),(4,"janni4",47383944739)]
# cur.executemany("insert into student1 values(?,?,?)",sunny)

# '''add new column'''
# cur.execute("alter table student1 add column 'address'")

# '''add values to new column'''
# cur.execute("update student1 set address='nanded' ")

# demo=cur.execute("select * from student1")
# for row in demo:
#     # print(row)

#     ##OR
#     print(row[0],row[1])

# ####Fetchall()
# cur.execute("select * from student1")
# demo=cur.fetchall()
# print("Total Rows: ",len(demo))

# for row in demo:
# #     print(row)

#     ##OR
#     print(row[0],row[1])


# ####Fetchone()
# cur.execute("select * from student1")
# demo=cur.fetchone()
# print(demo)

# '''Add New Column'''
# cur.execute("alter table student1 add column 'newcity'")


# # '''Drop particular column'''
# cur.execute("alter table student1 drop column 'newcity' ")

# '''delete particular value'''
# cur.execute("UPDATE student1 SET contact = NULL WHERE id = 4")


# # '''delete data from table'''
# cur.execute("delete from student1 where id=4")

# '''drop table'''
# # cur.execute("drop table student1")
# con.rollback()


# con.commit()
# con.close()
    
# ##### OOPS #####
# ### Class and Object ###
# class car:
#     color="Red"
#     brand="BMW"
# car1=car()
# print(car1.color)
# print(car1.brand)


# ##### Constructor #####
# ##constructor
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

# s1=Student("janni",97)
# print(s1.name,s1.marks)

# s2=Student("Pravin_bhai",99)
# print(s2.name,s2.marks)


##task
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    def get_balance(self):
        return self.balance

    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("Total balance= ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
        print("total balance= ",self.get_balance())

    

acc1=Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
    