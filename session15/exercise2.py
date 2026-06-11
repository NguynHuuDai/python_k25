atm_vault_balance = 50000000
ser_account_balance = 10000000


def main():
    print("""
============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================""")
    choice = input("Vui lòng chọn giao dịch (1-4): ").strip()
    return choice


def display_balances():
    global ser_account_balance, atm_vault_balance
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {ser_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money():
    global ser_account_balance, atm_vault_balance
    print("\n--- NẠP TIỀN ---")
    deposit_input = input("Nhập số tiền muốn nạp: ").strip()

    if not deposit_input.isdigit() or int(deposit_input) <= 0:
        print("Số tiền không hợp lệ")
        return

    amount = int(deposit_input)
    ser_account_balance += amount
    atm_vault_balance += amount
    print(
        f"Giao dịch thành công! Số dư tài khoản hiện tại: {ser_account_balance:,} VND.")


def check_withdrawal_rules():
    global atm_vault_balance, ser_account_balance
    print("\n--- RÚT TIỀN ---")
    withdrawing_input = input("Nhập số tiền cần rút: ").strip()

    if not withdrawing_input.isdigit() or int(withdrawing_input) <= 0:
        print("Số tiền không hợp lệ")
        return

    amount = int(withdrawing_input)

    if amount % 50000 != 0:
        print("Số tiền rút phải là bội số của 50,000")
        return

    fee = 1100
    total_deduction = amount + fee

    if amount > atm_vault_balance:
        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
    elif total_deduction > ser_account_balance:
        print("Giao dịch thất bại: Số dư tài khoản không đủ để thực hiện giao dịch (bao gồm phí).")
    else:
        print("Giao dịch đang xử lý...")
        ser_account_balance -= total_deduction
        atm_vault_balance -= amount
        print(f"Phí giao dịch: {fee:,} VND")
        print(f"Bạn đã rút thành công {amount:,} VND.")
        print(f"Số dư tài khoản còn lại: {ser_account_balance:,} VND.")


while True:
    choice = main()

    if choice == "1":
        display_balances()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        check_withdrawal_rules()
    elif choice == "4":
        print("Cảm ơn quý khách đã sử dụng dịch vụ!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
