transaction = "   nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction = transaction.strip().split("|")
name = transaction[0].strip().title()
code = transaction[1].strip().upper()
amount = int(transaction[2].strip())
status = transaction[3].strip().upper()

print(f"Học viên: {name}")
print(f"Khóa học: {code}")
print(f"Số tiền: {amount:,}")
print(f"Trạng thái: {status}")
