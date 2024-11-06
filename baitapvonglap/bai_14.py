#bai_14
n = int(input("nhập số dòng của tam giác Pascal: "))

pascal = [[1] * (i + 1) for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

for row in pascal:
    print(" ".join(str(x) for x in row).center(n * 3))
