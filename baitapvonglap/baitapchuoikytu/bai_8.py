#bài 8
str_1 = input("Nhập vào chuỗi str_1: ")
str_2 = input("Nhập vào chuỗi str_2: ")
if str_2 in str_1:
    print(f"chuỗi '{str_2}' có nằm trong chuỗi '{str_1}'.")
else:
    print(f"chuỗi '{str_2}' không có trong chuỗi '{str_1}'.")
if str_1 in str_2:
    print(f"chuỗi '{str_1}' có nằm trong chuỗi '{str_2}'.")
else:
    print(f"chuỗi '{str_1}' không có trong chuỗi '{str_2}'.")
