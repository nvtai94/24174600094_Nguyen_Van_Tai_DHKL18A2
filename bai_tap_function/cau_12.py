#Cau 12
def tinh_tich(*args):
    tich = 1 
    for so in args: 
        tich *= so
    return tich
print(tinh_tich(1, 7, 4, 2, 9)) 
print(tinh_tich(10, -8, 7))