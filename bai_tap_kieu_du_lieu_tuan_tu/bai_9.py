#Bài 9
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
print("Nhập ma trận A = ")
A = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(int(input(f"Nhập phần tử ma trận A tại vị trí ({i+1}, {j+1}): ")))
    A.append(hang)

print("Nhập ma trận B:")
B = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(int(input(f"Nhập phần tử ma trận B tại vị trí ({i+1}, {j+1}): ")))
    B.append(hang)

tong = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(A[i][j] + B[i][j])
    tong.append(hang)

hieu = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(A[i][j] - B[i][j])
    hieu.append(hang)

k = int(input("Nhập số k để tính tích ma trận A với số k: "))
tich_A_k = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(A[i][j] * k)
    tich_A_k.append(hang)
    
tich = []
for i in range(m):
    hang = []
    for j in range(n):
        gia_tri = 0
        for l in range(len(A[0])):  
            gia_tri += A[i][l] * B[l][j]
        hang.append(gia_tri)
    tich.append(hang)

doi_xung = []
for j in range(n):
    hang = []
    for i in range(m):
        hang.append(A[i][j])
    doi_xung.append(hang)
    
print("Tổng hai ma trận A và B:")
for hang in tong:
    print(hang)
print("Hiệu hai ma trận A và B:")
for hang in hieu:
    print(hang)
print("Tích ma trận A với số k:")
for hang in tich_A_k:
    print(hang)
print("Tích hai ma trận A và B:")
for hang in tich:
    print(hang)
print("Ma trận đối xứng của A:")
for hang in doi_xung:
    print(hang)
