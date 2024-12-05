#b_4
import math
#Nhập các cạnh
a = float(input("nhập cạnh a: "))
b = float(input("nhập cạnh b: "))
c = float(input("nhập cạnh c: "))
# Kiểm tra các cạnh của tam giác
if a + b > c and a + c > b and b + c > a:
    # Kiểm tra tam giác đều
    if a == b == c:
        print("tam giác đều")
    # Kiểm tra tam giác vuông
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2: 
        # Kiểm tra tam giác vuông cân
        if a == b or b == c or a == c:
            print("tam giác vuông cân")
        else:
            print("tam giác vuông.")
    # Kiểm tra tam giác cân
    elif a == b or b == c or a == c:
        print("tam giác cân.")
    else:
        print("tam giác thường.")
else:
    print("Không phải ba cạnh của tam giác.")
