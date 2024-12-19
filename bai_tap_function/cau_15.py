#Cau 15
def is_perfect(n):
    if n <= 1:
        return False
    tong_uoc_so = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            tong_uoc_so += i
            if i != n // i:
                tong_uoc_so += n // i
    return tong_uoc_so== n
def so_hoan_hao_nho_nhat(lst):
    so_hoan_hao = [so for so in lst if is_perfect(so)] 
    if so_hoan_hao:
        return min(so_hoan_hao)
    return None 
danh_sach_so = [6,28,24,8888]
so_hoan_hao_nho_nhat = so_hoan_hao_nho_nhat(danh_sach_so)
print("Số hoàn hảo nhỏ nhất trong dãy là:", so_hoan_hao_nho_nhat)
