# Câu 4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_string(s):
    try:
        num = int(s)
        return is_prime(num)
    except ValueError:
        return False
print(is_prime_string("7"))
print(is_prime_string("10"))
print(is_prime_string("abc"))
print(is_prime_string("13"))
