#bài 9
chuoi_nhi_phan = input("Nhập vào một chuỗi nhị phân: ")
if all(ky_tu in '01' for ky_tu in chuoi_nhi_phan):
    so_thap_phan = int(chuoi_nhi_phan, 2)
    print(f"'{chuoi_nhi_phan}' là số nhị phân, chuyển sang thập phân: {so_thap_phan}")
else:
    print(f"'{chuoi_nhi_phan}' không phải là số nhị phân hợp lệ.")
