#bài 6
chuoi_nhap_vao = input("Nhập vào một chuỗi bất kì: ")
if chuoi_nhap_vao.startswith('-') and chuoi_nhap_vao[1:].isdigit():
    print("Đây là một số âm.")
else:
    print("Đây không phải là một số âm.")
