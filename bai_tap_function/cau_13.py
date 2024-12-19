#Cau 13
def phan_tich_nguyen_to(n):
    thu_so_nguyen_to = [] 
    i = 4
    while i * i <= n:
        while n % i == 0:
            thu_so_nguyen_to.append(i)
            n //= i 
        i += 1
    if n > 1:
        thu_so_nguyen_to.append(n)
    return thu_so_nguyen_to
print(phan_tich_nguyen_to(80))
print(phan_tich_nguyen_to(90))

