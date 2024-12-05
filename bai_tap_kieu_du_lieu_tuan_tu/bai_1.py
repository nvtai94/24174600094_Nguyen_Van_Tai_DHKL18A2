#Bài 1
ds_nguyen_to = []
while True:
    n = input("Nhap vao so nguyen duong n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1,i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)

ds_nguyen_to.sort()
print(ds_nguyen_to)