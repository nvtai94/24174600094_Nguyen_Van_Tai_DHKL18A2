#Bai_11
#Nhập vào hai số
a = int(input("nhập vào số thứ nhất: "))
b = int(input("nhập vào số thứ hai: "))

# Tính GCD (Ước chung lớn nhất) bằng thuật toán Euclid
x, y = a, b
while y != 0:
    x, y = y, x % y

#In ra BCNN trực tiếp mà không cần biến phụ
print(f"BCNN của {a} và {b} là: {abs(a * b) // x}")