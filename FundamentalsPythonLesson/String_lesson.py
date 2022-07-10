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
# print(s1[2:8])
# print(s1[:8])
# print(s1[2: len(s1)])
# print(s1[2:-2])
# print(s1[:-2])
# print(s1[:])

"""  Slicing with a distance
    -  s[i:j:k] a part of string from i to j-1 with a distance k
"""
# print(s1[2:9:2]) # pairs
# print(s1[1:9:2]) # unpairs
# print(s1[1:9:3])

"""Change or Delete a string
    - In Python,  Strings are immutable. It isn't changed or deleted
"""

# s1[1] = 'i'  # Lỗi: TypeError: 'str' object does not support item assignment
# del s[0]  # Lỗi: TypeError: 'str' object doesn't support item deletion

""" Mã - Code của ký tự
    + Trong máy tính, mọi dữ liệu đều được lưu thành số - chính xác là dạng số nhị phân
    + Mỗi ký tự được lưu thành một số khác nhau, được gọi là mã - code
    + Danh sách các mã của các ký tự được gọi là bảng mã
    + Bảng mã đơn giản nhất là bảng mã ASCII gồm 256 ký tự, đánh số từ 0 đến 255,
    trong đó gồm tất cả các ký tự ta có thẻ nhìn thấy trên bàn phím máy tính
    + Bảng mã phổ biến nhất hiện nay là Unicode, chứa hầu hết các ngôn ngữ trên thế giới, ký tự toán học, biểu tượng cảm xúc, ...
"""

""" Bảng mã ASCII
    + Chữ cái từ A đến Z có mã tương ứng từ 65 đến 90
    + Chữ cái từ a đến z có mã tương ứng từ 97 đến 122
    + Chữ số từ 0 đến 9 có mã tương ứng từ 48 đến 57
    + Dấu cách có mã 32
"""

"""
- Lấy mã của ký tự dùng hàm ord(ký_tự_muốn_lấy_mã)
- Chuyển từ mã ra ký tự dùng hàm chr(mã_muốn_chuyển)
"""

# print(ord('A'))
# print(ord('Z'))
# print(ord('b'))
# print(ord('z'))
# print(ord('5'))

# print(chr(97))
# print(chr(ord('a') - 32))

""" Operaters in and not in
    + in: check s1 is in s2 or not
    + not in:
"""
# s2 = 'Toulouse University'
# print('Toulouse' in s2)
# print('Tulouse' in s2)


# Ex: Get the numbers in a string from keyboard
# s = input("Input: ")
# # Method 1:
# for i in range(len(s)):
#     if '0' <= s[i] <= '9':
#         print(s[i], end= "")

# print()
# # Method 2:
# for nb in s:
#     if '0' <= nb <= '9':
#         print(nb, end="")
# print()
# # Ex2: Get all lettre 'a' in string
# for i in s:
#     if i == 'a':
#         print (i, end ="")

""" The methods for String
    s.upper()	    Chuyển tất các chữ cái trong chuỗi s thành chữ IN HOA
    s.lower()	    Chuyển tất các chữ cái trong chuỗi s thành chữ in thường
    s.title()	    Viết hoa các chữ cái ở đầu các từ và viết thường các ký tự khác trong chuỗi s
    s.strip()	    Xóa bỏ tất khoảng trắng ở đầu và cuối chuỗi s
    s.lstrip()	    Xóa bỏ tất khoảng trắng ở đầu chuỗi s
    s.rstrip()	    Xóa bỏ tất khoảng trắng ở cuối chuỗi s
    s.count(sub)	Đếm số lần xuất hiện của chuỗi sub trong chuỗi s (trả ra số nguyên)
"""
""" find and replace in String
    
    s.find(sub)	        Trả ra chỉ số (vị trí) đầu tiên bắt đầu xuất hiện chuỗi sub bên trong chuỗi s. Nếu không có chuỗi sub trong s, trả ra -1
    s.rfind(sub)	    Trả ra chỉ số cuối cùng bắt đầu xuất hiện chuỗi sub bên trong chuỗi s. Nếu không có chuỗi sub trong s, trả ra -1
    s.startswith(sub)	Trả ra True nếu chuỗi s bắt đầu bằng chuỗi sub
    s.endswith(sub)	    Trả ra False nếu chuỗi s kết thúc bằng chuỗi sub
    s.replace(s1, s2)	Trả ra chuỗi mới bằng cách thay thế tất cả các chuỗi s1 trong s thành s2
"""
s = 'python is amazing'
print(s.find('on')) # return 4 ( index of 'o' in s)
print(s.find('Python')) # return -1 ( there isn't lettre 'P' in s)
print(s.rfind('n')) # # return 15 ( index of the last 'n' in s)
print(s.startswith("Py")) # return False
print(s.endswith("ing")) #return True
print(s.replace('is', 'are'))

"""  f-strings
 f-strings is used from Python 3.6, cho phép chèn giá trị biến hoặc nhúng cả biểu thức vào trong chuỗi
"""

import math
name, age = 'Python', '30'
a, b = 3, 4.5

print(f"{name} is {age} years old.")
print(f"PI number: {math.pi:10.4}")  # ko nói gì thì mặc định là 6 chữ số thập phân, nhưng ở đây lấy 4
print(f"Superficie {a}x{b} = {a*b}")

