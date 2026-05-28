# Lỗi nằm ở dòng total_budget = salary

#     tác dụng là gán giá trị mới chứ không phải cộng dồn
# tác hại
#     Giá trị cũ bị mất hoàn toàn
#     Biến total_budget chỉ giữ lương của nhân viên nhập cuối cùng

# lỗi kinh điển
# Sai:    total = value
# Đúng:   total = total + value
# hoặc:   total += value
total_budget = 0

for i in range(1, 4):

    print(f"Đang xử lý nhân viên số {i}")
    salary = int(input("Nhập mức lương (VNĐ): "))
    total_budget += salary

print("\n=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:",
      total_budget, "VNĐ")
