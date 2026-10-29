import sqlite3 as sq
con=sq.connect("mydata.db")
cur=con.cursor()
cur.execute("create table student(id int, name text)")
cur.execute("insert into student(id,name)values(?,?)",(1,'janni'))

L=[(2,"pravin"),(3,"shiv"),(4,"Gaurav"),(5,"Arjun")]
cur.executemany("insert into student values(?,?)",L)

data=cur.execute("select * from student")
print(data)

for row in data:
    print(row[0],row[1])

cur.execute("select * from student")
data=cur.fetchall()
print("Total rows: ",len(data))

for row in data:
    print(row[0],row[1])


cur.execute("select * from student where id=2")
data=cur.fetchone()
print(data)

cur.execute("update student set name='Gajanan' where id=1")

cur.execute("delete from student where id=4")




con.commit()
con.close()

