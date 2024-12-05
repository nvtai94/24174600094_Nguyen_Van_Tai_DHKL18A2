#Bài 15
ds_sinh_vien = []
while True:
    print("MENU:")
    print("1. Xem danh sách sinh viên")
    print("2. Nhập thông tin sinh viên vào danh sách")
    print("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
    print("4. Xóa thông tin sinh viên ứng với mã sinh viên")
    print("5. Thoát chương trình")
    lua_chon = input("Nhập lựa chọn mà bạn muốn sử dụng: ")
    if lua_chon.isdigit() == False:
        print("Yeu cau nhap lai")
    else:
        lua_chon = int(lua_chon)
        if lua_chon == 1:
            print("Xem danh sách sinh viên")
            print("ma_sinh_vien","\t","ho_dem", "\t", "ten", "\t", "diem_toan", "\t", "diem_ly", "\t", "diem_hoa", "\t", "diem_tb")
            for sv in ds_sinh_vien:
                print(sv["ma_sinh_vien"],"\t",sv["ho_dem"], "\t", sv["ten"], "\t", sv["diem_toan"], "\t", sv["diem_ly"], "\t", sv["diem_hoa"], "\t", sv["diem_tb"])
        
        elif lua_chon == 2:
           while True:
                sinh_vien = {"ma_sinh_vien": "",
                            "ho_dem": "",
                            "ten": "",
                            "diem_toan": 0.0,
                            "diem_ly": 0.0,
                            "diem_hoa": 0.0,
                            "diem_tb": 0.0,
                            }
                sinh_vien['ma_sinh_vien'] = input("Nhap ma sinh vien: ")
                sinh_vien['ho_dem'] = input("Nhap ho dem: ")
                sinh_vien['ten'] = input("Nhap ten: ")
                #Thêm kiểm tra nhập float
                sinh_vien['diem_toan'] = float(input("Nhap diem toan: "))
                sinh_vien['diem_ly'] = float(input("Nhap diem ly: "))
                sinh_vien['diem_hoa'] = float(input("Nhap diem hoa: "))
                sinh_vien["diem_tb"] = (sinh_vien["diem_toan"] + sinh_vien["diem_ly"] + sinh_vien['diem_hoa'])/3
                ds_sinh_vien.append(sinh_vien)
                
                n = input("Ban co muon nhap them sinh vien nua khong? Y/N")
                if n.capitalize() != 'Y':
                    break
        elif lua_chon == 3:
            print("Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
            n = input("Nhap vao ma sinh vien muon sua: ")
            index = -1
            if len(ds_sinh_vien) == 0:
                print("Dang sach rong")
            else:
                for i in range(len(ds_sinh_vien)):
                    if ds_sinh_vien[i]["ma_sinh_vien"] == n:
                        print("Sinh vien co ton tai")
                        index = i
                        break
                else:
                    print("Sinh vien khong ton tai")
                
                if index != -1:
                    print("Sua thong tin sinh vien:")
                    ds_sinh_vien[index]['ma_sinh_vien'] = input("Nhap ma sinh vien: ")
                    ds_sinh_vien[index]['ho_dem'] = input("Nhap ho dem: ")
                    ds_sinh_vien[index]['ten'] = input("Nhap ten: ")
                    #Thêm kiểm tra nhập float
                    ds_sinh_vien[index]['diem_toan'] = float(input("Nhap diem toan: "))
                    ds_sinh_vien[index]['diem_ly'] = float(input("Nhap diem ly: "))
                    ds_sinh_vien[index]['diem_hoa'] = float(input("Nhap diem hoa: "))
                    ds_sinh_vien[index]["diem_tb"] = (ds_sinh_vien[index]["diem_toan"] + ds_sinh_vien[index]["diem_ly"] + ds_sinh_vien[index]['diem_hoa'])/3
        elif lua_chon == 4:
            print("Xóa thông tin sinh viên ứng với mã sinh viên")
            n = input("Nhap vao ma sinh vien muon xoa: ")
            index = -1
            if len(ds_sinh_vien) == 0:
                print("Dang sach rong")
            else:
                for i in range(len(ds_sinh_vien)):
                    if ds_sinh_vien[i]["ma_sinh_vien"] == n:
                        print("Sinh vien co ton tai")
                        index = i
                        break
                else:
                    print("Sinh vien khong ton tai")
                    
                if index != -1:
                    ds_sinh_vien.remove(ds_sinh_vien[index])   
                    print("Tien hanh xoa sinh vien thanh cong")
        elif lua_chon == 5:
            print("Thoat chuong trinh")
            break
        else:
            print("Yeu cau nhap lai")