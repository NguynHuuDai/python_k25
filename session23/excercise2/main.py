
# Câu 1. Tác hại của from datetime import *
# Import toàn bộ thành phần của thư viện datetime vào chương trình.
# Dễ gây xung đột tên biến(Name Collision).
# Khó xác định hàm hoặc lớp đến từ đâu.
# Khó bảo trì khi dự án lớn.

# Ví dụ:

# time = 120


# Khi đó tên time của thư viện datetime có thể ghi đè hoặc gây nhầm lẫn với biến time trong chương trình.

# Nên dùng:


# hoặc

# Câu 2. Hàm nào tốt hơn os.mkdir()?

# Sử dụng:

# os.makedirs(path, exist_ok=True)

# Ưu điểm:

# Tạo được nhiều thư mục lồng nhau.
# Không phát sinh lỗi nếu thư mục đã tồn tại.
# An toàn hơn os.mkdir().

# Ví dụ:

# os.makedirs("media_vault/2026/video", exist_ok=True)
from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date


raw_files = [
    {
        "filename": "pod_ep1.mp3",
        "size_bytes": 4500,
        "duration_sec": 180,
        "upload_at": "2026-06-10"
    },
    {
        "filename": "movie_trailer.mp4",
        "size_bytes": 105000,
        "duration_sec": 145,
        "upload_at": "2026-06-31"
    },
    {
        "filename": "clip_short.mp4",
        "size_bytes": 8200,
        "duration_sec": 15,
        "upload_at": "2026-05-15"
    }
]


def main():
    success_count = 0

    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")

    safe_create_dir("media_vault")

    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    print("-" * 75)

    for media_file in raw_files:

        print(f"\n[TỆP TIN: {media_file['filename']}]")

        upload_date = parse_and_inspect_date(
            media_file["upload_at"]
        )

        if upload_date is None:
            print(
                f" + Trạng thái phân loại: 🔴 THẤT BẠI "
                f"(Lỗi: Định dạng ngày upload "
                f"'{media_file['upload_at']}' không tồn tại)"
            )
            continue

        disk_blocks = calculate_disk_blocks(
            media_file["size_bytes"]
        )

        if media_file["filename"].endswith(".mp3"):
            folder_type = "audio"
        else:
            folder_type = "video"

        safe_create_dir(
            f"media_vault/{folder_type}"
        )

        print(
            f" + Dung lượng thực tế: "
            f"{media_file['size_bytes']:,} Bytes"
        )

        print(
            f" + Số khối phân vùng (4KB Block): "
            f"{disk_blocks} Blocks"
        )

        print(
            f" + Trạng thái phân loại: "
            f"🟢 HỢP LỆ "
            f"(Lưu trữ vào thư mục '{folder_type}')"
        )

        success_count += 1

    print("=" * 56)

    print(
        f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý "
        f"{success_count}/{len(raw_files)} tệp tin thành công. "
        f"Hệ thống ổn định."
    )


if __name__ == "__main__":
    main()
