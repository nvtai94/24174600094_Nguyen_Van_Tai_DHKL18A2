#Bai_8
#Nhập vào một số n
n = int(input("nhập vào một số n: "))

#Tìm và in tất cả các số chính phương nhỏ hơn n
x = 1
while x * x < n:
    print(x * x)
    x += 1