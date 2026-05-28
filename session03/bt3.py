# input 
# employee_id → kiểu string
# full_name → kiểu string
# department → kiểu string

# output 

# Mã nhân viên: NV001
# Họ tên: Nguyễn Văn A
# Phòng ban: IT


# Trường hợp không hợp lệ
# Nếu mã hoặc tên:
# + rỗng ""
# + chỉ chứa khoảng trắng " "

# Hiển thị:

# [CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.

# đề xuất dùng for để lặp 3 lần

print("===== HỆ THỐNG NHẬP LIỆU NHÂN SỰ =====")

for employee_number in range(1, 4):

    print(f"\n--- Nhập thông tin nhân viên số {employee_number} ---")

    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")

    if employee_id == "" or full_name == "":
        print(
            "\n[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        continue

    print("\n===== HỒ SƠ NHÂN SỰ ĐIỆN TỬ =====")
    print("Mã nhân viên :", employee_id)
    print("Họ và tên    :", full_name)
    print("Phòng ban    :", department)
    print("=================================")

print("\nĐã hoàn tất quy trình onboarding cho 3 nhân viên!")
