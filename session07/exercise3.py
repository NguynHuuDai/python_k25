raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

employees_list = raw_data.split("|")
for i in range(len(employees_list)):
    parts = employees_list[i].strip().split(";")

    emp_id = parts[0].strip().upper()
    name = parts[1].strip().title()

    phone_raw = parts[2].strip()
    phone_clean = ""
    for char in phone_raw:
        if char.isdigit():
            phone_clean += char

    department = parts[3].strip().upper()

    employees_list[i] = [emp_id, name, phone_clean, department]

choice = ""
while choice != "4":
    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if choice == "1":
        print("\nChuỗi dữ liệu gốc:", raw_data)

    elif choice == "2":
        print("\n--- BÁO CÁO NHÂN SỰ ---")
        for employee in employees_list:
            print(f"Mã nhân viên: {employee[0]}")
            print(f"Họ tên: {employee[1]}")
            print(f"Số điện thoại: {employee[2]}")
            print(f"Phòng ban: {employee[3]}")
            print("-" * 25)

    elif choice == "3":
        search_id = input("Nhập mã ID nhân viên cần tìm: ").strip().upper()
        check = False

        for employee in employees_list:
            if employee[0] == search_id:
                print(
                    f"\n[KẾT QUẢ TÌM KIẾM] Nhân viên có mã ID {search_id} là: {employee[1]}")
                check = True
                break

        if not check:
            print(f"\nKhông tìm thấy nhân viên có mã ID: {search_id}")

    elif choice == "4":
        print("\nChương trình kết thúc. Cảm ơn và hẹn gặp lại!")

    else:
        print("\nLựa chọn không hợp lệ. Vui lòng nhập lại từ 1 đến 4!")
