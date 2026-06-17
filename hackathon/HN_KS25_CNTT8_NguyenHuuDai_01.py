nhan_su = [
    {
        "ma_nv": "NV001",
        "ten_nv": "Nguyen Van A",
        "luong": 400000,
        "ngay_cong": 25,
        "phu_cap": 1500000,
        "tong_thu_nhap": 11500000,
        "phan_loai_thu_nhap": "Trung bình"
    },
]


def hienthiLuachon():
    print("""
1. Hiển thị danh sách nhân viên
2. Tiếp nhận nhân viên mới
3. Cập nhập thông tin và ngày công
4. Xóa nhân viên
5. Tìm kiếm nhân viên
6. Thông kê quỹ lương và nhân sự
7. Thoát chương trình
""")


def danh_sach_nhan_vien():
    print("Danh sách nhân viên")
    print(f"Mã nhân viên | Họ và tên | Lương | Ngày công | Phụ cấp | Tổng thu nhập | Phân loại thu nhập")
    for lanDem in nhan_su:
        print(
            f"{lanDem['ma_nv']} | {lanDem['ten_nv']} | {lanDem['luong']} | {lanDem['ngay_cong']} | {lanDem['phu_cap']} | {lanDem['tong_thu_nhap']} | {lanDem['phan_loai_thu_nhap']}")


def them_nhan_vien():
    ma_nv_moi = input("Nhập vào mã nhân viên: ").upper()
    if ma_nv_moi == "":
        print("Mã nhân viên không được để trống")
        return
    ten_nv_moi = input("Nhập vào tên nhân viên: ")
    if ten_nv_moi == "":
        print("Tên nhân viên không được để trống")
        return
    luong_moi = float(input("Nhập vào lương nhân viên: "))
    phu_cap_moi = float(input("Nhập vào lương phụ cấp: "))
    ngay_cong_moi = float(input("Nhập vào ngày công"))
    if luong_moi < 0 and phu_cap_moi < 0:
        print('Lỗi: Lương ngày cơ bản và phụ cấp phải lớn hơn hoặc bằng không')
        return

    if ngay_cong_moi < 0 and ngay_cong_moi > 31:
        print("Số ngày không hợp lệ!")
        return

    for lanDem in nhan_su:
        if lanDem['ma_nv'] == ma_nv_moi:
            print("Mã nhân viên đã tồn tại trong hệ thống")
            return
        else:
            tong_thu_nhap = luong_moi * ngay_cong_moi + phu_cap_moi
            if tong_thu_nhap < 9000000:
                phan_loai_thu_nhap = "Thấp"
            elif tong_thu_nhap > 9000000 and tong_thu_nhap < 15000000:
                phan_loai_thu_nhap = "Trung bình"
            elif tong_thu_nhap > 15000000 and tong_thu_nhap < 30000000:
                phan_loai_thu_nhap = "Khá"
            elif tong_thu_nhap > 30000000:
                phan_loai_thu_nhap = "Cao"

            nhan_su.append({
                "ma_nv": ma_nv_moi,
                "ten_nv": ten_nv_moi,
                "luong": luong_moi,
                "ngay_cong": ngay_cong_moi,
                "phu_cap": phu_cap_moi,
                "tong_thu_nhap": tong_thu_nhap,
                "phan_loai_thu_nhap": phan_loai_thu_nhap

            })

def capNhapthongTin():
    tim_ma = input("Nhập vào mã nhân viên muốn tìm")
    for lanDem in nhan_su:
        if tim_ma == lanDem['ma-nv']:
            luong_co_ban = input("Nhập lương mới: ")
            ngay_cong = input("Nhập ngày công mới: ")
            phu_cap = input("Nhập phụ cấp mới: ")
            nhan_su_moi = nhan_su({
                
            })
        else:
            print("Không tìm thấy mã nhân viên")
            return
            
while True:
    hienthiLuachon()
    luaChon = input("Nhập vào lựa chọn của bạn: ")
    if luaChon == "1":
        danh_sach_nhan_vien()
    elif luaChon == "2":
        them_nhan_vien()
    elif luaChon == "3":
        capNhapthongTin()
    else:
        print("Thoát chương trình")