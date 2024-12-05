#Bài 14
ds_sinh_vien = []
n = int(input("Nhập số sinh viên n = "))
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    diem = float(input(f"Nhập điểm tổng kết cuối năm của {ten}: "))
    ds_sinh_vien.append([ten, diem])
print("Danh sách sinh viên:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien[0]}    {sinh_vien[1]}")
ten_can_sua = input("Nhập tên sinh viên muốn sửa thông tin: ")
sua_thong_tin = False
for sinh_vien in ds_sinh_vien:
    if sinh_vien[0].lower() == ten_can_sua.lower():
        diem_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
        sinh_vien[1] = diem_moi
        sua_thong_tin = True
        break
if sua_thong_tin:
    print(f"Đã sửa thông tin sinh viên {ten_can_sua}")
else:
    print("Sinh viên không tồn tại trong danh sách")
print("Danh sách mới:")
for sinh_vien in ds_sinh_vien:
    print(f"{sinh_vien[0]}    {sinh_vien[1]}")
