# Vòng lặp ngoài: for month in range(...) : Đang yêu cầu hệ thống đi qua từng tháng trước

# Vòng lặp trong: for branch in range(...) : Đang yêu cầu hệ thống đi qua từng chi nhánh trong mỗi tháng đó

# Lỗi hiển thị sẽ bị trộn lẫn, không gom nhóm được doanh thu theo từng chi nhánh như yêu cầu báo cáo

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3
result = ""
    
for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        result = result + \
            f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n"

print("\n-------------- Kết quả --------------")
print(result)
