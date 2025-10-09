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


