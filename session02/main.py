# toán tử số học
first_number = 10
second_number = 3

print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")


age = 18
if age >= 18:
    print("Bạn đủ tuổi để lái xe.")
else:
    print("Bạn chưa đủ tuổi để lái xe.")


gender = "Male"

if gender == "Male":
    print("Bạn là nam.")
elif gender == "Female":
    print("Bạn là nữ.")
else:
    print("Giới tính không xác định.")  


# trường hợp bài toán có 2 điều kiện trở lên
avg_point = 8.5

if avg_point >= 9 and avg_point <= 10:
    print("Học sinh giỏi.")
elif avg_point >= 7 and avg_point < 9:
    print("Học sinh khá.")
elif avg_point >= 5 and avg_point < 7:
    print("Học sinh trung bình.")
else:
    print("Học sinh yếu.")

status = "ACTIVE" # có thể là ACTIVE, INACTIVE, PENDING
match status:
    case "ACTIVE":
        print("Đang hoạt động")
    case "INACTIVE":
        print("Đã ngừng hoạt động")
    case "PENDING":
        print("Đang chờ xử lý")


my_age = 18

# độ cận
nearsightedness = 5

if my_age >= 18:
    if nearsightedness > 3:
        print("Bạn đủ tuổi để lái xe nhưng độ cận cao. Kết luận ko đạt")
    else:
        print("Bạn đủ tuổi để lái xe và độ cận thấp. Kết luận đạt")
else:
    print("Bạn chưa đủ tuổi để lái xe.")


# toán tử 3 ngôi

#gender = "FEMALE"
print(f" {'nam' if gender == 'MALE' else 'nữ'}")