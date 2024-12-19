#Cau 8
def tim_uoc(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc
n = 18
print(f"Các ước của {n} là: {tim_uoc(n)}")
