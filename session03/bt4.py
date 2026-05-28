# Phân tích & Đề xuất giải pháp

# Input

# Người dùng nhập:

#     number_of_new_employees
#     Kiểu dữ liệu: int
#     Điều kiện hợp lệ
#     number_of_new_employees > 0
# Output

#     Nếu nhập sai:

#         [LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.

#     Nếu nhập đúng:

#         [THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản!
#     Đề xuất 2 giải pháp
#         Giải pháp 1 — while True
#             while True:
#             Chạy vô hạn
#             Nếu nhập đúng thì dùng break
#         Ưu điểm
#             Linh hoạt
#             Phổ biến
#         Nhược điểm
#             khó hiểu hơn
#         Giải pháp 2 — while có điều kiện
#             while number <= 0:
#             Chỉ lặp khi dữ liệu sai
#         Ưu điểm
#             Dễ đọc
#             Gần ngôn ngữ tự nhiên
#         Nhược điểm
#             Cần khởi tạo biến ban đầu
# Bảng so sánh
# Tiêu chí                while True      while có điều kiện
# Độ ngắn gọn	            Ngắn	        Hơi dài hơn
# Dễ hiểu	                Trung bình	    Dễ hiểu hơn 
# Phù hợp người mới học	Không tối ưu	Tốt hơn
# Chốt lựa chọn

# Chọn:

# while number_of_new_employees <= 0

# Lý do:

# Dễ hiểu
# Đúng logic nghiệp vụ
# Phù hợp người mới học
print("___ HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ___")

number_of_new_employees = 0

while number_of_new_employees <= 0:

    number_of_new_employees = int(
        input("Vui lòng nhập số lượng nhân sự mới trong tháng này: ")
    )

    if number_of_new_employees <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")

print(
    f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {number_of_new_employees} nhân sự mới!"
)

print("___ CHƯƠNG TRÌNH KẾT THÚC ___")
