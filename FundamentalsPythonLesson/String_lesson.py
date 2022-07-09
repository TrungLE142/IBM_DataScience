__author__ = "leductrung142@gmail.com"

""" String Manipulation
    + Accessing Strings
    + Basic Operations
    + String Slices
    + Function and Method
"""
# my_str = "Hello world"
# print(my_str)
# print(my_str*3)
# print(my_str+my_str)

""" String length
    - nb of character of string
    - len()
"""
s = "13v  dbertijkf"
print(len(s))

""" Accessing Strings. Truy cập vào các ký tự trong Chuỗi.
    -  Access a string by index or slicing
    Chúng ta có thể truy cập từng ký tự bằng chỉ số (index) hoặc một đoạn ký tự bằng cắt (slicing).
    - Index of character begins by 0:
    Index các ký tự trong chuỗi được đánh số từ trái qua phải và bắt đầu từ 0:
    ký tự đầu tiên là 0, ký tự thứ 2 là 1, ..., ký tự cuối cùng là (độ dài - 1)
"""
# print(s[1])
# print(s[-1])
# # To take the final character
# print(s[len(s)-1])
# # IndexError: Index out of range
# print(s[len(s)])


""" Slicing - basic
    - Take a part of initial string => substring
    Dùng để lấy 1 phần từ chuỗi gốc, tạo ra chuỗi con - substring
    
    - Attention:
        + s[:j]: return a substring of (s[0] - s[j-1])
        + s[i:]: return a substring of (s[i] - s[-1])
        + => s[:]: return this s
"""
s1 = "Python Core"
print(s1[2:8])
print(s1[:8])
print(s1[2: len(s1)])
print(s1[2:-2])
print(s1[:-2])
print(s1[:])
