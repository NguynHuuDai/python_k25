def display_orders(orders):
    if len(orders) == 0:
        print("\nDanh sach don hang trong!\n")
        return

    print("\n{:<10} {:<25} {:>15} {:<10}".format(
        "Ma HD", "Ten Dai Ly", "Gia Tri", "Trang Thai"
    ))
    print("-" * 65)

    for order in orders:
        print("{:<10} {:<25} {:>15,} {:<10}".format(
            order["id"],
            order["name"],
            order["price"],
            order["status"]
        ))
    print()


def input_order_id():
    while True:
        order_id = input("Nhap ma don hang: ").strip()

        if order_id == "":
            print("Ma don hang khong duoc de trong!")
            continue

        return order_id


def input_agency_name():
    while True:
        name = input("Nhap ten dai ly: ").strip()

        if name == "":
            print("Ten dai ly khong duoc de trong!")
            continue

        return name


def input_order_price():
    while True:
        price = input("Nhap gia tri don hang: ").strip()

        if not price.isdigit():
            print("Gia tri don hang phai la so nguyen duong!")
            continue

        price = int(price)

        if price <= 0:
            print("Gia tri don hang phai lon hon 0!")
            continue

        return price


def add_order(orders):
    print("\n===== THEM MOI DON HANG =====")

    order_id = input_order_id()

    for order in orders:
        if order["id"].lower() == order_id.lower():
            print("ERR-01: Ma don hang da ton tai!\n")
            return

    name = input_agency_name()
    price = input_order_price()

    new_order = {
        "id": order_id,
        "name": name,
        "price": price,
        "status": "Unpaid"
    }

    orders.append(new_order)

    print("Them moi don hang thanh cong!\n")


def update_payment_status(orders):
    print("\n===== CAP NHAT THANH TOAN =====")

    order_id = input("Nhap ma don hang can cap nhat: ").strip()

    for order in orders:
        if order["id"].lower() == order_id.lower():

            if order["status"] == "Paid":
                print("ERR-04: Don hang da duoc thanh toan truoc do!\n")
                return

            order["status"] = "Paid"
            print("Cap nhat trang thai thanh toan thanh cong!\n")
            return

    print("ERR-03: Khong tim thay ma don hang!\n")


def calculate_revenue(orders):
    total_revenue = 0

    for order in orders:
        if order["status"] == "Paid":
            total_revenue += order["price"]

    discount_percent = 0

    if total_revenue >= 100000000:
        discount_percent = 5

    discount_amount = total_revenue * discount_percent / 100

    return total_revenue, discount_percent, discount_amount


def show_revenue_report(orders):
    total_revenue, discount_percent, discount_amount = calculate_revenue(
        orders
    )

    print("\n===== BAO CAO DOANH THU =====")
    print(f"Tong doanh thu thuc te : {total_revenue:,} VND")
    print(f"Ty le chiet khau      : {discount_percent}%")
    print(f"Tien chiet khau       : {discount_amount:,.0f} VND\n")


def show_menu():
    print("========== AGENCY ORDER MANAGEMENT ==========")
    print("1. Xem danh sach don hang")
    print("2. Tao moi don hang")
    print("3. Cap nhat trang thai thanh toan")
    print("4. Tinh tong doanh thu va chiet khau")
    print("5. Thoat")
    print("=============================================")


def input_menu_choice():
    while True:
        choice = input("Nhap lua chon cua ban: ").strip()

        if not choice.isdigit():
            print("Vui long nhap so tu 1 den 5!")
            continue

        choice = int(choice)

        if choice < 1 or choice > 5:
            print("Vui long nhap so tu 1 den 5!")
            continue

        return choice


def main():
    orders = [
        {
            "id": "HD01",
            "name": "Dai ly Hoang Long",
            "price": 45000000,
            "status": "Paid"
        },
        {
            "id": "HD02",
            "name": "Tap hoa Minh Thu",
            "price": 15000000,
            "status": "Unpaid"
        }
    ]

    while True:
        show_menu()

        choice = input_menu_choice()

        if choice == 1:
            display_orders(orders)

        elif choice == 2:
            add_order(orders)

        elif choice == 3:
            update_payment_status(orders)

        elif choice == 4:
            show_revenue_report(orders)

        elif choice == 5:
            print("\nCam on ban da su dung chuong trinh!")
            break


main()
