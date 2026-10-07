student={
    "name":"Gajanan",
    "age":23,
    "city":"Nanded"
}

# #keys()
# print(student.keys())

# #values()
# print(student.values())

# #items()
# print(student.items())

# #get()
# print(student.get("age"))
# print(student.get("name"))
# print(student.get("city"))

# # update()
# student.update({"age":25})
# print(student)
# student.update({"city":"Mumbai"})
# print(student)
# student.update({"name":"janni"})
# print(student)

# #setdefault()
# student.setdefault("job","developer")
# print(student)

# #add new value
# student.update({"sirname":"kasewar"})
# print(student)

# #pop()
# x=student.pop("job")
# print(x)
# print(student)

# #pop-item()
# student.popitem()
# print(student)

#copy()
student2=student.copy()
print(student2)

#fromkeys()
keys=["name","age","city"]
student=dict.fromkeys(keys,"unknown")
print(student)