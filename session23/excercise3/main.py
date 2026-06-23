

# import math
# Vì sao không nên dùng from math import *
# Import toàn bộ hàm của thư viện vào chương trình.
# Dễ gây trùng tên biến và hàm.
# Khó đọc và bảo trì mã nguồn.
# Khó xác định hàm thuộc thư viện nào.

# Nên dùng:

# from math import ceil

# hoặc:
# import math
from core.logistics import display_flights
from core.manager import add_flight

from utils.time_helper import calculate_eta
from utils.file_helper import create_folder


flights = [
    {
        "flight_id": "RA001",
        "passengers": 154,
        "depart_time": "2026-06-15 08:00:00",
        "duration_min": 120
    },
    {
        "flight_id": "RA002",
        "passengers": 85,
        "depart_time": "2026-06-15 13:30:00",
        "duration_min": 45
    }
]


def main():

    while True:

        try:

            print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
            print("1. Hiển thị lịch trình và Thống kê hậu cần")
            print("2. Tiếp nhận chuyến bay mới")
            print("3. Tính thời gian hạ cánh dự kiến (ETA)")
            print("4. Khởi tạo thư mục lưu trữ log hệ thống")
            print("5. Thoát chương trình")
            print("==================================================")

            choice = int(
                input("Nhập lựa chọn của bạn: ")
            )

            if choice == 1:
                display_flights(flights)

            elif choice == 2:
                add_flight(flights)

            elif choice == 3:
                calculate_eta(flights)

            elif choice == 4:
                create_folder()

            elif choice == 5:
                print(
                    "Cảm ơn kỹ sư đã sử dụng hệ thống!"
                )
                break

            else:
                print(
                    "Vui lòng nhập từ 1 đến 5!"
                )

        except ValueError:
            print(
                "Lựa chọn không hợp lệ! "
                "Vui lòng nhập từ 1 đến 5."
            )


if __name__ == "__main__":
    main()
