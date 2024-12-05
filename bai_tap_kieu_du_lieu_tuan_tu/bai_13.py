#bài 13
ds_sinh_vien = []
n = int(input("Nhập số sinh viên n = "))
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    diem = float(input(f"Nhập điểm tổng kết cuối năm của {ten}: "))
    ds_sinh_vien.append([ten, diem])
print("Danh sách sinh viên:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien[0]}    {sinh_vien[1]}")
ten_moi = input("Nhập tên sinh viên muốn thêm: ")
ton_tai = False
for sinh_vien in ds_sinh_vien:
    if sinh_vien[0].lower() == ten_moi.lower():
        ton_tai = True
        break
if ton_tai:
    print("Thông tin sinh viên đã tồn tại")
else:
    diem_moi = float(input(f"Nhập điểm tổng kết của sinh viên {ten_moi}: "))
    ds_sinh_vien.append([ten_moi, diem_moi])
    print("Đã thêm sinh viên")
print("Danh sách mới:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien[0]}    {sinh_vien[1]}")
