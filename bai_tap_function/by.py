doi_bong = []

def xem_danh_sach():
    for cau_thu in doi_bong:
        print(cau_thu)

def nhap_thong_tin():
    ma_cau_thu = input("Nhập mã cầu thủ: ")
    ten_cau_thu = input("Nhập tên cầu thủ: ")
    tuoi = int(input("Nhập tuổi cầu thủ: "))
    vi_tri = input("Nhập vị trí cầu thủ (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
    so_huy_chuong = int(input("Nhập số huy chương của cầu thủ: "))
    thuong = 0  # Sẽ tính sau

    cau_thu = {
        'ma_cau_thu': ma_cau_thu,
        'ten_cau_thu': ten_cau_thu,
        'tuoi': tuoi,
        'vi_tri': vi_tri,
        'so_huy_chuong': so_huy_chuong,
        'thuong': thuong
    }
    doi_bong.append(cau_thu)

def tinh_thuong():
    for cau_thu in doi_bong:
        so_huy_chuong = cau_thu['so_huy_chuong']
        if so_huy_chuong > 10:
            cau_thu['thuong'] = so_huy_chuong * 500000
        elif 5 <= so_huy_chuong <= 10:
            cau_thu['thuong'] = so_huy_chuong * 300000
        else:
            cau_thu['thuong'] = so_huy_chuong * 200000

def xoa_cau_thu():
    ma_cau_thu = input("Nhập mã cầu thủ cần xóa: ")
    for cau_thu in doi_bong:
        if cau_thu['ma_cau_thu'] == ma_cau_thu:
            doi_bong.remove(cau_thu)
            print(f"Đã xóa cầu thủ có mã {ma_cau_thu}")
            return
    raise ValueError(f"Không tìm thấy cầu thủ có mã {ma_cau_thu}")

def chinh_sua_thong_tin():
    ma_cau_thu = input("Nhập mã cầu thủ cần chỉnh sửa: ")
    for cau_thu in doi_bong:
        if cau_thu['ma_cau_thu'] == ma_cau_thu:
            cau_thu['ten_cau_thu'] = input("Nhập tên cầu thủ mới: ")
            cau_thu['tuoi'] = int(input("Nhập tuổi cầu thủ mới: "))
            cau_thu['vi_tri'] = input("Nhập vị trí cầu thủ mới: ")
            cau_thu['so_huy_chuong'] = int(input("Nhập số huy chương của cầu thủ mới: "))
            print(f"Đã cập nhật thông tin cho cầu thủ có mã {ma_cau_thu}")
            return
    raise ValueError(f"Không tìm thấy cầu thủ có mã {ma_cau_thu}")

def sap_xep_cau_thu():
    doi_bong.sort(key=lambda x: x['so_huy_chuong'])
    xem_danh_sach()

def menu():
    while True:
        try:
            print("Chương trình quản lý đội bóng")
            print("1. Xem danh sách cầu thủ")
            print("2. Nhập thông tin cầu thủ")
            print("3. Tính cột thưởng cho cầu thủ")
            print("4. Tìm kiếm và xóa cầu thủ theo mã")
            print("5. Tìm kiếm và chỉnh sửa thông tin cầu thủ theo mã")
            print("6. Xem danh sách cầu thủ sắp xếp theo số huy chương từ nhỏ đến lớn")
            print("0. Thoát")

            choice = input("Chọn chức năng: ")
            
            if choice == '1':
                xem_danh_sach()
            elif choice == '2':
                nhap_thong_tin()
            elif choice == '3':
                tinh_thuong()
            elif choice == '4':
                xoa_cau_thu()
            elif choice == '5':
                chinh_sua_thong_tin()
            elif choice == '6':
                sap_xep_cau_thu()
            elif choice == '0':
                break
            else:
                raise ValueError("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    menu()
