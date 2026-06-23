

# Câu 1.from math import * là Anti-pattern?
# Import toàn bộ hàm và biến của thư viện vào chương trình.
# Dễ gây trùng tên hàm, biến.
# Khó đọc và khó bảo trì mã nguồn.
# Khó xác định một hàm thuộc thư viện nào.

# Cách tốt hơn:
# import math


# hoặc
# from math import sqrt

# Câu 2. Thư mục cần tệp gì để trở thành Package?

# Cần có file:

# __init__.py

# Vai trò:

# Đánh dấu thư mục là Package Python.
# Cho phép import các module bên trong package.
from datetime import datetime

from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
from utils.file_helper import create_log_dir


shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    }
]


def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

    create_log_dir("logs")

    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)

    for shipment in shipments:

        distance = calculate_distance(
            shipment["from_lat"],
            shipment["from_lon"],
            shipment["to_lat"],
            shipment["to_lon"]
        )

        eta = predict_eta(
            shipment["depart"],
            distance
        )

        deadline = datetime.strptime(
            shipment["deadline"],
            "%Y-%m-%d %H:%M:%S"
        )

        print(f"\n[CHUYẾN XE {shipment['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {shipment['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")

        if eta <= deadline:
            print(" + Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)")
        else:
            print(
                f" + Trạng thái: 🔴 CẢNH BÁO "
                f"(Trễ hạn! Deadline yêu cầu lúc {deadline.strftime('%H:%M:%S')})"
            )

    print("\n" + "=" * 56)


if __name__ == "__main__":
    main()
