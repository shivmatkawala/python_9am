# TUPLE DATA TYPE:-

    # What type of datat type is tuple ?
        # Tuple is a collection data type
        # Tuple is heterogeneous data type
        # Tuple is immutable data type   ---> can't be modified
        # tuple supports Indexing
        # tuple is ordered datatype


# Initialization of tuple:

    # ()  ==> parenthesis
# tup1 = ()
# print(tup1)
# print(type(tup1))   #<class 'tuple'>

# print("------------------------------")

# tup2 = (1, 2, 3)
# print(tup2)
# print(type(tup2))

# print("------------------------------")

# tup3 = (1, 1.1, 5-7j, True, 'Hello', [12, 23, 34], (1, 2, 3))
# print(tup3)
# print(type(tup3))

# print("------------------------------")

#     # tuple()  

# tup4 = tuple([1, 2, 3, 4, 5])
# print(tup4)
# print(type(tup4))  #TypeError: tuple expected at most 1 argument, got 5

# print("------------------------------")

# tup5 = tuple((12, 23, 34, 45))
# print(tup5)
# print(type(tup5))

# print("------------------------------")

# tup6 = tuple({100, 200, 300, 400})
# print(tup6)
# print(type(tup6))

# print("------------------------------")

# tup7 = tuple("APPLE")
# print(tup7)
# print(type(tup7))

# print("------------------------------")


# tup8 = tuple(6)  # tuple() function takes only one arguments and that has to be iterable / collection.
# print(tup8)
# print(type(tup8))  #TypeError: 'int' object is not iterable


    # INDEXING

        # 1) Positive Indexing
                # It starts from Left side and ends at right side.
                # Index starts from 0

        # 2) Negative Indexing
                # It starts from Righand ends at Left side.
                # It starts from -1

    
# tup9 = ("H", "E", "L", "L", "O", " ", "W", "O", "R", "L", "D")
# print(tup9)

# # H
# print(tup9[0])

# #L
# print(tup9[2])

# # W
# print(tup9[6])

# # H
# print(tup9[-11])

# # L
# print(tup9[-9])

# # W
# print(tup9[-5])


    # SLICING
        # [START INDEX: END INDEX+1: STEP]
        # Slicing privides us a slice 


tup1 = (1, 2.2, 3+4j, "Baby", [12, 23, 34], ('K', 2), True, False)

# print(tup1[0:3:1])
# print(tup1[-8:-5:1])

# print(tup1[3:8:2])
# print(tup1[-5::2])

# print(tup1[6::-2])


# BUILT IN METHODS ON TUPLE.

# count --> count repetation of a paricular element in tuple

# tup2 = (1, 2, 3, 4, 2, 3, 1, 5, 7, 6, 2, 2, 8, 1, 3)
# print(tup2.count(2))
# print(tup2.count(3))
# print(tup2.count(1))
# print(tup2.count(5))


# index()   ---> this method returns an index of a particular element

# tup3 = (12, 23, 34, 445, 56, 678)
# print(tup3.index(23))
# print(tup3.index(56))
# print(tup3.index(678))
# # print(tup3.index(90))  #ValueError: tuple.index(x): x not in tuple


# Concatination
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)


# Repetation
t3 = (10, 20, 30)
print(t3 * 3)


# Unpacking
t4 = (2, 3, 4, 5, 6, 7)
a, b, c, d, e, f, g = t4
print(a)
print(b)
print(c)
print(d)
print(e)
# ValueError: too many values to unpack (expected 5)
# ValueError: not enough values to unpack (expected 7, got 6)



