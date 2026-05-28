# phân tích lỗi
# khi working_days = 0
# Chương trình vào nhánh:

# if working_days == 0:
#     print("CẢNH BÁO...")
#  sau đó sẽ tiếp tục chạy đến dòng:
# bonus_amount = working_days * 200000
# print("Đã gửi Email...")
# nên hệ thông sẽ gửi email thưởng = 0
# lỗi : thiếu lệnh điều hướng vòng lặp, chỉ tạo cảnh báo nhưng ko giải quyết vấn đề

print("___ HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ___")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("___ Đang xử lý nhân viên số", employee_number, "___")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))

    # Kiểm tra điều kiện
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        print("__________________________________________\n")
        continue

    bonus_amount = working_days * 200000
    print("→ Đã gửi Email: Chúc mừng nhận được",
          bonus_amount, "VNĐ tiền thưởng!")
    print("__________________________________________\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")
