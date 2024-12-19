#Cau 6
def kiem_tra_so_hoan_hao(n):
    if n <= 0:
        return False
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n
n = 77
print(kiem_tra_so_hoan_hao(n))