#Bài 8
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = [[0] * n for _ in range(m)]
print("Nhập các phần tử cho ma trận A:")
for i in range(m):
    for j in range(n):
        A[i][j] = int(input(f"Nhập phần tử A[{i+1}][{j+1}]: "))
print("Ma trận A ban đầu là:")
for i in range(m):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
i = int(input("Nhập chỉ số của cột i cần đảo (từ 1 đến n): ")) - 1
j = int(input("Nhập chỉ số của cột j cần đảo (từ 1 đến n): ")) - 1
for k in range(m):
    A[k][i], A[k][j] = A[k][j], A[k][i]
print("Ma trận A sau khi đảo cột i và j là:")
for i in range(m):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
