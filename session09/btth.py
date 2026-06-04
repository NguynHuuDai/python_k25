branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu",
                "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]

daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]

target_achieved = [True, True, False, True, False]

choice = ""

while choice != "4":
    print("""
===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
""")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("\n--- BÁO CÁO DOANH THU TỔNG HỢP ---")
        print("Tên Cơ Sở               | Doanh Thu   | Trạng Thái")
        print("--------------------------------------------------------")

        for i in range(len(branch_names)):
            print(
                f"{branch_names[i]:25} | {daily_revenues[i]:10} | {'Đạt' if target_achieved[i] else 'Không Đạt'}"
            )

        print("--------------------------------------------------------")
        print(f"=> TỔNG DOANH THU TOÀN VÙNG: {sum(daily_revenues)} VND")

    elif choice == "2":
        max_revenue = max(daily_revenues)
        min_revenue = min(daily_revenues)

        max_index = daily_revenues.index(max_revenue)
        min_index = daily_revenues.index(min_revenue)

        print("\n--- THỐNG KÊ CHI NHÁNH CAO NHẤT / THẤP NHẤT ---")

        print(f"Cao nhất: {branch_names[max_index]}")
        print(f"Doanh thu: {max_revenue} VND")

        print()

        print(f"Thấp nhất: {branch_names[min_index]}")
        print(f"Doanh thu: {min_revenue} VND")

    elif choice == "3":
        failed_branches = []

        for i in range(len(target_achieved)):
            if target_achieved[i] == False:
                failed_branches.append(branch_names[i])

        print("\n--- DANH SÁCH CƠ SỞ CẦN HỖ TRỢ TRA CỨU ĐƯỢC ---")
        print(failed_branches)

    elif choice == "4":
        print("\nHệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")

    else:
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")
