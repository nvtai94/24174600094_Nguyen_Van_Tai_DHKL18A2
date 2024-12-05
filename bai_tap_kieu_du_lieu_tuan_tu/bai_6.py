#Bài 6
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = []

print("Nhập số cho ma trận A:")
for i in range(m):
    hàng = []  
    print(f"Nhập số của hàng {i+1}:")
    
    phần_tử = input().split()  
    for j in range(n):
        hàng.append(int(phần_tử[j])) 
    A.append(hàng) 
print("Ma trận A là:")
for hàng in A:
    print(" ".join(map(str, hàng)))  
