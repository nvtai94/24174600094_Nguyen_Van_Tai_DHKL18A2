#Bài 12
ds_sinh_vien = []
n = int(input("Nhập số lượng sinh viên n = "))
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    diem = float(input(f"Nhập điểm tổng kết cuối năm của {ten}: "))
    ds_sinh_vien.append([ten, diem])
print("Danh sách sinh viên:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien[0]}    {sinh_vien[1]}")
xoa_ten = input("Nhập tên sinh viên muốn xóa: ")
for sinh_vien in ds_sinh_vien:
    if sinh_vien[0].lower() == xoa_ten.lower():
        ds_sinh_vien.remove(sinh_vien)
        break
print("Danh sách sinh viên còn lại:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien[0]}    {sinh_vien[1]}")
