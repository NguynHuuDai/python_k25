choice = ""
shop_name = ""
product_name = ""
description = ""
category = ""
keywords = ""

while choice != "5":
    print("HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE")
    print("1. Nhập và phân tích thông tin sản phẩm")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra tính hợp lệ của mã giảm giá")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
    print("5. Thoát chương trình")

    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ Vui lòng nhập lại")
        choice = ""
        continue

    if choice == "1":
        temp_shop = input("Nhập tên shop: ")
        if not temp_shop.strip():
            print("Lỗi Tên shop không được bỏ trống")
            continue
        shop_name = temp_shop

        product_name = input("Nhập tên sản phẩm: ")

        temp_description = input("Nhập mô tả sản phẩm: ")
        if not temp_description.strip():
            print("Lỗi Mô tả sản phẩm không được rỗng")
            continue
        description = temp_description

        category = input("Nhập danh mục sản phẩm: ")
        keywords = input(
            "Nhập danh sách từ khóa tìm kiếm cách nhau bởi dấu phẩy: ")

        print("BÁO CÁO THỐNG KÊ SẢN PHẨM")
        print(f"Tên shop: {shop_name.strip()}")

        clean_product = " ".join(product_name.strip().split()).title()
        print(f"Tên sản phẩm: {clean_product}")

        clean_desc = description.strip()
        print(f"Mô tả sản phẩm: {clean_desc}")
        print(f"Độ dài mô tả sản phẩm: {len(clean_desc)} ký tự")

        clean_category = " ".join(category.strip().split()).lower()
        print(f"Danh mục sản phẩm: {clean_category}")

        clean_keywords = keywords.strip()
        print(f"Danh sách từ khóa: {clean_keywords}")

        if not clean_keywords:
            keyword_count = 0
        else:
            keyword_count = clean_keywords.count(",") + 1
        print(f"Số lượng từ khóa tìm kiếm: {keyword_count}")

        print(f"Mô tả chữ thường: {clean_desc.lower()}")
        print(f"Mô tả chữ hoa: {clean_desc.upper()}")

    elif choice == "2":
        if not shop_name:
            print("Vui lòng chạy Chức năng 1 để nhập tên shop trước")
            continue

        old_shop = shop_name

        clean_words = shop_name.strip().lower().split()
        normalized_name = "-".join(clean_words)

        if not normalized_name.startswith("shop-"):
            normalized_name = "shop-" + normalized_name

        print(f"Tên shop ban đầu: {old_shop}")
        print(f"Tên shop sau khi được chuẩn hóa: {normalized_name}")

    elif choice == "3":
        voucher_code = input("Nhập mã giảm giá cần kiểm tra: ").strip()

        if voucher_code == "":
            print("Lỗi Mã giảm giá không được rỗng")
        elif " " in voucher_code:
            print("Lỗi Mã giảm giá không được chứa khoảng trắng")
        elif len(voucher_code) < 6 or len(voucher_code) > 12:
            print("Lỗi Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
        elif not voucher_code.isupper():
            print("Lỗi Mã giảm giá phải được viết hoa toàn bộ")
        elif not voucher_code.isalnum():
            print("Lỗi Mã giảm giá chỉ được chứa chữ cái và chữ số")
        elif not voucher_code.startswith("SALE"):
            print("Lỗi Mã giảm giá phải bắt đầu bằng chuỗi SALE")
        else:
            print("Mã giảm giá hợp lệ")

    elif choice == "4":
        if not description:
            print("Vui lòng chạy Chức năng 1 để nhập mô tả sản phẩm trước")
            continue

        search_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")

        if search_keyword in description:
            count = description.count(search_keyword)
            description = description.replace(search_keyword, replace_keyword)
            print(f"Số lần xuất hiện của từ khóa: {count}")
            print(f"Mô tả sau khi thay thế: {description}")
        else:
            print("Không tìm thấy từ khóa cần tìm trong mô tả sản phẩm")

    elif choice == "5":
        print("Thoát chương trình")
