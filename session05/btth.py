quantity = int(input("Nhập số lượng nhân viên: "))

for i in range(quantity):
    name = input(f"Nhập tên nhân viên: ")
    working_date = int(input(f"Nhập số ngày làm: "))
    if working_date < 0 or working_date > 22:
        print("Số ngày làm không hợp lệ")
        continue
    elif working_date == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
    elif working_date >= 18:
        print(f"{name}: {'*'*working_date} \nLàm việc chăm chỉ")
    elif working_date < 10:
        print(f"{name}: {'*'*working_date} \nLàm việc ít")
    else:
        print(f"{name}: {'*'*working_date} \nLàm việc bình thường")
    
