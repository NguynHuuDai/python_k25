ton_kho = 100
tong_doanh_thu = 0.0


def nhap_hang(so_luong):
    global ton_kho

    ton_kho += so_luong

    print(f"Đã nhập thành công {so_luong} sản phẩm.")
    print(f"Tồn kho hiện tại: {ton_kho}")


def kiem_tra_ton_kho(so_luong_mua):
    if so_luong_mua > ton_kho:
        print(
            f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {ton_kho}."
        )
        return False

    return True


def tinh_hoa_don(so_luong, don_gia):
    tam_tinh = so_luong * don_gia

    giam_gia = 0

    if tam_tinh >= 1000:
        giam_gia = tam_tinh * 0.1

    sau_giam_gia = tam_tinh - giam_gia

    thue_vat = sau_giam_gia * 0.08

    tong_thanh_toan = sau_giam_gia + thue_vat

    return tam_tinh, giam_gia, thue_vat, tong_thanh_toan


def bao_cao():
    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {ton_kho} sản phẩm")
    print(f"Tổng doanh thu: ${tong_doanh_thu}")


def hien_thi_menu():
    print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
    print("1. Nhập thêm hàng vào kho")
    print("2. Bán hàng (Tính toán hóa đơn)")
    print("3. Xem báo cáo tổng quan")
    print("4. Thoát chương trình")
    print("=================================================")


def menu_nhap_hang():
    so_luong = input("Nhập số lượng sản phẩm muốn thêm: ")

    if not so_luong.isdigit():
        print("Vui lòng nhập đúng kiểu dữ liệu số.")
        return

    so_luong = int(so_luong)

    if so_luong <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return

    nhap_hang(so_luong)


def menu_ban_hang():
    global ton_kho
    global tong_doanh_thu

    so_luong = input("Nhập số lượng mua: ")
    don_gia = input("Nhập đơn giá ($): ")

    if not so_luong.isdigit():
        print("Vui lòng nhập đúng số lượng.")
        return

    if not don_gia.replace(".", "", 1).isdigit():
        print("Vui lòng nhập đúng đơn giá.")
        return

    so_luong = int(so_luong)
    don_gia = float(don_gia)

    if so_luong <= 0 or don_gia <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return

    if not kiem_tra_ton_kho(so_luong):
        return

    tam_tinh, giam_gia, thue_vat, tong_thanh_toan = tinh_hoa_don(
        so_luong,
        don_gia
    )

    ton_kho -= so_luong
    tong_doanh_thu += tong_thanh_toan

    print("\n--- HÓA ĐƠN CHI TIẾT ---")
    print(f"Số lượng: {so_luong}")
    print(f"Đơn giá: ${don_gia}")
    print(f"Tạm tính: ${tam_tinh}")
    print(f"Giảm giá (10%): ${giam_gia}")
    print(f"Thuế VAT (8%): ${thue_vat}")
    print(f"Tổng thanh toán: ${tong_thanh_toan}")
    print("Đã bán thành công!")


def thoat_chuong_trinh():
    print("Lưu dữ liệu...")
    print("Cảm ơn bạn đã sử dụng hệ thống!")


while True:
    hien_thi_menu()

    lua_chon = input("Chọn chức năng (1-4): ")

    if lua_chon == "1":
        menu_nhap_hang()

    elif lua_chon == "2":
        menu_ban_hang()

    elif lua_chon == "3":
        bao_cao()

    elif lua_chon == "4":
        thoat_chuong_trinh()
        break

    else:
        print("Lựa chọn không hợp lệ.")
