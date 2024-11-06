#bai_13
#Nhập vào một số
n = int(input("nhập một số: "))

#In "1" đầu tiên
print("1", end="")

# Kiểm tra các thừa số từ 2 đến n
for i in range(2, n + 1):
    while n % i == 0:
        print(f"*{i}", end="")
        n //= i

#Kết thúc
print()