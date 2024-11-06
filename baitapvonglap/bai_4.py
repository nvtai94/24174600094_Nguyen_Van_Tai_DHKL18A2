#bai_4
#Nhập vào một số 
n = int(input("nhập vào một số: "))

#Kiểm tra số nguyên tố
if n <= 1:
    print(f"{n}không phải là số nguyên tố")
else:
    for i in range(2, n):  #kiểm tra từ 2 đến n-1
        if n % i == 0:  #n chia heets cho i thì n không phải số nguyên tố
            print(f"{n}không phải là số nguyên tố")
            break  #nếu chia hết thì ngừng kiểm tra
    else:
        print(f"{n}là số nguyên tố")