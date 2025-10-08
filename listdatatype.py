# List:-

    # List is a collection datatype
    # One variable stores / refers to Multiple values.
    # List is created inside []
    # Inside []  any type of data can be written. [Heterogeneous]
    # List datatype is mutable datatype
    # List is an Ordered collection
    # List supports Indexing.

# Intialize List:-

# students = ["Shakti", "Navitha", "Balkrishna"]
# print(students)
# print(type(students))   #<class 'list'>

# print("--------------------------------------")

# students_age = [23, 21, 22, 23, 20, 24]
# print(students_age)
# print(type(students_age))

# print("--------------------------------------")

# fruits = ["Apple", "Grapes", "Watermelon", "Papaya"]
# print(fruits)
# print(type(fruits))


# grocery = ['sugar', 'jaggery', 'tea powder', 'oil']
# print(grocery)
# print(type(grocery))

# print("-----------------------------------------------")

# random = [12, 4.5, 6-7j, 'Python', True, ['A', 'B', 2,  False]]
# print(random)
# print(type(random))

# print("-----------------------------------------------")

# print(random[3])
# print(random[5])
# print(random[0])

# print(random[-3])
# print(random[-5])
# print(random[-6])

# Slicing

# str1 = "Dear Comrade"
    # strat index : end index+1 : step
# print(str1[0:4:1])
# print(str1[5:12:1])

# print(str1[-12:-8:1])
# print(str1[-7::1])
# # DA ORD
# print(str1[0:12:2].upper())


# str1 = "Dear Comrade"
# # Darm
# print(str1[-2:-6:-1].title())
# #DC
# print(str1[0:10:5])

# # CD
# print(str1[-7::-5])
# print(str1[5:11:5].upper())



# List functions:-
# append add element at the end of the list.
list2 = [12, 23, 34, 45 ,56]

# list2.append(77)
# print(list2)

# list2.append('Kilo')
# print(list2)

# list2.append(False)
# print(list2)


# insert
# it adds element wherever you want.
# list2.insert(0, 100)
# print(list2)

# print(list2.insert(3, 500))
# print(list2)

# extend
# adds multiple elements at end

# list2.extend([100, 200, 300, 400])
# print(list2)


# list2.extend([100, 200, 300, 400])
# print(list2)


list2 = [12, 23, 34, 45 ,56]

# list2.clear()

# list2.remove(34)
# list2.remove(56)
# print(list2)

# print(list2.pop())
# print(list2)


# index()
# list3 = [100, 'S', 78, 4.50, True, [1, 2,3], 123, 78, "K", 1.23]
# print(list3.index(True))
# print(list3.index(123))
# print(list3.index(78))


# list4 = [1, 2, 3, 1, 3, 244, 4432, 5, 12]
# print(list4.count(2))
# print(list4.count(3))
# print(list4.count(1))

# list4.reverse()
# print(list4)

# list4.sort()

# print(list4)

# list4.sort(reverse=True)
# print(list4)



# Repetation

l1 = [1, 2, 3]
# print(l1*3)

# a, b, c, d = [12, 23, 34, 45]
# print(a)
# print(c)

l2 = [7, 8, 9]
print(l1 + l2)

