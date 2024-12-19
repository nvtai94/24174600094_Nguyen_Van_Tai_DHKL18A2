#Cau 10
import math
def thap_phan_sang_phan_so(thap_phan):
    mau_so = 10 ** len(str(thap_phan).split('.')[1])
    tu_so = int(thap_phan * mau_so)
    ucln = math.gcd(tu_so, mau_so)
    return tu_so // ucln, mau_so // ucln
so_thap_phan = 0.98
print(thap_phan_sang_phan_so(so_thap_phan))
