
customer = 0
choice = "c"
larger = 0
sum = 0

while choice == "c":

    match choice:

        case "k":
            break
        case "c":
            customer += 1
            price = int(input(f"Khách hàng {customer}: "))

            # Cộng dồn doanh thu
            sum += price
            choice = input(
                "Nhập 'c' để tiếp tục hoặc 'k' để kết thúc: ").lower()

            if price >= 1000000:
                larger += 1



print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
print("Tổng số hóa đơn đã xử lý: ", customer, " hóa đơn")
print("Tổng doanh thu ngày hôm nay: ", sum, "VNĐ")
print("Số hóa đơn lớn (>= 1000000 VND))", larger, " hóa đơn")
print("Tỉ lệ hóa đơn lớn đạt: ", larger/customer *
      100 if customer > 0 else 0, "% trên tổng số đơn hàng")
