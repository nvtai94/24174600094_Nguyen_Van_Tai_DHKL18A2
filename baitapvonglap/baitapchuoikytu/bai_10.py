#bài 10
chuoi_nhap_vao = input("Nhập vào một chuỗi bất kì: ")
so = ''.join([ky_tu for ky_tu in chuoi_nhap_vao if ky_tu.isdigit()])  
ky_tu = ''.join([ky_tu for ky_tu in chuoi_nhap_vao if not ky_tu.isdigit()])  
chuoi_ket_qua = so + ky_tu
print(f"Kết quả: {chuoi_ket_qua}")
