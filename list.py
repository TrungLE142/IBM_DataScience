
from operator import le
from random import random
from re import L
import random


# lst = [1,2,3,4]
# lst1 = [1,'hi',3, 14, [1,2,2], "abcd"]
# lst2 = []
#print(lst1[1][1])
# print((lst1[2:5]))
# print((lst1[:5]))
# print(lst1[:-3])
# print(lst1[3:])
# print(lst1[::5]) # lay theo khoang cach 5

# list la type modifiable or mutable
# my_list = [1,'hi',3, 14, [1,2,2], "abcd"]
# my_list[3] = 17
# my_list[-1] ='cdef'
# my_list[2:4] = [5, 20, 6]
# # print(my_list)

# list = [1,'hi',3, 14, [1,2,2], "abcd"]
# list1 = [1,2,3,4,7,8,9,2]
# add an element : append()
# list.append([1,3])
# list.append(list1)
# print(list)
# list.extend([1,2,3])

# cong cac list, phai concatenate list vs list
# print(list + [1,2,3,'a','b'] )

# #insert (index, value)
# list.insert(2,'insert')
# list[2:2] = [1,2,3,4]
# print(list)

#remove or del elements of list
# del list[2]
# del list[-1]
# del list[:1]
# del list1
# list1.remove(2)
# print(list1)

# my_list4 =  list(input("Enter: ").split(","))
# my_list5 =  [1,2,3,4,6,7,8,'ab','cd']
# lst = []


# while len(lst) <= 4:
#     rd = random.randint(0, len(my_list5)-1)
#     print(len())
#     lst.append(my_list5[rd])
#     print(len(lst))

    

# # print(lst)
# dict = {'a': 5000, 'b':10000}
# x= dict.keys()
# for i in x:
#     dict[i]
    
# print(x)
A = 'fgex.;'
B = 'tyf34gdgf;ektufjhgdgex.;.;rtjynur6'

def sep ():
    A = input("Enter 1st: ")
    B = input("Enter 2nd: ")
    AB = []
    test = False
    for i in A:
        for j in B:
            if i == j and i not in AB:
                AB.append(i)
                print(AB)
                lenAB = len(AB) + A.count(i)
                print(lenAB)
    if len(A) == lenAB:
        print (True)
    else: 
        print (False)
        

sep()









