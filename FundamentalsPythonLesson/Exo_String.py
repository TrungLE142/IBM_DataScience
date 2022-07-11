""" Exercices:
01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, 
        nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
"""
# 01.
# s = input("my string: ")
# s = s.replace(s[0],'$')
# print("New String: ", s)

# 02.
# s = 'Toulouse'
# m = int(input ( 'Entre m: '))
# s = s.replace(s[m],"",1) # (index, space , first posititon)
# print('New String: ', s)

# 04.
# s = input ('Enter a string : ')
# if len(s) < 2:
#     print ("")
# else:
#     s1 = s[0:2] + s[len(s)-2:len(s)]
#     print(s1)

# 05.
# s = input ('Enter a string : ')
# a  = '0'
# for i in s:
#     if i >= a:
#         a= i;
# print("max: " +a)

# print("Max character is {} with code {}".format(max(s),ord(max(s))))
# print("Min character is {} with code {}".format(min(s),ord(max(s))))

# 06.
# s = input ('Enter a string : ')
# for i in s:
#     if 65 <= ord(i) <=90:
#         a = i.lower()
#         s = s.replace(i,a,1)
#     elif 97 <= ord(i) <= 122:
#         a = i.upper()
#         s = s.replace(i,a,1)
# print(s)

"""----------------------------------------------------------"""
#Exo1: Write a function to show string and len of string
# def show_string(s):
#     print('String: ',s)
#     print('Length of String: ', len(s))

# s = input("Enter ur string: ")
# show_string(s)

#Exo2: Write a function with 2 args s1, s2. Return a new string in format (s1 + s2). if length of any string is smaller than 5, multiply 5 times.

# from operator import le
# def concat_string(s1,s2):
    
#     if len(s1)<5 and len(s2)<5:
#         s = (s1*3 + s2*3)
#     elif len(s1) < 5 and len(s2)>=5:
#         s= (s1*3 + s2)
#     elif len(s2) < 5 and len(s1)>=5:
#         s= (s1+ s2*3 )
#     else:
#         s = s1+s2
#     return print(s)

# s1 = input('Enter s1: ')
# s2 = input('Enter s2: ')
# concat_string(s1,s2)

#Exo3: Write a function with 2 args s1 s2. Check if s2 is substring of s1 and how many times does s1 present in s2?
# def check_substring(s1,s2):
#     if s2 in s1:
#         print(s1.count(s2)) # count how many times s2 is in s1
#     else:
#         print("String {} isn't in {}".format(s2,s1))

# s1 = input('Enter s1: ')
# s2 = input('Enter s2: ')
# check_substring(s1,s2)

#Exo4: Write a function to reverse a segment of string from index a to index b and return this reversed segment
# def reverse_substring(s,a,b):
#     sub = s[a:b]
#     reverse_sub= sub[::-1]
#     return reverse_sub


# s = input('Enter string: ')
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))


 #exception:
# try:
#     if a<0 or b< 0 :
#         print("Enter integers a, b : ")
#     elif a>b:
#         print('Enter a and b with a<b')
#     elif a>len(s) or b>len(s):
#         print('a or b are longer than length s')
#     else:
#         print(reverse_substring(s,a,b))
# except:
#     print("data type is not OK")

# Exo5: Trả về chuỗi đan xen lần lượt ký tự đầu của chuỗi s1 và ký tự cuối của chuỗi s2

# def exo5 (s1,s2):
#     cible_string =''
#     s2 = s2[::-1]
#     max_length = max (len(s1), len(s2))
#     for i in range(max_length):
#         if i < len(s1):
#             cible_string += s1[i]
#         if i < len(s2):
#             cible_string += s2[i]
#     return cible_string

# s1 = input('Enter string s1: ')
# s2 = input('Enter string s2: ')

# print(exo5(s1,s2))

#exo6: Viết hàm truyền vào tham số là chuỗi s. Trả về chuỗi kết quả bằng cách thay thế đuôi "ing" bằng đuôi "ly" 
# nếu chuỗi s kết thúc bằng "ing", nếu không thì thêm đuôi "ing" vào chuỗi s.
# def exo6(s):
#     if len(s) >= 3 and s[-3:] == 'ing':
#         s= s[:-3]+  'ly'
#     else:
#         s += 'ing'
#     return s

# s = input('Enter a string: ')
# print(exo6(s))

#exo7: Trả về chuỗi kết quả sau khi xóa các ký tự chẵn nếu chuỗi s có độ dài chẵn
# def exo7(s):
#     if len(s)%2 == 0:
#         s = s[1::2]
#     else:
#         s = s[0::2]
#     return s
# s = input('Enter a string: ')
# print(exo7(s))

#exo8: Trả về chuỗi s viết thường nếu ký tự đầu chuỗi s là chữ thường
# def exo8(s):
#     if s[0].islower():
#         s = s.lower()
#     else:
#         s = s.upper()
#     return s
# s = input('Enter a string: ')
# print(exo8(s))

#exo9: Viết hàm trả về chuỗi s sau khi xóa các khoảng trắng thừa
# def exo9(s):
#     s = s.split()
#     s = ''.join(s)
#     return s
# s = input('Enter a string: ')
# print(exo9(s))

#exo10: Viết hàm nối các từ của chuỗi s bằng dấu "-"

# def exo10(s):
#     s = s.replace(' ','-')
#     return s
# def exo10(s):
#     s = s.split()
#     s = '-'.join(s)
#     return s
# s = input('Enter a string: ')
# print(exo10(s))

#exo11 Viết hàm xóa các ký tự trùng lặp trong chuỗi. (Tham số truyền vào là chuỗi s).

# def exo11(s):
#     new_str =''
#     for i in s:
#         if i not in  new_str:
#             new_str += i
    
#     return new_str
# s = input('Enter a string: ')
# print(exo11(s))

#exo12 Hàm trả về từ có độ dài lớn nhất theo thứ tự trong chuỗi s

# def exo12(s):
#     lst = s.split()
#     length_max_character =''
#     for i in range(len(lst)):
#         if len(lst[i]) >len (length_max_character):
#             length_max_character = lst[i]
    
#     return length_max_character
# s = input('Enter a string: ')
# print(exo12(s))

#exo13 Hàm hiển thị các câu của chuỗi s. Các câu đã xóa khoảng trắng thừa và định dạng theo tittle().
# def delete_space(s):
#     s = s.strip() # delete space at begin and end
#     while "  " in s:
#         s = s.replace('  ', ' ')
    
#     s1 = s.split('.')

#     return s
# def exo13(s1):
#     s1 = s.split('.')
#     for i in s1:
#         sentence = delete_space(i)
#         print( sentence.title())
# s = input('Enter a string: ')
# print(exo13(s))

#exo 14: Viết hàm hiển thị số lần xuất hiện của các ký tự trong chuỗi s
def exo14(s):
    count = []
    lst = []
    for i in s:
        if i not in lst:
            nb = s.count(i)
            count.append(nb)
            lst.append(i)
    dictionary = dict(zip(lst, count))
    return dictionary

s ='1 22 333 4444 55555 66666'
print(exo14(s))


    













