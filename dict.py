student={
    "name":"Gajanan",
    "age":24,
    "course": "MCA"
}

print(student)
print(student["name"])
print(student["course"])

#update age
student["age"]=25
print(student)

#add new element
student.update({"city":"pune"})
print(student)
#add new element 2nd way
student["sirname"]="kasewar"
print(student)

#To access any element
print(student.get("course"))
#2nd way
print(student["course"])

#get() with default value
print(student.get("email","Not Available"))

#keys()
print(student.keys())

#values()
print(student.values())

#items()
student["city"]="pune"
print(student.items())

#pop
x=student.pop("city")
print(x)
print(student)

y=student.popitem()
print(y)
print(student)


#remove()
employee={
    "name":"rahul",
    "salary":30000,
    "department":"it"
}
print(employee)
employee.clear()
print(employee)

del()
employee2={
    "name":"amit",
    "salary":40000,
    "department":"hr",
    "city":"pune"
}

del employee2["department"]
print(employee2)

#in
employee2 = {
    "name": "Amit",
    "salary": 40000,
    "department": "HR",
    "city": "Pune"
}

print("salary" in employee2)

#set default
employee2.setdefault("city","mumbai")
print(employee2["city"])

#To access particular value
print(employee2["salary"])


employee2.setdefault("email","gaju@gmail.com")
print(employee2)
print(employee2["email"])


employee3=employee2.copy()
print(employee3)