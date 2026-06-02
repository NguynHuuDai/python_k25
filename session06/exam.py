#Bài tập 1

price = float(input("Nhập đơn giá: "))
quantity = int(input("Nhập số lượng "))

total_price = price * quantity

if total_price > 1000000:
    total_price = total_price * 0.9

print(f"Tổng tiền: {total_price}")    


#Bài tập 2
pass_word = ("123456")

key = 0
while key < 3:
    password_input = input("Nhập mật khẩu: ")
    if password_input == pass_word:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        key += 1
        if key == 3:
            print("Tài khoản bị khóa")


#Bài tập 3

total_quantity = 0
valid_goods = 0
quantity = int(input("Nhập số lượng hàng hóa: "))

while quantity != 0:
    if quantity < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
    elif quantity > 0:
        total_quantity += quantity
        valid_goods += 1
        print("Thùng hàng hợp lệ, đã thêm vào tổng số lượng!")
    quantity = int(input("Nhập số lượng hàng hóa: "))


print(f"Tổng số lượng hàng hóa: {total_quantity}")
print(f"Số lượng hàng hóa thu được: {valid_goods}")
