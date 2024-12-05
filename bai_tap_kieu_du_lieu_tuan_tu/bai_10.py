#Bài 10
ds_sinh_vien = []
n = int(input("Nhập số sinh viên n = "))
for sinh_vien in range(n):
    ten = input(f"Nhập tên sinh viên thứ {sinh_vien + 1}: ")
    diem = float(input(f"Nhập điểm tổng kết cuối năm của {ten}: "))
    ds_sinh_vien.append({ten: diem})
print("Thông tin sinh viên và điểm tổng kết cuối năm:")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"Tên: {ten}, Điểm: {diem}")



