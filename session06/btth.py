

laptop = 0
phone = 0
tablet = 0

while True:
    print("\n===== MENU QUẢN LÝ KHO =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    # Xem báo cáo tồn kho
    if choice == "1":
        print("\n===== BÁO CÁO TỒN KHO =====")
        print("Laptop:", laptop)
        print("Phone:", phone)
        print("Tablet:", tablet)

        print("\nBiểu đồ tồn kho:")
        print("Laptop (" + str(laptop) + "): ", end="")
        for i in range(laptop):
            print("*", end="")
        print()

        print("Phone (" + str(phone) + "): ", end="")
        for i in range(phone):
            print("*", end="")
        print()

        print("Tablet (" + str(tablet) + "): ", end="")
        for i in range(tablet):
            print("*", end="")
        print()

    # Nhập kho
    elif choice == "2":
        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = input("Chọn mặt hàng: ")

        quantity = -1
        while quantity < 0:
            quantity = int(input("Nhập số lượng: "))
            if quantity < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")

        if product == "1":
            laptop += quantity
            print("Nhập kho Laptop thành công!")

        elif product == "2":
            phone += quantity
            print("Nhập kho Phone thành công!")

        elif product == "3":
            tablet += quantity
            print("Nhập kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

    # Xuất kho
    elif choice == "3":
        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = input("Chọn mặt hàng: ")

        quantity = -1
        while quantity < 0:
            quantity = int(input("Nhập số lượng: "))
            if quantity < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")

        if product == "1":
            if quantity > laptop:
                print("Không đủ hàng!")
            else:
                laptop -= quantity
                print("Xuất kho Laptop thành công!")

        elif product == "2":
            if quantity > phone:
                print("Không đủ hàng!")
            else:
                phone -= quantity
                print("Xuất kho Phone thành công!")

        elif product == "3":
            if quantity > tablet:
                print("Không đủ hàng!")
            else:
                tablet -= quantity
                print("Xuất kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

    # Cảnh báo tồn kho thấp
    elif choice == "4":
        print("\n===== CẢNH BÁO TỒN KHO =====")

        if laptop < 10:
            print("[CẢNH BÁO] Laptop sắp hết (Chỉ còn", laptop, "sản phẩm)")

        if phone < 10:
            print("[CẢNH BÁO] Phone sắp hết (Chỉ còn", phone, "sản phẩm)")

        if tablet < 10:
            print("[CẢNH BÁO] Tablet sắp hết (Chỉ còn", tablet, "sản phẩm)")

    # Thoát chương trình
    elif choice == "5":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
