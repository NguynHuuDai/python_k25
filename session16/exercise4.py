# Phân tích thiết kế hàm
# 1. display_records(records)
# Input: Danh sách hồ sơ bệnh án.
# Output: Không trả về gì(None).
# Chức năng: Hiển thị toàn bộ hồ sơ bệnh nhân.
# 2. find_patient_index(records, patient_id)
# Input: Danh sách hồ sơ, mã bệnh nhân.
# Output: Vị trí(index) của bệnh nhân hoặc - 1 nếu không tìm thấy.
# Chức năng: Tìm bệnh nhân theo mã.
# 3. add_patient(records)
# Input: Danh sách hồ sơ.
# Output: Không trả về gì(None).
# Chức năng: Thêm bệnh nhân mới, kiểm tra trùng mã và năm sinh hợp lệ.
# 4. update_diagnosis(records)
# Input: Danh sách hồ sơ.
# Output: Không trả về gì(None).
# Chức năng: Tìm bệnh nhân theo mã và cập nhật chẩn đoán.
# 5. generate_age_report(records)
# Input: Danh sách hồ sơ.
# Output: Không trả về gì(None).
# Chức năng: Tính tuổi và thống kê số lượng bệnh nhân theo nhóm tuổi.
# Luồng hoạt động chương trình
# Hiển thị menu.
# Người dùng chọn chức năng.
# Gọi hàm tương ứng:
# 1 => display_records()
# 2 => add_patient()
# 3 => update_diagnosis()
# 4 => generate_age_report()
# 5 => Thoát chương trình.
# Lặp lại cho đến khi chọn 5.
patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()

    for index, record in enumerate(records):
        if record.startswith(patient_id + "-"):
            return index

    return -1


def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    for index, record in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = record.split("-")

        print(
            f"{index}. [{patient_id}] {name:<20} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

    print("--------------------------------------------------------------------------")


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = name.replace("-", " ").strip().title()

    current_year = 2026

    birth_year = input("Nhập năm sinh: ").strip()

    if (
        not birth_year.isdigit()
        or int(birth_year) < 1900
        or int(birth_year) > current_year
    ):
        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")
        return

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.replace("-", " ").strip().capitalize()

    record = "-".join([
        patient_id,
        name,
        birth_year,
        diagnosis
    ])

    records.append(record)

    print("\nThêm hồ sơ bệnh nhân thành công!")


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ")

    new_diagnosis = (
        new_diagnosis.replace("-", " ")
        .strip()
        .capitalize()
    )

    data[3] = new_diagnosis

    records[index] = "-".join(data)

    print("\nCập nhật chẩn đoán thành công!")


def generate_age_report(records):
    current_year = 2026

    children = 0
    adult = 0
    elderly = 0

    for record in records:
        data = record.split("-")

        age = current_year - int(data[2])

        if age < 16:
            children += 1
        elif age <= 60:
            adult += 1
        else:
            elderly += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


while True:
    print("""
===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====
1. Xem danh sách hồ sơ bệnh án
2. Thêm hồ sơ bệnh nhân mới
3. Cập nhật chẩn đoán theo Mã BN
4. Báo cáo phân loại theo độ tuổi
5. Thoát chương trình
==================================================
""")

    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        display_records(patient_records)

    elif choice == "2":
        add_patient(patient_records)

    elif choice == "3":
        update_diagnosis(patient_records)

    elif choice == "4":
        generate_age_report(patient_records)

    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
