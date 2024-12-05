#Bài 3
n = input("Nhập vào một số nguyên dương n: ")
if not n.isdigit():
    print("Nhập một số nguyên dương!")
else:
    n = int(n) 
    if n <= 0:
        print("Nhập một số lơn hơn 0!")
    else:
        A = [i for i in range(1, n) if i % 2 != 0]

        B = [i for i in range(1, n) if i % 2 == 0]

        A.sort(reverse=True)
        B.sort(reverse=True)

        print("Danh sách A (số lẻ nhỏ hơn n theo tt giảm dần):", A)
        print("Danh sách B (số chẵn nhỏ hơn n theo tt giảm dần):", B)
        
