#Cau 14
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def average_of_primes(lst):
    primes = [so for so in lst if is_prime(so)]
    if len(primes) == 0:
        return None
    return sum(primes) / len(primes)
danh_sach_so = [2, 3, 5, 7, 8, 10, 13]
trung_binh = average_of_primes(danh_sach_so)
print("ttrung binh các số nguyên tố trong dãy:", trung_binh)
