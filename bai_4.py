#bài 4
#nhap thời gian
thoi_gian = float(input("nhap thoi gian: "))
# tri tiết bóng đèn
hieu_dien_the = 220
cuong_do_dong_dien = 2.7
cong_suat = 7000 
#phép tính
cong_suat = thoi_gian*hieu_dien_the*cuong_do_dong_dien/3600*1000
#tính
phai_tra = cong_suat*7000
# in kết quả
print("tien phai tra la: ", phai_tra)