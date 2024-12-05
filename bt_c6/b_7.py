import math
#Nhập các hệ số từ bàn phím
a1 = float(input("nhập hệ số a1: "))
a2 = float(input("nhập hệ số a2: "))
b1 = float(input("nhập hệ số b1: "))
b2 = float(input("nhập hệ số b2: "))
c1 = float(input("nhập hệ số c1: "))
c2 = float(input("nhập hệ số c2: "))

#Công thức tính đinh thức
D = a1 * b2 - a2 * b1

if D == 0:
    #Kiểm tra các trường hợp
    D1 = c1 * b2 - c2 * b1
    D2 = a1 * c2 - a2 * c1
    if D1 == 0 and D2 == 0:
        print("hệ phương trình vô số nghiệm")
    else:
        print("hệ phương trình vô nghiệm")
else:
    #Tính x, y theo công thức cramer
    x = (c1 * b2 - c2 * b1) / D
    y = (a1 * c2 - a2 * c1) / D
    print(f"Nghiệm của hệ phương trình là: x = {x}, y = {y}")