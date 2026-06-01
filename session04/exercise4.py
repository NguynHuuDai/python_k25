lucky_number = 36

for i in range(1, 6):
    number = int(input(f"Lượt đoán {i + 1} - Nhập số của bạn: "))
    if number == lucky_number:
        print("Chúc mừng! Bạn đã đoán đúng chính xác số may mắn")
        break
    if number < lucky_number:
        print("=> Gợi ý: Số của bạn nhỏ hơn số may mắn")
    else:
        print("=> Gợi ý: Số của bạn lớn hơn số may mắn")

print("--- TRÒ CHƠI KẾT THÚC ---")
