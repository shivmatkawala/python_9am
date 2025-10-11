# SET Datatype:-

    # Set is a collection datatype.
    # Set is mutable datatype
    # Set allows no duplicate only unique element are maintained.
    # Set is unordered collection
    # Set doesnt support Indexing.
    # Set is parially herogeneous datatype (allows only immutable datatypes elements)

# Initialize a set:-
#     # {}
# set1 = {1}
# print(set1)
# print(type(set1))

# set2 = {1, 2.2, 3+4j, "Hello", (1, 2, 3)}
# print(set2)
# print(type(set2))


#############################

# set3 = {1, 2, 3, 4, 1, 2}
# print(set3)


# set4 = {1, 1.0, True, '1'}
# print(set4)

# set4 = {'A', 'Apple'[0], 'a'.upper(), chr(65)}
# print(set4)



    # set()

# set5 = set([1,2,3,4])
# print(set5)
# print(type(set5))

# set6 = set((12, 23, 34))
# print(set6)
# print(type(set6))

# set7 = set({12, 23, 'A', True, (1, 2, 3)})
# print(set7)
# print(type(set7))


# set8 = set("MOgli")
# print(set8)
# print(type(set8))


# Adding & removing elements from set.

# add()
# set1 = {12, 89, 'A', 'b', True}

# print(set1)

# set1.add(False)
# print(set1)

# set1.add(1)
# print(set1)

# set1.add('0')
# print(set1)

# set1.add(6+6)
# print(set1)

# set1.add(100-11)


# update()
# set2 = {10, 20, 30, 40}
# set3 = {'A','B','C'}
# set2.update(set3)
# print(set2)


# pop()
set4 = {5, 10, 15, 20, 25, 0, 100}
# print(set4.pop())
# print(set4)



# # UNION:-
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1 | s2)

# # INTERSCTION
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6, 7}
# print(s1 & s2)


# # difference
# s1 = {9, 8, 7, 6}
# s2 = {7, 6, 5, 4, 3}
# print(s1 - s2)
# print(s2 - s1)


# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8, 9}

# s3 = s1 ^ s2
# print(s3)


# s1 = {1,2, 3, 4, 0}
# s2 = {7, 8, 9, 0}
# print(s1.isdisjoint(s2))


# s1 = {1, 2, 3, 4, 5, 6, 7, 8} # superset
# s2 = {4, 5}  #subset
# print(s1.issubset(s2))

# print(s2.issubset(s1))

# print(s1.issuperset(s2))

# print(s2.issuperset(s1))

# print(s1.issubset(s1))
# print(s1.issuperset(s1))


s1 = {1, 2, 3}  # {1, 2}
s2 = {3, 4, 5}

# diiference Update()
# s1.difference_update(s2)
# print(s1)

# intersection_update()
# s1.intersection_update(s2)
# print(s1)

# symmetric_difference_update()
# s1.symmetric_difference_update(s2)
# print(s1)

