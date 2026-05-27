

 

 # chương trình không bị crash khi người dùng nhập sai kiểu dữ liệu nhưng vấn đề lỗi logic vẫn tồn tại
 # vấn đề gặp phải là khi người dùng nhập sai kiểu dữ liệu, chương trình sẽ không bị crash nhưng sẽ không hoạt động đúng như mong đợi
print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ')
name = input("Nhập họ tên bệnh nhân: ")
age = input("Nhập tuổi: ")
symptom = input("Nhập triệu chứng: ")

print("\n --- PHIẾU KHÁM BỆNH --- ")
print("Họ tên bệnh nhân:", name)
print("Tuổi:", age)
print("Triệu chứng:", symptom)
