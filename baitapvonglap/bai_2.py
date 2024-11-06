#Bai_2
#Nhập giá trị n 
n = int(input("nhập giá trị n: "))
#Tính S1 
S1 = 0
for i in range(1, n+1):
    S1 += i
#Tính S2
S2 = 0
for i in range (1 , n):
    S2 *= i 
#Tính S3
S3 = 0 
for k in range(1 , n + 1):
    S3 += ((-1) ** (k-1)) / k 
#Tính S4
S4 = 0 
for k in range (n + 1):
    S4 += k / (k + 2)
#In kết quả
print("S1= ", S1)
print("S2= ", S2)
print("S3= ", S3)
print("S4= ", S4)









