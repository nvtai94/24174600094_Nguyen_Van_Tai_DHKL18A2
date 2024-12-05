#Bài 7
m = 4  
n = 4  
ma_tran_don_vi = [[1 if i == j else 0 for j in range(n)] for i in range(m)]
print("Ma trận ban đầu:")
for hang in ma_tran_don_vi:
    print(hang)
i = int(input("Nhập vào hàng i: "))
j = int(input("Nhập vào hàng j: "))
if 0 <= i < m and 0 <= j < m:
    temp = ma_tran_don_vi[i]
    ma_tran_don_vi[i] = ma_tran_don_vi[j]
    ma_tran_don_vi[j] = temp
    print("Ma trận sau khi đảo vị trí hai hàng:")
    for hang in ma_tran_don_vi:
        print(hang)
else:
    print("Không hợp lệ!")

