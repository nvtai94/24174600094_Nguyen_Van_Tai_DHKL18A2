#bai_12
#Nhập vào tử số và mẫu số
tu_so = int(input("nhập vào tử số: "))
mau_so = int(input("nhập vào mẫu số: "))

#Kiểm tra mẫu số có phải là 0 hay không
if mau_so == 0:
    print("mẫu số khác bằng 0!")
else:
    #Tính GCD (Ước chung lớn nhất) bằng thuật toán Euclid
    a, b = tu_so, mau_so
    while b != 0:
        a, b = b, a % b
    
    #Tối giản phân số
    tu_so //= a
    mau_so //= a

    #In kết quả phân số đã tối giản
    print(f"nhân số đã tối giản là: {tu_so}/{mau_so}")