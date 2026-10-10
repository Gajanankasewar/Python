#SET
s={10,20,30}
s.add(50)
s.update([50,60])
print(s)

#intersection()
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.intersection(b))

#difference() set
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.difference(b))

#symmetric_difference()
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))
