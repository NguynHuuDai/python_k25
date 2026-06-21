import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sua Da", "price": 35000},
    "F1": {"name": "Freeze Tra Xanh", "price": 55000},
    "T1": {"name": "Tra Sen Vang", "price": 45000}
}


class ItemNotFoundError(Exception):
    """Raised when drink code does not exist."""
    pass


class InvalidQuantityError(Exception):
    """Raised when quantity is less than or equal to 0."""
    pass


def view_menu():
    """Display drink menu."""
    print("\n--- THUC DON HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - {item['name']} - "
            f"{item['price']:,} VND"
        )


def add_to_order(order, drink_code, quantity):
    """
    Add drink to order list.

    Args:
        order (list): Current order.
        drink_code (str): Drink code.
        quantity (int): Quantity.

    Raises:
        ItemNotFoundError
        InvalidQuantityError
    """

    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError

    if quantity <= 0:
        raise InvalidQuantityError

    order.append({
        "code": drink_code,
        "quantity": quantity
    })

    logging.info(
        f"Added {quantity} of {drink_code} to order"
    )

    return DRINK_MENU[drink_code]["name"]


def calculate_total(order):
    """
    Calculate total bill.

    Args:
        order (list)

    Returns:
        int
    """

    total = 0

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        total += (
            DRINK_MENU[code]["price"] * quantity
        )

    return total


def view_order(order):
    """Display order details."""

    if not order:
        print(
            "Gio hang trong, vui long chon mon "
            "(Chuc nang 2)."
        )
        return

    print("\n--- GIO HANG HIEN TAI ---")
    print(
        "Ma SP | Ten do uong        | "
        "Don gia | So luong | Thanh tien"
    )
    print("-" * 65)

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]

        subtotal = price * quantity

        print(
            f"{code:<5} | "
            f"{name:<18} | "
            f"{price:>7,} | "
            f"{quantity:^8} | "
            f"{subtotal:>10,} VND"
        )

    print("-" * 65)

    total = calculate_total(order)

    print(
        f"Tong tien can thanh toan: "
        f"{total:,} VND"
    )


def checkout(order):
    """Process payment."""

    if not order:
        print(
            "Gio hang trong, vui long chon mon "
            "(Chuc nang 2)."
        )
        return

    total = calculate_total(order)

    print("\n--- THANH TOAN ---")
    print(f"Tong tien can thanh toan: {total:,} VND")

    choice = input(
        f"Xac nhan thanh toan "
        f"{total:,} VND? (y/n): "
    ).strip().lower()

    if choice == "y":
        logging.info("Checkout successful")
        order.clear()

        print("Thanh toan thanh cong.")
        print("Gio hang da duoc lam trong.")

    elif choice == "n":
        print(
            "Da huy thao tac thanh toan. "
            "Quay lai menu chinh."
        )

    else:
        print(
            "Lua chon khong hop le. "
            "Thanh toan da bi huy."
        )
