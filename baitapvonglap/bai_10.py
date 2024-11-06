#Bai_10
#Nhập hai số từ người dùng
a = int(input("nhập số thứ nhất: "))
b = int(input("nhập số thứ hai: "))

#Dùng thuật toán Euclid để tìm UCLN
while b != 0:
    a, b = b, a % b

#In ra kết quả
print(f"UCLN của hai số là: {a}")
