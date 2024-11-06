#Bai_6
import math

#Nhập vào một số
n = int(input("Nhập một số: "))

#Tính căn bậc hai của số n
sqrt_n = math.isqrt(n)  # dùng math.isqrt để lấy căn bậc hai nguyên của n

#Kiểm tra nếu căn bậc hai bình phương = n
if sqrt_n * sqrt_n == n:
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
