#bài 5
chuoi_nhap_vao = input("Nhập vào một chuỗi bất kì: ")
so_chu_hoa = 0  
so_chu_thuong = 0 
for ky_tu in chuoi_nhap_vao:
    if ky_tu.isupper(): 
        so_chu_hoa += 1
    elif ky_tu.islower():
        so_chu_thuong += 1
print(f"Số chữ cái viết hoa: {so_chu_hoa}")
print(f"Số chữ cái viết thường: {so_chu_thuong}")
