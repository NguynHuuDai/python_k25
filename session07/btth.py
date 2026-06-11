raw_input = "   nGuyen vaN aN  ;  2004   "

parts = raw_input.split(";")
name = parts[0].strip()
birth_year = 2026 - int(parts[1].strip())
name_parts = name.split()

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
        print("Họ tên chuẩn hóa:", name.title())
        print("Tuổi:", birth_year)

    elif choice == "3":
        id = name_parts[-1].upper() + parts[1].strip()[-2:]
        print("Mã ID tự động:", id)

        email_prefix = ""
        for word in name_parts[:-1]:
            email_prefix += word[0].lower()  

        email = email_prefix + name_parts[-1].lower() + "@company.com"
        print("Email tự động:", email)

        print("\n--- THẺ THÀNH VIÊN ---")
        print("Mã số:", id)
        print("Họ tên:", name.title())
        print("Email:", email)
        print("----------------------")

    elif choice == "4":
        print("\nChương trình kết thúc. Cảm ơn và hẹn gặp lại!")
