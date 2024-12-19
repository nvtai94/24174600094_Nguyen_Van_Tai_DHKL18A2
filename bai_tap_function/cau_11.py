#Cau 11
def tinh_tong(*args):
    tong = 00
    for so in args:
        tong += so
    return tong
print(tinh_tong(6,9,10,4,7))
print(tinh_tong(10, -5, 3))