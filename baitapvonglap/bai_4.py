#bai_4
#Nhập vào một số 
n = int(input("nhập vào một số: "))

#Kiểm tra số nguyên tố
if n <= 1:
    print(f"{n}không phải là số nguyên tố")
else:
    for i in range(2, n):  
        if n % i == 0:  
            print(f"{n}không phải là số nguyên tố")
            break  
    else:
        print(f"{n}là số nguyên tố")