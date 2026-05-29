sum = 0
goal = 0
for inCome in range(1, 8):
    revenue = int(input(f"Nhập doanh thu ngày {inCome}: "))
    sum += revenue
    if revenue >= 500000:
        goal += 1
    
    


print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE---")
print("Doanh thu trung bình mỗi ngày: ", sum / 7, "VNĐ")
print("Số ngày đạt doanh thu mục tiêu: ", goal, "ngày")