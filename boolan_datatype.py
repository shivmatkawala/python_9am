# Boolean:-

    # True   --> 1
    # False  --> 0
# print(0 == False)

# print(1 == True)

# print(1 == False)

# print(0 == True)

# x = 4
# y = 5
# print(x == y)

# print(x + y  == 9)
# str1 = "Komal"
# print(str1 == 'komal')

# print(34 > 5)
# print(67 < 8)

# print(True + True + True)
# print(True * False)
# print(False / True)
# # print(True / False)  #ZeroDivisionError: division by zero

# print(0 == 0.000)
# print(1 == '1')

# st1 = 'BABY'
# st2 = 'BUJJI'
# print(st1[0] == st2[0])
import copy

# x = 5
# y = copy.deepcopy(x)
# print(x)
# print(y)

# print(x == y)
# print(id(x))
# print(id(y))

print("--------------------------")

# m = 10
# n = m
# print(id(m))
# print(id(n))

print("--------------------------")

z = [1, 22, 34]

y = copy.deepcopy(z)
print(f"{z} --> {id(z)}")
print(f"{y} --> {id(y)}")

print(z == y)  # False
print(y is z)  # False


# m = 5
# n = copy.deepcopy(m)
# print(f"{m} --> {id(m)}")
# print(f"{n} --> {id(n)}")

# print(m == n)  True
# print(m is n)  True
