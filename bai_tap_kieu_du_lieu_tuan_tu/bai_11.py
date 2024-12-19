#bài 11
ds_sinh_vien = []
n = int(input("Nhập sốviên n = ")) 
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    diem = float(input(f"Nhập điểm tổng kết cuối năm của {ten}: "))
    ds_sinh_vien.append((ten, diem))
print("Tên    Điểm")

for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien[0]}    {sinh_vien[1]}")
