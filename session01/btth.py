import random


name = input("Nhập tên bệnh nhân: ")
sex = input("Nhập giới tính bệnh nhân: ")
age = int(input("Nhập năm sinh bệnh nhân: "))
phone_number = input("Nhập số điện thoại bệnh nhân: ")
email = input("Nhập email bệnh nhân: ")
symptom = input("Nhập triệu chứng bệnh nhân: ")
cost = float(input("Nhập chi phí khám bệnh: "))

#Mã bệnh nhân 2 chữ cái viết hoa + năm sinh + 3 số ngẫu nhiên
id = "BN" + str(age) + str(random.randint(100, 999))


#message = f"--- THẺ BỆNH NHÂN ---\nMã bệnh nhân: {id}\n\n\nTên: {name}\nGiới tính: {sex}\nNăm sinh: {age}\nSố điện thoại: {phone_number}\nEmail: {email}\nTriệu chứng: {symptom}\nChi phí khám bệnh: {cost}\n"
infomation = f"--- THÔNG TIN BỆNH NHÂN ---\nMã bệnh nhân: {id}\n\n\nTên: {name}\nGiới tính: {sex}\nNăm sinh: {age}\nSố điện thoại: {phone_number}\nEmail: {email}\nTriệu chứng: {symptom}\nChi phí khám bệnh: {cost}\n"
#print(message)
print(infomation)