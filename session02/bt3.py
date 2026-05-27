# Input(Dữ liệu đầu vào):

# patient_name str: Họ và tên của bệnh nhân.

# patient_age int Tuổi của bệnh nhân.

# Output(Dữ liệu đầu ra):

# Trường hợp dữ liệu lỗi: Thông báo lỗi trực quan và dừng chương trình, không in phiếu.

# Trường hợp dữ liệu hợp lệ: In ra Phiếu khám bệnh điện tử chứa thông tin hành chính và kết quả phân luồng ưu tiên.
import sys

print("--- KHỞI TẠO & PHÂN LUỒNG BỆNH ÁN SỐ ---")
patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))

name_clean = patient_name.strip()


if name_clean == "" or patient_age < 0 or patient_age > 150:
    print("\nLỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()


if patient_age < 6:
    triage_result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif patient_age >= 80:
    triage_result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    triage_result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print("\n" + "═"*20 + " PHIẾU KHÁM BỆNH ĐIỆN TỬ " + "═"*20)
print(f" Họ và tên bệnh nhân : {name_clean.upper()}")
print(f" Tuổi                : {patient_age} tuổi")
print(f" Trạng thái phân loại: {triage_result}")
print("═"*65)
