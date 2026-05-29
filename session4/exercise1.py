old_total = int(input("Số tiền ban đầu của hóa đơn: "))
discount = 0
if old_total < 0:
    print("Số tiền không hợp lệ! Vui lòng nhập một số dương.")
elif old_total > 500000:

    new_total = old_total * 0.9
    discount = old_total - new_total
else:
    new_total = old_total

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print("/nSố tiền được giảm giá: ", discount, "VNĐ")
print("Tổng số tiền khách phải trả: ", new_total, "VNĐ")
    