# vấn đề gặp phải là việc sử dụng toán tử không chính xác
# and là để kết hợp hai điều kiện còn or là để xét cho điều kiện nào đúng cũng được
# nên muốn đồng thời kiểm tra ta cần sử dụng and

print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))


if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    print("Reason(s) for rejection:")
    if donor_age < 18:
        print("- Under 18 years old.")
    if donor_weight < 50:
        print("- Weight is under 50 kg.")
