max_price = 0
min_price = 0
quantity = int(input("Nhập số lượng hóa đơn có trong ca :"))
for i in range(quantity):
    price = int(input(f"Nhập giá trị hóa đơn thứ {i + 1}: "))
    if price > max_price:
        max_price = price
    if price < min_price:
        min_price = price

print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print("Giá trị hóa đơn cao nhất: ", max_price, "VNĐ")
print("Giá trị hóa đơn thấp nhất: ", min_price, "VNĐ")
