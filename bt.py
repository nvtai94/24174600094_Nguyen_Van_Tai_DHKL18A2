# Câu 8
# Viết chương trình tính điểm của sinh viên.
# Chương trình này sẽ đọc vào các loại điểm của sinh viên (điểm chuyên cần, điểm giữa kỳ, và điểm cuối kỳ) và xếp loại điểm theo quy luật sau:
# – if điểm trung bình >=9 =>loại=A
# – if điểm trung bình >= 7 và < 9 => loại=B
# – if điểm trung bình >= 5 and < 7 =>loại=C
# – if điểm trung bình < 5 => loại=D

diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))
    

diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
    

if diem_trung_binh >= 9:
       loai= "A"
elif diem_trung_binh >= 7:
        loai = "B"
elif diem_trung_binh >= 5:
        loai = "C"
elif diem_trung_binh <5:
        loai = "D"
    
print(f"Điểm trung bình: {diem_trung_binh:.2f} - Loại: {loai}")
