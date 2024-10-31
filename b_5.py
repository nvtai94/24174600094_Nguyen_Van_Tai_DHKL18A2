#b_5
import math
# Nhập ký tự từ bàn phím
ky_tu = input("Nhập một ký tự từ bàn phím: ")
# Định nghĩa các nguyên âm
nguyen_am = "UEOAIueoai"

# Kiểm tra ký tự là nguyên âm hay phụ âm
if len(ky_tu) != 1 or not ky_tu.isalpha():
    print("ký tự sai")
else:
    if ky_tu in nguyen_am:
        print(" là nguyên âm")
    else:
        print("là phụ âm")
