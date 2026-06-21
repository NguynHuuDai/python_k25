import logging

from pos_logic import (
    view_menu,
    add_to_order,
    view_order,
    checkout,
    ItemNotFoundError,
    InvalidQuantityError
)

current_order = []


def print_menu():
    """Display main menu."""

    print("""
========== HIGHLANDS MINI POS ==========
1. Xem thuc don
2. Them mon vao gio
3. Xem gio hang & Tinh tong tien
4. Thanh toan & Xoa gio hang
5. Thoat ca lam viec
========================================
""")


while True:
    print_menu()

    choice = input(
        "Chon chuc nang (1-5): "
    ).strip()

    if choice == "1":
        view_menu()

    elif choice == "2":

        print("\n--- THEM MON VAO GIO ---")

        try:
            drink_code = input(
                "Nhap ma do uong: "
            )

            quantity = int(
                input("Nhap so luong: ")
            )

            drink_name = add_to_order(
                current_order,
                drink_code,
                quantity
            )

            print(
                f"Da them {quantity} x "
                f"{drink_name} vao gio hang."
            )

        except ValueError:
            print(
                "Vui long nhap so luong "
                "la mot so nguyen!"
            )

            logging.error(
                "ValueError - Invalid quantity input"
            )

        except ItemNotFoundError:
            print(
                "Ma do uong khong hop le, "
                "vui long kiem tra lai thuc don!"
            )

            logging.warning(
                f"ItemNotFoundError - "
                f"Code: {drink_code}"
            )

        except InvalidQuantityError:
            print(
                "So luong phai lon hon 0!"
            )

            logging.warning(
                f"InvalidQuantityError - "
                f"Quantity: {quantity}"
            )

    elif choice == "3":
        view_order(current_order)

    elif choice == "4":
        checkout(current_order)

    elif choice == "5":

        logging.info(
            "Cashier logged out. "
            "System shutdown."
        )

        print(
            "Da thoat ca lam viec. "
            "Hen gap lai!"
        )

        break

    else:
        print(
            "Lua chon khong hop le!"
        )
