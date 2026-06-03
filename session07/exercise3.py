raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


choice = ""
check = False
while choice != "4":
    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("\nChuỗi dữ liệu gốc:", raw_data)
    elif choice == "2":
        raw_data = raw_data.split("|")
        for i in range(len(raw_data)):
            raw_data[i] = raw_data[i].strip().split(";")

        for employee in raw_data:
            emp_id = employee[0].strip().upper()
            name = employee[1].strip().title()
            phone = employee[2].strip()
            department = employee[3].strip().upper()
            print(f"Mã nhân viên: {emp_id}\nHọ tên: {name}\nSố điện thoại: {phone}\nPhòng ban: {department}\n")
    elif choice == "3":
        search_id = input("Nhập mã ID nhân viên cần tìm: ").strip().upper()
        for i in range(len(raw_data)):
            for j in range(len(raw_data[i])):
                if raw_data[i][j] == search_id:
                    print(f"Nhân viên có mã ID {search_id} là: {raw_data[i][1].strip().title()}")
                    check = True
                    break
        if not check:
            print(f"Không tìm thấy nhân viên.")
   
                   
                