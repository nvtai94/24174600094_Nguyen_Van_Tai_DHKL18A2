#Bài 3
n = int(input("Nhập vào số nguyên dương n: "))
A = [i for i in range(n) if i % 2 != 0]
B = [i for i in range(n) if i % 2 == 0]
A.sort(reverse=True)
B.sort(reverse=True)
print("Danh sách A (số lẻ nhỏ hơn n):", A)
print("Danh sách B (số chẵn nhỏ hơn n):", B)