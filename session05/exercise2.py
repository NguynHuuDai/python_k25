# Nguyên nhân lỗi biến total_students = 0 được khởi tạo bên ngoài vòng lặp for branch gây ra tình trạng
#  biến này tồn tại xuyên suốt từ đầu đến cuối chương trình và không bao giờ được "reset" (đặt lại) về 0 khi chương trình chuyển sang chi nhánh mới
# nên sau khi tính tổng nhánh đầu tiên biến total_students đã có giá trị lớn hơn 0 và khi tính sang nhánh 2 thì biến giữ nguyên giá trị từ nhánh 1

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
  
    total_students = 0

    print(f"\nNhập dữ liệu cho Chi nhánh {branch}:")

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count

   
    print(f"Chi nhánh {branch}: {total_students} học viên")
