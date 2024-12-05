n = int(input("Nhap gia tri nguyen duong n:"))
tong_n = 0
for k in range(1, n):
    tong_1 = 0
    for l in range(1, k):
        tong_l = tong_1 + (l + 1)
    tong_n = tong_n + (tong_1/k)
    