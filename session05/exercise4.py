# input :
#     num_branches: Số lượng chi nhánh
#     student_count: Số học viên đi học
# Output: Trạng thái lớp học dựa trên số học viên
# Đề xuất giải pháp
#     Vòng lặp: Sử dụng vòng lặp lồng nhau: vòng ngoài duyệt chi nhánh, vòng trong duyệt lớp.

# Xử lý dữ liệu:

#     Sử dụng vòng lặp while để yêu cầu nhập lại nếu người dùng nhập số âm.

#     Sử dụng cấu trúc if -elif -else để phân loại trạng thái lớp học dựa trên ngưỡng 20 học viên.

#     Sử dụng lệnh break  để thoát khỏi vòng nhập dữ liệu khi đã có dữ liệu hợp lệ.

# Thuật toán:

# Nhập num_branches.


# Vòng lặp branch từ 1 đến num_branches:
# a. Vòng lặp class từ 1 đến 2:
# i. Dùng while True để nhập student_count.
# ii. Nếu student_count < 0, báo lỗi và lặp lại.
# iii. Nếu student_count == 0, in thông báo vắng toàn bộ, kết thúc nhập lớp này.
# iv. Nếu student_count >= 20, in "Lớp học ổn định".
# v. Nếu 0 < student_count < 20, in "Lớp cần nhắc nhở".

num_branches = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, num_branches + 1):
    print(f"\nChi nhánh {branch}:")

    for classroom in range(1, 3):
        student_count = -1

        while student_count < 0:
            student_count = int(
                input(f"Nhập số học viên đi học của lớp {classroom}: "))

            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")

        if student_count == 0:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
        elif student_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp học ổn định")
        else:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: Lớp cần được nhắc nhở theo dõi")
