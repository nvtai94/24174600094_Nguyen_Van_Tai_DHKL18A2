#b_1
#Nhập năm từ bàn phím
year = float(input("nhập năm từ bàn phím: "))

#Kiểm tra năm nhuận
if year % 4 == 0 and year % 400 == 0  :
    print(f"năm là năm nhuận")
else:
    print(f"năm không phải là năm nhuận")    