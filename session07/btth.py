raw_input = "   nGuyen vaN aN  ;  2004   "

choice = ""
while choice != "4":
    print("===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")
    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("\nChuỗi dữ liệu gốc:", raw_input)
    elif choice == "2":
        raw_input = raw_input.strip()
        parts = raw_input.split(";")
        name = parts[0].strip()
        birth_year = 2026 - int(parts[1].strip())
        name_parts = name.split()
        
        # sau khi tách thì hiện tại name là nguyen van an còn năm sinh là parts[1]
        print("Họ tên chuẩn hóa:", name.title())
        print("Tuổi:", birth_year)
    elif choice == "3":
        id = name_parts[-1].upper() + parts[1].strip()[-2:]
        print("Mã ID tự động:", id)
        email = name_parts[0].lower() + name_parts[1].lower() + name_parts[2].lower() + "@company.com"
        print("Email tự động:", email)
