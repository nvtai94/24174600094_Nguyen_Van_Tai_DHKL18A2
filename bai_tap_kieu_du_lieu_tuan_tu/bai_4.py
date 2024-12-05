#Bài 4
m = int(input("Nhập vào số cột của ma trận m = "))
n = int(input("Nhập vào số hàng của ma trận n = "))
ma_tran_a = [[0,0,0],
             [0,0,0],
             [0,0,0]]
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
print("Ma trận a:")
for hang in ma_tran_a:
    print(hang)
ma_tran_b = [[0] * m for _ in range(n)]
print("Ma trận b:")
for hang in ma_tran_b:
    print(hang)
