# input() trong Python luôn trả về kiểu str, nên nhập 65.5 thì dữ liệu vẫn được lưu dưới dạng chuỗĩ nên các phép tính ko thực hiện được

print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")

name_patient = input("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân : ")) # đã ép sang float

print("=== KIỂM TRA DỮ LIỆU LƯU TRỮ ===")
print("Bệnh nhân :", name_patient)
print("Cân nặng đã nhập :", weight)

print("CẢNH BÁO - Kiểu dữ liệu đang lưu là :", type(weight))
