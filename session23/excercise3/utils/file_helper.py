import os


def create_folder():
    print("----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")

    if not os.path.exists("aviation_logs"):

        print(
            "[SYSTEM] Thư mục 'aviation_logs' "
            "chưa tồn tại. Đang tiến hành khởi tạo..."
        )

        os.mkdir("aviation_logs")

        print("[SYSTEM] Tạo thư mục thành công!")

    else:
        print(
            "Thư mục đã tồn tại, "
            "bỏ qua bước khởi tạo"
        )
