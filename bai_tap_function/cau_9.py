#Cau 9
import math

def toi_gian_phan_so(tu, mau):
    ucln = math.gcd(tu, mau)
    return tu // ucln, mau // ucln
tu, mau = 8,4
print(toi_gian_phan_so(tu, mau))
