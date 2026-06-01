# in bảng cửu chương từ 2 đến 9
# for i in range(2, 10):
#     print(f"Bảng cửu chương {i}:")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")

# vẽ hình chữ nhật bằng vòng lặp dấu *
# width = int(input("Nhập vào chiều rộng hình chữ nhật: "))
# height = int(input("Nhập vào chiều dài hình chữ nhật: "))

# for i in range(height):
#     for j in range(width):
#         print("*", end=" ")
#     print()

# vẽ hình chữ nhật rỗng bằng vòng lặp dấu *



# doc = int(input("Nhập vào chiều rộng hình chữ nhật: "))
# ngang = int(input("Nhập vào chiều dài hình chữ nhật: "))

# for i in range(ngang):
#     if i == 0 or i == ngang - 1:  # hàng đầu tiên và hàng cuối cùng cột ngang
#         print("* " * doc)
#     else:
#         print("* " + "  " * (doc - 2) + "* ") # bỏ qua hàng giữa in ra dấu * đầu cột dọc và cuối cột dọc, phần giữa in ra dấu cách


# tam giác vuông

height = int(input("Nhập vào chiều cao của tam giác vuông: "))

for i in range(1, height + 1):
    print("* " * i)