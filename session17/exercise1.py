student_management = [
    {
        "id": "SV001",
        "name": "Nguyen Van A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0,
        "avg": 8.17,
        "ranking": "Giỏi"
    }
]


def calculate_rank(avg):
    if avg < 5:
        return "Yếu"
    elif avg < 7:
        return "Trung bình"
    elif avg < 8:
        return "Khá"
    return "Giỏi"


def input_score(subject):
    while True:
        score = input(f"Nhập điểm {subject}: ")

        if score.replace(".", "", 1).isdigit():
            score = float(score)

            if 0 <= score <= 10:
                return score

        print("Điểm phải là số từ 0 đến 10!")

def print_menu():
    print("""
================ QUẢN LÝ SINH VIÊN ================
1. Hiển thị danh sách sinh viên
2. Tiếp nhận sinh viên
3. Cập nhật kết quả học tập
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Thống kê học lực
7. Thoát
""")


def print_list():
    if len(student_management) == 0:
        print("Danh sách sinh viên trống!")
        return

    print(
        f"{'ID':<8} {'Tên':<20} {'Toán':<8} {'Lý':<8} "
        f"{'Hóa':<8} {'TB':<8} {'Học lực'}"
    )

    for student in student_management:
        print(
            f"{student['id']:<8}"
            f"{student['name']:<20}"
            f"{student['math']:<8}"
            f"{student['physics']:<8}"
            f"{student['chemistry']:<8}"
            f"{student['avg']:<8.2f}"
            f"{student['ranking']}"
        )


def add_student():
    student_id = input("Nhập mã sinh viên: ").strip()

    if student_id == "":
        print("Mã sinh viên không được để trống!")
        return

    for student in student_management:
        if student["id"] == student_id:
            print("Mã sinh viên đã tồn tại!")
            return

    name = input("Nhập tên sinh viên: ").strip()

    if name == "":
        print("Tên sinh viên không được để trống!")
        return

    math = input_score("Toán")
    physics = input_score("Lý")
    chemistry = input_score("Hóa")

    avg = (math + physics + chemistry) / 3
    ranking = calculate_rank(avg)

    student_management.append({
        "id": student_id,
        "name": name,
        "math": math,
        "physics": physics,
        "chemistry": chemistry,
        "avg": round(avg, 2),
        "ranking": ranking
    })

    print("Thêm sinh viên thành công!")


def update_student():
    student_id = input("Nhập mã sinh viên cần cập nhật: ")

    for student in student_management:
        if student["id"] == student_id:
            math = input_score("Toán")
            physics = input_score("Lý")
            chemistry = input_score("Hóa")

            avg = (math + physics + chemistry) / 3

            student["math"] = math
            student["physics"] = physics
            student["chemistry"] = chemistry
            student["avg"] = round(avg, 2)
            student["ranking"] = calculate_rank(avg)

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy sinh viên!")


def delete_student():
    student_id = input("Nhập mã sinh viên cần xóa: ")

    for student in student_management:
        if student["id"] == student_id:

            confirm = input(
                "Bạn có chắc muốn xóa? (Y/N): "
            ).upper()

            if confirm == "Y":
                student_management.remove(student)
                print("Xóa thành công!")
            else:
                print("Đã hủy xóa!")

            return

    print("Không tìm thấy sinh viên!")


def search_student():
    keyword = input(
        "Nhập mã hoặc tên sinh viên: "
    ).lower()

    found = False

    print(
        f"{'ID':<8} {'Tên':<20} {'TB':<8} {'Học lực'}"
    )

    for student in student_management:
        if (
            keyword in student["id"].lower()
            or keyword in student["name"].lower()
        ):
            found = True

            print(
                f"{student['id']:<8}"
                f"{student['name']:<20}"
                f"{student['avg']:<8.2f}"
                f"{student['ranking']}"
            )

    if not found:
        print("Không tìm thấy sinh viên!")


def statistics_avg():
    excellent = 0
    good = 0
    average = 0
    weak = 0

    for student in student_management:
        if student["ranking"] == "Giỏi":
            excellent += 1
        elif student["ranking"] == "Khá":
            good += 1
        elif student["ranking"] == "Trung bình":
            average += 1
        else:
            weak += 1

    print("\n===== THỐNG KÊ HỌC LỰC =====")
    print(f"Giỏi       : {excellent}")
    print(f"Khá        : {good}")
    print(f"Trung bình : {average}")
    print(f"Yếu        : {weak}")




while True:
    print_menu()

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        print_list()

    elif choice == "2":
        add_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        search_student()

    elif choice == "6":
        statistics_avg()

    elif choice == "7":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
