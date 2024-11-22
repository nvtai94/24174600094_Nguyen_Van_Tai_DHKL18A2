#bai_4
chuoi_nhap = input("Nhập vào một chuỗi bất kì: ")
so_ky_tu_la_chu = 0  
so_ky_tu_la_so = 0   
so_ky_tu_la_ky_tu_dac_biet = 0  
for ky_tu in chuoi_nhap:
    if ky_tu.isalpha(): 
        so_ky_tu_la_chu += 1
    elif ky_tu.isdigit():  
        so_ky_tu_la_so += 1
    else:  
        so_ky_tu_la_ky_tu_dac_biet += 1        
print(f"Số ký tự là chữ: {so_ky_tu_la_chu}")
print(f"Số ký tự là số: {so_ky_tu_la_so}")
print(f"Số ký tự là ký tự đặc biệt: {so_ky_tu_la_ky_tu_dac_biet}")


















