#Câu 5
import math
def is_perfect_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n

def is_perfect_square_string(s):
    try:
        num = int(s)
        return is_perfect_square(num)
    except ValueError:
        return False
print(is_perfect_square_string("16"))
print(is_perfect_square_string("25"))
print(is_perfect_square_string("10"))
print(is_perfect_square_string("abc"))
print(is_perfect_square_string("1"))
