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
s = input ('Enter a string : ')
print(ord('a'))
for i in s:
    if 65 <= ord(i) <=90:
        a = i.lower()
        s = s.replace(i,a,1)
    elif 97 <= ord(i) <= 122:
        a = i.upper()
        s = s.replace(i,a,1)
print(s)





