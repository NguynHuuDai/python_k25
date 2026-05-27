# Input: tuổi, huyết áp, đường huyết → kiểu int
# Output:
# “ĐỦ ĐIỀU KIỆN PHẪU THUẬT”
# “TỪ CHỐI PHẪU THUẬT”
# hoặc “Dữ liệu nhập vào không hợp lệ”


# C1: Gộp tất cả điều kiện bằng and
# C2: Dùng if lồng nhau

age = int(input("Nhập tuổi: "))
blood_pressure = int(input("Nhập huyết áp tâm thu: "))
blood_sugar = int(input("Nhập đường huyết: "))

if age < 0 or blood_pressure < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")

elif age < 75 and 90 <= blood_pressure <= 140 and blood_sugar < 150:
    print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")

else:
    print("TỪ CHỐI PHẪU THUẬT")
