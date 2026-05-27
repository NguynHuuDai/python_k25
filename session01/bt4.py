# Input từ input() ban đầu đều là str
# Output mong muốn:
# Nhiệt độ : float
# Nhịp tim : int

# có 2 cách ép kiểu
# cách 1: Ép kiểu trực tiếp float(input()), int(input())
# bộ nhớ ít hơn, ngắn gọn nhưng khó sửa nếu gặp lỗi

# cách 2: Lưu vào biến chuỗi rồi mới ép kiểu
# bộ nhớ dài hơn, code dài hơn nhưng dễ sửa lỗi hơn

print("--- HỆ THỐNG CHUẨN HÓA SINH HIỆU ---")

patient_id = input("Nhập mã bệnh nhân: ")
temperature = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))

print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", patient_id)

print("Nhiệt độ cơ thể:", temperature, "độ C")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))

print("Nhịp tim:", heart_rate, "nhịp/phút")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))

print("\nThông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")
