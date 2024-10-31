import math
#nhập loại xe, quãng đường, thời gian chờ
loai_xe = float(input("nhập loại xe (4 hoặc 7): "))
quang_duong = float(input("nhập s (km): "))
thoi_gian_cho = float(input("nhập t chờ (phút): "))

#Giá phí xe 4 chỗ 
if loai_xe == 4:
    gia_mo_cua = 11000 / 0.8
    if quang_duong <= 0.8:
        cuoc = gia_mo_cua
    elif quang_duong <= 20:
        cuoc = gia_mo_cua + (quang_duong - 0.8) * 12100
    else:
        cuoc = gia_mo_cua + (19.2 * 12100) + (quang_duong - 20) * 10000

#Giá phí xe 7 chỗ
elif loai_xe == 7:
    gia_mo_cua = 13000 / 0.8
    if quang_duong <= 0.8:
        cuoc = gia_mo_cua
    elif quang_duong <= 30:
        cuoc = gia_mo_cua + (quang_duong - 0.8) * 14100
    else:
        cuoc = gia_mo_cua + (29.2 * 14100) + (quang_duong - 30) * 12000
else:
    print("loại xe không hợp lệ")

#Tính tiền chờ
if thoi_gian_cho > 5:
    thoi_gian_cho <= 5  # Miễn phí 5 phút đầu
    tien_cho = thoi_gian_cho * 800
else:
    tien_cho = 0   
        
#Tính giá cước        
tong_gia_cuoc = cuoc + tien_cho

#In ra kết quả
print(f"tổng cước taxi: {tong_gia_cuoc} đồng.")