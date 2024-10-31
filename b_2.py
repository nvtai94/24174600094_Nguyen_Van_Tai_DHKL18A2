#b_2
import math
#Nhập tọa độ điểm M tâm I và bán kính R từ bàn phím
x = float(input("nhập tọa độ x của M: "))
y = float(input("nhập tọa độ y của M: "))
a = float(input("nhâp tọa đọ a của I: "))
b = float(input("nhập tọa độ b của I: "))
R = float(input("nhập bán kính R: "))

#Công thức tính khoảng cách từ M đến I
khoang_cach = (x - a)**2 + (y - b)**2

#Kiểm tra M nằm trong hoặc trên đường tròn
if khoang_cach <= R:
    print(f"M nằm trong hoặc trên đường tròn")
else:
    print(f"M nằm ngoài đường tròn")    