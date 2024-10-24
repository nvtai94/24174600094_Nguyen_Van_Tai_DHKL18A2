#Bai_8
import math

def calculate_expression(x):
    # Tính log4(x)
    log4_x = math.log(x, 4)
    
    # Tính logx(2)
    logx_2 = math.log(2, x)
    
    # Tính giá trị của biểu thức
    result = log4_x + logx_2
    
    # Làm tròn đến số thập phân thứ hai
    return round(result, 2)

# Nhập giá trị x từ bàn phím
x = float(input("Nhập giá trị của x: "))

# Tính và hiển thị kết quả
result = calculate_expression(x)
print(f"Giá trị của biểu thức là: {result}")
