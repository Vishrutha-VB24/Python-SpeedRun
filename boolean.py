a = 10
b = 20

print(a > 10)
print(a > b)
print(a < b)

#
a = ["apple","papaya","Banana"]
print(a[1])#list
a.insert(1,"Mango")
a.append("Manago")
print(a)

b = {"apple","papaya","Banana"}
print(b)

c = ["Dosa","Roti"]
d = ["tea","coffee"]

print(c + d)#simple adding


c.extend(d)
print(c)

d.sort()
print(d)

f = c.copy()
print(f)