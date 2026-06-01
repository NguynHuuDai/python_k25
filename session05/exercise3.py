# input num_rooms: Số lượng phòng(số nguyên).
#       rows, cols: Số hàng và số ghế mỗi hàng
# output sơ đồ bằng ký tự * 

# Giải pháp :
#     Sử dụng vòng lặp for duyệt số lượng phòng
#     Sử dụng các cấu trúc kiểm tra điều kiện (if -elif -else) để chặn các "bẫy" dữ liệu ngay tại thời điểm nhập.

# Sử dụng vòng lặp lồng nhau để vẽ sơ đồ.

# Thiết kế thuật toán
#     Nhập num_rooms. Nếu num_rooms <= 0, thông báo lỗi và kết thúc.

# Vòng lặp room từ 1 đến num_rooms:
#     Nhập rows và cols.
#     Nếu rows > 10 hoặc cols > 10, in thông báo và dừng toàn bộ chương trình.
#     Nếu rows <= 0 hoặc cols <= 0, in thông báo và dùng continue để bỏ qua phòng này.
#     Nếu hợp lệ, thực hiện in hình chữ nhật:
# Vòng lặp i từ 1 đến rows:
#     In ra cols dấu * trên một dòng.

num_rooms = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if num_rooms <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
   
    for i in range(1, num_rooms + 1):
        print(f"\n--- Phòng số {i} ---")
        rows = int(input("Nhập số hàng ghế: "))
        cols = int(input("Nhập số ghế mỗi hàng: "))

        if rows > 10 or cols > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break  

       
        if rows <= 0 or cols <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue  
        # Vẽ sơ đồ
        print(f"Sơ đồ phòng {i}:")
        # Vòng lặp in từng hàng
        for r in range(rows):
            print("*" * cols)
