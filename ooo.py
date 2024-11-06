#câu lệnh vòng lặp while
n = 10
while n > 2: #True
    print(f"chay vong lap: {n}")
    n = n-1
    
#Vòng lặp While cũng hỗ trợ

n = 10
while n > 2:
    print(f"chay vong lap: {n}")
    n = n - 1 

#While số nguyên tố lớn nhất bằng 20
n = 20
while True:
    for i in range(1,n):
        print("so nay khong phai so nguyen to")
        n = n - 1 
        break
    else:
        print("day la so nguyen to")
        
    if n < 1:
        break
    
print("so nguyen to la: {n}")

        