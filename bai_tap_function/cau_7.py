#Cau 7
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = 49
b = 53
print(f"UCLN của {a} và {b} là: {ucln(a, b)}")
