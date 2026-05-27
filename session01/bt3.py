# phân tích input: họ tên, mã bệnh án, khoa phòng khám kiểu dữ liệu str
# output : bệnh nhân, mã, phòng chuyển tới

print("=== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ===")

name = input("Nhập họ tên bệnh nhân: ")
medical_id = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám: ")

print("\n=== PHIẾU KHÁM BỆNH ===")
print(f"Bệnh nhân: {name} - Mã BA: {medical_id} - Chuyển tới: {department}")
