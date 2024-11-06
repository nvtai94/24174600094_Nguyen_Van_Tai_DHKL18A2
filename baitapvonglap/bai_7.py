#bai_7
#Nhập vào một số n
n = int(input("Nhập vào một số n: "))

#Kiểm tra số nguyên tố
for num in range(2, n): # Lặp qua các số từ 2 đến n-1
    so_nguyen_to = True # Giả sử số là số nguyên tố
    for i in range(2,num): # Kiểm tra xem số có chia hết cho i không
        if num % i == 0:
            so_nguyen_to = False # Nếu chia hết, số không phải là số nguyên tố
            break
    if so_nguyen_to:
         # In ra số nguyên tố
        print(num) 