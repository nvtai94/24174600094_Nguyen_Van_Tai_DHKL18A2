import math
#Nhập lương nhân viên
luong = float(input("nhập lương nhân viên (VNĐ): "))

#Thuế thu nhập
if luong >= 15000000:
    thue = luong * 0.3
elif luong >= 7000000:
    thue = luong * 0.2
else:
    thue = luong * 0.1
    
#Tính lương ròng
luong_rong = luong - thue

#In ra kết quả
print(f"lương nhân viên: {luong:.2f} VNĐ")
print(f"thuế thu nhập: {thue:.2f} VNĐ")
print(f"lương ròng (số tiền thực sự nhận được): {luong_rong:.2f} VNĐ")