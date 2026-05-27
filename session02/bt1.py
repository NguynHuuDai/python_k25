# vấn đề gặp phải : việc sắp xếp if else không hợp lý
# việc xử lý > 100 trước >120 sẽ khiến cho việc kiểm tra > 120 sẽ không được thực hiện
# cách giải quyết: sắp xếp if else theo thứ tự tăng dần hoặc giảm dần

print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")
