num = 222
temp = num
rev = 0

while num > 0:
    n = num % 10
    rev = (rev * 10) + n
    num = num // 10
if temp == rev :
    print("Palindrom")

else:
    print("Not Palindrom")



a = "Hi hello my name"
print("Hi" in a)

a = "hi hello "
print(a[1])

for letter in "Punita":
    print(letter)

for i in a:
    print(i)

print(len(a))


b = "   my name is vb"
# slice()
print(b[-7:-1])

print(a.upper())

print(b.strip())

print(a.replace("i","e"))

print(a.split())

print(a+b)

txt = "My name is \"Vishrutha\" V B"
print(txt)

c = 'My name is "Vishrutha"  V B'
print(c)