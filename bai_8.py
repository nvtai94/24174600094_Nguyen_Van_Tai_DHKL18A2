#bài 8
import math
# nhap gia tri x 
x = float(input("nhap gia tri x:"))
# phép tính
log4_x = math.log(x, 4)
logx_2 = math.log(2, x)
# tính biểu thức
ket_qua = log4_x + logx_2
#làm tròn đến số thập phân thứ 2
ket_qua = round(ket_qua, 2)
# kết quả 
print(f"gia tri cua bieu thuc la: {ket_qua}")