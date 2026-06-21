import logging

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


balance = 0


def print_menu():
    print("""
========== VÍ MOMO GIẢ LẬP ==========
1. Nạp tiền vào ví
2. Chuyển tiền
3. Xem số dư hiện tại
4. Thoát chương trình
====================================
""")


def validate_amount(amount: int):
    if amount <= 0:
        raise InvalidAmountError

    return True


def check_balance(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError

    return True
def deposit_money():
    global balance

    print("\n--- NẠP TIỀN VÀO VÍ ---")

    while True:
        try:
            amount = int(
                input("Nhập số tiền cần nạp: ")
            )

            if amount <= 0:
                raise InvalidAmountError

            balance += amount

            print(
                f"\nNạp tiền thành công: +{amount:,} VND"
            )
            print(
                f"Số dư hiện tại: {balance:,} VND"
            )

            logging.info(
                f"Deposit successful: +{amount} VND. "
                f"Current Balance: {balance}"
            )

            break

        except ValueError:
            print(
                "Lỗi: Vui lòng nhập số tiền hợp lệ."
            )

            logging.error(
                "ValueError: Invalid numeric input for deposit."
            )

        except InvalidAmountError:
            print(
                "Lỗi: Số tiền giao dịch phải lớn hơn 0."
            )

            logging.error(
                f"InvalidAmountError: Attempted to process "
                f"{amount} VND."
            )


def transfer_money():
    global balance

    print("\n--- CHUYỂN TIỀN ---")

    phone = input(
        "Nhập số điện thoại người nhận: "
    ).strip()

    if not (phone.isdigit() and len(phone) == 10):
        print("Số điện thoại không hợp lệ.")
        return

    while True:
        try:
            amount = int(
                input("Nhập số tiền cần chuyển: ")
            )

            if amount <= 0:
                raise InvalidAmountError

            if amount > balance:
                raise InsufficientBalanceError

            if amount >= 10000000:
                logging.warning(
                    f"High value transaction detected: "
                    f"{amount} VND to {phone}"
                )

            balance -= amount

            print(
                f"\nChuyển tiền thành công tới số điện thoại {phone}."
            )
            print(
                f"Số tiền đã chuyển: {amount:,} VND"
            )
            print(
                f"Số dư còn lại: {balance:,} VND"
            )

            logging.info(
                f"Transfer successful: -{amount} VND "
                f"to {phone}. Current Balance: {balance}"
            )

            break

        except ValueError:
            print(
                "Lỗi: Vui lòng nhập số tiền hợp lệ."
            )

            logging.error(
                "ValueError: Invalid numeric input for transfer."
            )

        except InvalidAmountError:
            print(
                "Lỗi: Số tiền giao dịch phải lớn hơn 0."
            )

            logging.error(
                f"InvalidAmountError: Attempted to process "
                f"{amount} VND."
            )

        except InsufficientBalanceError:
            print(
                "\nGiao dịch thất bại: "
                "Số dư của bạn không đủ."
            )
            print(
                f"Số dư hiện tại: {balance:,} VND"
            )

            logging.error(
                f"InsufficientBalanceError: Attempted to transfer "
                f"{amount} VND with balance {balance} VND."
            )

            break


def show_balance():
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance:,} VND")

    logging.info(
        f"Balance checked. Current Balance: {balance}"
    )


while True:
    print_menu()

    choice = input(
        "Chọn chức năng (1-4): "
    )

    if choice == "1":
        deposit_money()

    elif choice == "2":
        transfer_money()

    elif choice == "3":
        show_balance()

    elif choice == "4":
        print("Thoát chương trình.")

        logging.info("System shutdown")

        break

    else:
        print("Lựa chọn không hợp lệ.")
