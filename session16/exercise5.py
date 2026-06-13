# 1. find_patient_index(patients, er_id)
# Input: Danh sách bệnh nhân, mã ER.
# Output: Trả về vị trí(index) hoặc - 1.
# Mục đích: Dùng chung cho tìm kiếm, cập nhật và xóa bệnh nhân.

# Thuật toán:

# Chuẩn hóa mã ER bằng strip().upper().
# Duyệt danh sách.
# Dùng startswith(er_id + "|").
# Tìm thấy → trả về index.
# Không thấy → trả về - 1.
# 2. extract_vital_value(vital_string)
# Input: Chuỗi sinh hiệu("HR:115" hoặc "TEMP:39.5").
# Output: Giá trị số dạng float.

# Thuật toán:

# Tách chuỗi bằng:
# vital_string.split(":")
# Các hàm chính
# display_dashboard(patients)
# Hiển thị danh sách bệnh nhân cấp cứu.
# admit_patient(patients)
# Thêm bệnh nhân mới.
# Kiểm tra trùng mã ER.
# Chuẩn hóa tên.
# Ghép dữ liệu thành chuỗi bằng "|".join().
# update_vitals(patients)
# Tìm bệnh nhân.
# Chọn cập nhật HR hoặc TEMP.
# split("|") → sửa dữ liệu → join("|").
# trigger_red_alert(patients)
# Duyệt toàn bộ danh sách.
# Lấy HR và TEMP bằng extract_vital_value().
# Nếu:
# HR > 100 hoặc
# TEMP ≥ 39.0
# Đưa vào danh sách nguy kịch.
# discharge_patient(patients)
# Tìm bệnh nhân theo mã ER.
# Xóa bằng pop(index).
# Luồng chương trình
# while True
# Hiển thị menu

# 1 -> display_dashboard()
# 2 -> admit_patient()
# 3 -> update_vitals()
# 4 -> trigger_red_alert()
# 5 -> discharge_patient()
# 6 -> Thoát
er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]


def find_patient_index(patients, er_id):
    er_id = er_id.strip().upper()

    for index, patient in enumerate(patients):
        if patient.startswith(er_id + "|"):
            return index

    return -1


def extract_vital_value(vital_string):
    return float(vital_string.split(":")[1])


def display_dashboard(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")

    for index, patient in enumerate(patients, start=1):
        er_id, name, hr, temp = patient.split("|")

        print(
            f"{index}. [{er_id}] {name} | "
            f"Nhịp tim: {hr.split(':')[1]} bpm | "
            f"Nhiệt độ: {temp.split(':')[1]} °C"
        )

    print("-----------------------------------------------------------------")


def admit_patient(patients):
    print("--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ").strip().upper()

    if er_id == "":
        print("Mã ER không được để trống!")
        return

    if find_patient_index(patients, er_id) != -1:
        print("\nMã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()

    if name == "":
        print("\nTên bệnh nhân không được để trống!")
        return

    while True:
        hr = input("Nhập nhịp tim HR: ").strip()

        if hr.isdigit() and int(hr) > 0:
            break

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    while True:
        temp = input("Nhập nhiệt độ TEMP: ").strip()

        if temp.replace(".", "", 1).isdigit() and float(temp) >= 36.5:
            break

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

    patient = f"{er_id}|{name}|HR:{hr}|TEMP:{temp}"

    patients.append(patient)

    print("\nTiếp nhận ca cấp cứu mới thành công!")


def update_vitals(patients):
    print("--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    data = patients[index].split("|")

    print(f"Tìm thấy bệnh nhân: {data[1]}")
    print(f"Sinh hiệu hiện tại: {data[2]} | {data[3]}")
    print("Bạn muốn cập nhật:")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ")

    if choice == "1":
        hr = input("Nhập nhịp tim mới: ").strip()

        if not (hr.isdigit() and int(hr) > 0):
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return

        data[2] = f"HR:{hr}"
        patients[index] = "|".join(data)

        print("\nCập nhật nhịp tim thành công!")

    elif choice == "2":
        temp = input("Nhập nhiệt độ mới: ").strip()

        if not (
            temp.replace(".", "", 1).isdigit()
            and float(temp) >= 36.5
        ):
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
            return

        data[3] = f"TEMP:{temp}"
        patients[index] = "|".join(data)

        print("\nCập nhật nhiệt độ thành công!")

    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")


def trigger_red_alert(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    count = 0

    print("!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")

    for patient in patients:
        er_id, name, hr, temp = patient.split("|")

        hr_value = extract_vital_value(hr)
        temp_value = extract_vital_value(temp)

        if hr_value > 100 or temp_value >= 39.0:
            count += 1

            print(
                f"{count}. [{er_id}] {name} | "
                f"HR: {int(hr_value)} bpm | "
                f"TEMP: {temp_value} °C | "
                f"CẦN XỬ LÝ KHẨN CẤP"
            )

    if count == 0:
        print("--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
    else:
        print("-----------------------------------------------------")
        print(f"Tổng số ca nguy kịch: {count}")


def discharge_patient(patients):
    print("--- XUẤT VIỆN / CHUYỂN KHOA ---")

    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip().upper()

    if er_id == "":
        print("Mã ER không được để trống!")
        return

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    name = patients[index].split("|")[1]

    patients.pop(index)

    print(f"Đã chuyển khoa thành công cho bệnh nhân {name}!")


while True:
    print("""
===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====
1. Bảng theo dõi bệnh nhân
2. Tiếp nhận ca cấp cứu mới
3. Cập nhật lại sinh hiệu
4. BÁO ĐỘNG ĐỎ Lọc bệnh nhân nguy kịch
5. Xuất viện / Chuyển khoa
6. Thoát chương trình
=================================================
""")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        display_dashboard(er_patients)

    elif choice == "2":
        admit_patient(er_patients)

    elif choice == "3":
        update_vitals(er_patients)

    elif choice == "4":
        trigger_red_alert(er_patients)

    elif choice == "5":
        discharge_patient(er_patients)

    elif choice == "6":
        print("Kết thúc ca trực. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
