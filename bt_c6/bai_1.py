#Bai_1
import math
#Bán kính và chiều cao từ bàn phím 
ban_kinh = float(input("Nhập bán kính khối trụ:"))
chieu_cao = float(input("Nhập chiều cao khối trụ"))

#Công thức Sxq Stp
pi = 3.14
dien_tich_xung_quanh = 2 * ban_kinh * chieu_cao
dien_tich_toan_phan = 2 * pi * ban_kinh * (ban_kinh + chieu_cao)
the_tich = pi * ban_kinh **2 * chieu_cao

#Làm tròn kết quả đến số thập phân thứ hai
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)
 
#In ra kết quả
print(f"Diện tích quanh: {dien_tich_xung_quanh}")
print(f"Diện tích toàn phần: {dien_tich_toan_phan}")
print(f"Thể tích: {the_tich}")