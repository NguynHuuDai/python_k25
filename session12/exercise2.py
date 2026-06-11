saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Nhập lựa chọn (1-7): ").strip()

    if choice == "1":
        if not saving_accounts:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("\nDanh sách sổ tiết kiệm:")
            for idx, account in enumerate(saving_accounts, start=1):
                print(
                    f"{idx}. Mã sổ: {account['account_id']} | "
                    f"Khách hàng: {account['customer_name']} | "
                    f"Số tiền gửi: {account['balance']} | "
                    f"Kỳ hạn: {account['term_months']} tháng | "
                    f"Lãi suất: {account['interest_rate']}%/năm | "
                    f"Trạng thái: {account['status']}"
                )

    elif choice == "2":
        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        if not account_id:
            print("Mã sổ tiết kiệm không được để trống!")
            continue

        is_duplicate = False
        for account in saving_accounts:
            if account["account_id"] == account_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue

        customer_name = input("Nhập tên khách hàng: ").strip()
        if not customer_name:
            print("Tên khách hàng không được để trống")
            continue

        balance_raw = input("Nhập số tiền gửi: ").strip()
        term_months_raw = input("Nhập kỳ hạn gửi theo tháng: ").strip()
        if (not balance_raw.isdigit() or int(balance_raw) <= 0 or
                not term_months_raw.isdigit() or int(term_months_raw) <= 0):
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue

        interest_rate_raw = input("Nhập lãi suất năm: ").strip()
        if (interest_rate_raw.count(".") > 1 or
            not interest_rate_raw.replace(".", "", 1).isdigit() or
                float(interest_rate_raw) <= 0):
            print("Lãi suất không hợp lệ!")
            continue

        saving_accounts.append({
            "account_id": account_id,
            "customer_name": customer_name,
            "balance": int(balance_raw),
            "term_months": int(term_months_raw),
            "interest_rate": float(interest_rate_raw),
            "status": "active"
        })
        print("Mở sổ tiết kiệm thành công!")

    elif choice == "3":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

        target_account = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                target_account = account
                break

        if target_account is None:
            print("Không tìm thấy mã sổ tiết kiệm!")
            continue

        if target_account["status"] == "closed":
            print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
            continue

        customer_name = input("Nhập tên khách hàng mới: ").strip()
        if not customer_name:
            print("Tên khách hàng không được để trống")
            continue

        balance_raw = input("Nhập số tiền gửi mới: ").strip()
        term_months_raw = input("Nhập kỳ hạn mới theo tháng: ").strip()
        if (not balance_raw.isdigit() or int(balance_raw) <= 0 or
                not term_months_raw.isdigit() or int(term_months_raw) <= 0):
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue

        interest_rate_raw = input("Nhập lãi suất năm mới: ").strip()
        if (interest_rate_raw.count(".") > 1 or
            not interest_rate_raw.replace(".", "", 1).isdigit() or
                float(interest_rate_raw) <= 0):
            print("Lãi suất không hợp lệ!")
            continue

        target_account["customer_name"] = customer_name
        target_account["balance"] = int(balance_raw)
        target_account["term_months"] = int(term_months_raw)
        target_account["interest_rate"] = float(interest_rate_raw)
        print("Cập nhật thành công!")

    elif choice == "4":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()

        target_account = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                target_account = account
                break

        if target_account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue

        target_account["status"] = "closed"
        print("Tất toán thành công!")

    elif choice == "5":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

        target_account = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                target_account = account
                break

        if target_account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue

        if target_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue

        interest = target_account["balance"] * (
            target_account["interest_rate"] / 100) * (target_account["term_months"] / 12)
        total_received = target_account["balance"] + interest

        print(f"Tiền lãi dự kiến: {interest:.2f}")
        print(f"Tổng tiền nhận khi đến hạn: {total_received:.2f}")

    elif choice == "6":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()

        target_account = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                target_account = account
                break

        if target_account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue

        if target_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue

        actual_months_raw = input("Nhập số tháng thực gửi: ").strip()
        if not actual_months_raw.isdigit() or int(actual_months_raw) <= 0:
            print("Số tháng thực gửi không hợp lệ!")
            continue

        actual_months = int(actual_months_raw)

        if actual_months < target_account["term_months"]:
            applied_rate = 0.5
            print("Khách hàng rút trước hạn (Áp dụng lãi suất không kỳ hạn: 0.5%/năm)")
        else:
            applied_rate = target_account["interest_rate"]
            print(
                f"Khách hàng đủ điều kiện hưởng lãi đúng hạn (Áp dụng lãi suất kỳ hạn: {applied_rate}%/năm)")

        interest = target_account["balance"] * \
            (applied_rate / 100) * (actual_months / 12)
        total_received = target_account["balance"] + interest

        print(f"Tiền lãi thực nhận: {interest:.2f}")
        print(f"Tổng tiền thực nhận: {total_received:.2f}")

    elif choice == "7":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
