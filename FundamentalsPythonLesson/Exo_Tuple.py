"""Exercise:
 1) Convert Tuple to List and List to Tuple
 2) Reverse a new Tuple from an existing Tuple
 3) Count the numer of element in a List until there's a Tuple appearing
 4) A List with the tuples not empty inside. Arrange this list with ascending order for the last element of each Tuple
 5) Show the commun element of tuples
 6) Sum, max, min of a tuple
 7) Have a List = ["www.hust.edu.fr", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
    Give a tuple with all suffix # ('fr','org','net','com')
"""
#Exo_1
# a = 'python', 'java', 'js', 4, 6,0.1
# print(a)
# b = list(a)
# print(b)
# my_lst = tuple(b)
# print(my_lst)

#Exo_2
# my_tuple = (1,2,5,7,8)
# my_tuple = my_tuple[::-1]
# print(my_tuple)

#Exo_3
# lst = (1,3,'abc', [4,5,6], ('a','f','k'),4,6)
# count= 0
# for i in lst:
#     if type(i) == tuple:
#         break
#     count +=1
# print(count)

#Exo_4:
lst = [(1,3,4), (3,0,1), (4,8,10), (2,1,4)]

lst1 = []
sort_lst =[]
for i in lst:
    lst1.append(i[-1])
lst2 = set(lst1.sort())
print(lst2)
for j in lst1:
    for a in lst: 
        if a[-1]==j:
            sort_lst.append(a)
# print(sort_lst)
# print(lst1)

# a = [(2, 1, 5), (4, 1, 1), (0, 1, 0)]
# my_list = a[:]
# for i in range(len(my_list)):
#     my_list[i] = my_list[i][::-1]
# my_list.sort()
# for i in range(len(my_list)):
#     my_list[i] = my_list[i][::-1]
print(lst1)
print(sort_lst)


