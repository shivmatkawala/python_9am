# Range Datatype:-
    # It creates a sequence of numbers [immutable sequence]

# Intialize Range:-
    # single argument
r1 = range(5)  # => start 0, end 5, step 1  (start and step are default)
print(list(r1))

r2 = range(8, 15)  # => start 8, end 15, step 1 (step is default)
print(list(r2))


r3 = range(25, 40, 2)  # start 25, end 40, step 2
print(list(r3))


r4 = range(90, 70, -2) 
print(list(r4))
