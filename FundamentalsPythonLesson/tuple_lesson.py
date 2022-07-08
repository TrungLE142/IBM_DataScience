""" Tuple:
    - Introduction
    - Accessing Tuple
    - Operations
    - Working with Tuple
    - Functions and Methods
"""
""" ==>> Tuple is similar to List
    But Tuple is immutable => cannot change the elements of Tuple
"""
""" Avantages:
    -immutale type => use for "keys" of dictionary
    - faster for loop
    - avoid modifying data

"""

# empty_tuple = () # empty_tuple
# my_tuple = (1,-2,0,3)
# my_tuple1 = (1994, [1,0,4], ('py', 'java'))
# my_tuple3 = ('one element',)

# # print(my_tuple3)

# my_tuple2 = 1,'house', 1.4, [1,4,5] #tuple packing
# print(my_tuple2)


# your_tuple = (1, 'Hi', 'Night!', 2.718, 1+3j)
# print(len(your_tuple))  # Quantity of element of your_tuple
# print(your_tuple[4])
# print(your_tuple[0])

# our_tuple = (1992, [1, 0, 3, -5], (), ('Py', 'js', 0, 3.14))
# print(our_tuple[1])
# print(our_tuple[1][2])
# print(our_tuple[3][1])

# my_tuple_test = ('py', 'thon', 'java', 'script', 'Ox', 'Oy')
# print(my_tuple_test[-2])
# print(my_tuple_test[-6])

# my_tuple4 = ('py', 'thon', 'java', 'script', 'Ox', 'Oy')
# print(my_tuple4[:4])
# print(my_tuple4[2:])
# print(my_tuple4[1:4])
# print(my_tuple4[:-5])

""" Manipulate Tuple. Dont like List, Tuple is immutable
    - can modify a element if it is mutable( like List)
    - Concatenate 2 Tuple with operation +
    - Multiply 1 Tuple with n => 
"""
# tuple_01 = (1, 2, 3)
# tuple_02 = (4, 5, 6)
# tuple_03 = (7, 8, 9)
# print(tuple_01 + tuple_02 + tuple_03)
# print(tuple_01 * 2)

# Delete Tuple: cannot delete any element in tuple: immutable but can delete a tuple by "del"
# my_tuple = (0, 1, 2, 3, 4, 5)
# del my_tuple[3]  #  TypeError: 'tuple' object doesn't support item deletion

# del my_tuple  # Del tuple

""" Methodes of Tuple
    - immutable => doesn't have methods: add and remove
        - tuple.count(element): count number of this element in tuple
        - tuple.index(element): return index of this element
"""
# my_tuple = ('d', 'o', 'g', 'p', 'i', 'g', 'd', 'u', 'c', 'k')
# print(my_tuple.count('g'))
# print(my_tuple.index('d'))

# print('a' in my_tuple)
# print('i' in my_tuple)
# print('h' not in my_tuple)




