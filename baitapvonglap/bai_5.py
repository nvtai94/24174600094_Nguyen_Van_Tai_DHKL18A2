#Bai_5
#Nhập vào một số
n = int(input("nhập vào một số: "))

#Kiểm tra số hoàn hảo
if n <= 1:
    print(f"{n}không phải là số hoàn hảo.")
else:
    # Duyệt qua ước số từ 1 đến n-1
    for i in range(1, n):
        if n % i == 0:
            n -= i  
        if n == 0: 
            print(f"{n}là số hoàn hảo.")
            break
    else:
        print(f"{n}không phải là số hoàn hảo.") 
