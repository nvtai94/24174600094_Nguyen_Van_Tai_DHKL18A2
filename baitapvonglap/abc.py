import math
#nhap vao he so
a = float(input("nhap he so a: "))
b = float(input("nhap he so b: "))
c = float(input("nhap vao he so c: "))
#kim tra
if a == 0:
    print("day khong phai phuong trinh bac hai")
else:
    denta = b**2-4*a*c
    if denta < 0:
        print("phuong trinh vo nghiem")
    else:
        x1 = (-b + math.sqrt(denta)) / (2*a)
        x2 = (-b - math.sqrt(denta)) / (2*a)   
        nghiem = [x1, x2] if denta > 0 else [x1]
        for x in nghiem:
            if x > 0 and x.is_integer():
                x = int(x)
                tong_uoc = 0
                
                for i in range(1, x):
                    if x % i == 0:
                        tong_uoc += i
                print(f"nghiem{x} {'la' if tong_uoc == x else 'khong phai'} so hoan hao")
            else:
                print(f"nghiem{x} khong phai so hoan hao")        



