choice = ""
user = ""
title = ""
description = ""
hashtag = ""

while choice != "5":
    print("HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK")
    print("1. Nhập và phân tích thông tin video")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra tính hợp lệ của hashtag")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")

    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ Vui lòng nhập lại")
        choice = ""
        continue

    if choice == "1":
        temp_user = input("Nhập tên tài khoản người đăng video: ")
        if not temp_user.strip():
            print("Lỗi Tên tài khoản không được rỗng")
            continue
        user = temp_user

        title = input("Nhập tiêu đề video: ")

        temp_description = input("Nhập mô tả video: ")
        if not temp_description.strip():
            print("Lỗi Mô tả video không được rỗng")
            continue
        description = temp_description

        hashtag = input("Nhập vào danh sách hashtag cách nhau bởi dấu phẩy: ")

        print("BÁO CÁO THỐNG KÊ")
        print(f"Tên tài khoản: {user.strip()}")

        clean_title = " ".join(title.strip().split()).title()
        print(f"Tiêu đề: {clean_title}")

        clean_desc = description.strip()
        print(f"Mô tả: {clean_desc}")
        print(f"Độ dài mô tả: {len(clean_desc)}")
        print(f"Số lượng từ trong mô tả: {len(clean_desc.split())}")

        clean_hashtag = hashtag.strip()
        print(f"Danh sách hashtag hiện tại: {clean_hashtag}")

        if not clean_hashtag:
            hashtag_count = 0
        else:
            hashtag_count = clean_hashtag.count(",") + 1
        print(f"Số lượng hashtag: {hashtag_count}")

        print(f"Mô tả chữ thường: {clean_desc.lower()}")
        print(f"Mô tả chữ hoa: {clean_desc.upper()}")

    elif choice == "2":
        if not user:
            print("Vui lòng chạy Chức năng 1 để nhập tên tài khoản trước")
            continue

        old_name = user
        new_name = "@" + user.strip().lower()
        print(f"Tên tài khoản trước khi chuẩn hóa: {old_name}")
        print(f"Tên tài khoản sau khi chuẩn hóa: {new_name}")

    elif choice == "3":
        new_hashtag = input("Nhập vào hashtag mới: ").strip()

        if new_hashtag == "":
            print("Lỗi Hashtag không được rỗng")
        elif new_hashtag[0] != "#":
            print("Lỗi Hashtag phải bắt đầu bằng #")
        elif " " in new_hashtag:
            print("Lỗi Hashtag không được chứa khoảng trắng")
        elif len(new_hashtag) < 2:
            print("Lỗi Hashtag quá ngắn")
        else:
            content = new_hashtag[1:]
            is_valid = True
            for char in content:
                if not (char.isalnum() or char == "_"):
                    is_valid = False
                    break

            if is_valid:
                print("Hashtag hợp lệ")
                if hashtag.strip() == "":
                    hashtag = new_hashtag
                else:
                    hashtag = hashtag.strip() + ", " + new_hashtag
                print(f"Chuỗi hashtag cập nhật: {hashtag}")
            else:
                print("Lỗi Hashtag chỉ được chứa chữ số và dấu gạch dưới")

    elif choice == "4":
        if not description:
            print("Vui lòng chạy Chức năng 1 để nhập mô tả video trước")
            continue

        search_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")

        if search_keyword in description:
            count = description.count(search_keyword)
            description = description.replace(search_keyword, replace_keyword)
            print(f"Tìm thấy từ khóa xuất hiện {count} lần")
            print(f"Mô tả sau khi thay thế: {description}")
        else:
            print("Không tìm thấy từ khóa")

    elif choice == "5":
        print("Thoát chương trình")
