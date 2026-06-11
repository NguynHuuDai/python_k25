raw_input_data = "nguyEN vAn a | python basic | rk-001 | student01@GMAIL.COM"

tickets = raw_input_data.split(",")

for current_ticket in tickets:
    parts = current_ticket.split("|")

    if len(parts) != 4:
        print("Dữ liệu đăng ký không hợp lệ")
    else:
        name = parts[0].strip().title()
        course = parts[1].strip().title()
        student_id = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ")
        elif len(student_id) < 5:
            print("Mã học viên không hợp lệ")
        else:
            course_code = course.upper().replace(" ", "-")
            confirm_code = student_id + "_" + course_code

            print("PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA")
            print(f"Học viên: {name}")
            print(f"Khóa học: {course}")
            print(f"Mã học viên: {student_id}")
            print(f"Email: {email}")
            print(f"Mã xác nhận: {confirm_code}")
            print("-" * 30)
