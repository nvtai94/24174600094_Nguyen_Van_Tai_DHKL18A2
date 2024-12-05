import math
#Nhập điểm
diem_hoc_tap = input("nhập điểm học tập(A, B, C, D, E, F): ")

#Phân loại sinh viên
if diem_hoc_tap == 'A':
    thuoc_loai = "Sinh viên xuất sắc"
elif diem_hoc_tap == 'B':
    thuoc_loai = "sinh viên loại giỏi"
elif diem_hoc_tap == 'C':
    thuoc_loai = "Sinh viên loại khá"
elif diem_hoc_tap == 'D':
    thuoc_loai = "Sinh viên loại trung bình"
elif diem_hoc_tap == 'E':
    thuoc_loai = "Sinh viên loại yếu"
elif diem_hoc_tap == 'F':
    thuoc_loai = "Sinh viên thuộc loại kém"
        
#In ra kết quả
print(thuoc_loai)   