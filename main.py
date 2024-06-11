# num = 222
# temp = num
# rev = 0
#
# while num > 0:
#     n = num % 10
#     rev = (rev * 10) + n
#     num = num // 10
# if temp == rev :
#     print("Palindrom")
#
# else:
#     print("Not Palindrom")


# n = int(input("Enter the prime between one to n"))
# for i in range(0, n+1):
#
# if num %2 != 0 and num != 0:
#     for
#     print(num)
#
# else:
#     print("Not prime")


# clculate area of Hw:

#
# n = 5
# for i in range(n):
#     for j in range(n):
#         print(" * ",end='')
#     print("")


# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(j+1, end=' ')
#     print()
# for letter in "PYTHON":
#     print(letter)


# rows = int(input("Enter the number of rows: "))
#
# for i in range(rows, 0, -1):
#   print(" " * (rows - i) + "*" * i)

# rows = int(input("Enter the number of rows: "))
#
# for i in range(rows, 0, -1):
#   for j in range(i, 0, -1):
#     print(j, end=" ")
#   print()


# Function to print the half pyramid in reverse order
# def print_inverted_half_pyramid(n):
#
#     for i in range(n, 0, -1):
#         # Print leading spaces
#         for j in range(n - i):
#             print("  ", end="")
#         # Print numbers
#         for k in range(1, i + 1):
#             print(k+i, end=" ")
#         # Move to the next line
#         print()
#
# # Prompt user for the number of rows
# n = int(input("Enter the number of rows: "))
# print_inverted_half_pyramid(n)


# Function to print the half pyramid in reverse order starting with 5
# def print_inverted_half_pyramid(n):
#     for i in range(n, 0, -1):
#
#         for j in range(n - i):
#             print("  ", end="")
#
#         for k in range(n, n - i, -1):
#             print(k, end=" ")
#
#         print()
#
#
# # Prompt user for the number of rows
# n = int(input("Enter the number of rows: "))
# print_inverted_half_pyramid(n)

#2nd Os
n =5
for i in range(n, 0, -1):

    for j in range(n - i):
        print("  ", end="")

    for k in range(n, n - i, -1):
        print(k, end=" ")

    print()


#3rd Qs
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

# a = "Hi hello my name"
# print("Hi" in a)
#
# a = "hi hello "
# print(a[1])
#
# for letter in "Punita":
#     print(letter)
#
# for i in a:
#     print(i)
#
# print(len(a))


# b = "   my name is vb"
# # slice()
# print(b[-7:-1])
#
# print(a.upper())
#
# print(b.strip())
#
# print(a.replace("i","e"))
#
# print(a.split())
#
# print(a+b)
#
# txt = "My name is \"Vishrutha\" V B"
# print(txt)
#
# c = 'My name is "Vishrutha"  V B'
# print(c)