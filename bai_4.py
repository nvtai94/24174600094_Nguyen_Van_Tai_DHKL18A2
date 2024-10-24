#Bai_4
def calculate_electricity_chi_phi(thoi_gian_giay):
    dien_ap = 220  # V
    cuong_do_dong_dien = 2.7 # A
    gia_tien_kwh = 7000  # đ/kWh

    # Công suất tiêu thụ (P = U * I)
    cong_suat = dien_ap * cuong_do_dong_dien

    # Chuyển đổi thời gian sử dụng từ giây sang giờ
    thoi_gian_gio = thoi_gian_giay / 3600

    # Năng lượng tiêu thụ (E = P * t) trong kWh
    nang_luong = (cong_suat * thoi_gian_gio) / 1000

    # Tính tiền điện
    chi_phi = nang_luong * gia_tien_kwh

    # Làm tròn đến số thập phân thứ hai
    chi_phi = round(chi_phi, 2)

    return chi_phi

# Nhập thời gian sử dụng từ bàn phím
thoi_gian_giay = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

chi_phi = calculate_electricity_chi_phi(thoi_gian_giay)

print(f"Tiền điện phải trả: {chi_phi} đ")
