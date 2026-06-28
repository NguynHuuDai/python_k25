class CoffeeOrder:
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    @property
    def total_amount(self):
        return self.__total_amount

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    def calculate_final_bill(self):
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls.vat_rate = new_rate

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")
order_table1.add_item(50000)
order_table2.add_item(30000)

try:
    order_table1.total_amount = 0
except AttributeError:
    print("Không thể chỉnh sửa trực tiếp tổng tiền hóa đơn!")

CoffeeOrder.update_vat_rate(0.08)

print(f"Tổng tiền Bàn 1 (sau VAT): {order_table1.calculate_final_bill()} VNĐ")
print(f"Tổng tiền Bàn 2 (sau VAT): {order_table2.calculate_final_bill()} VNĐ")
print(f"VAT Bàn 1: {order_table1.vat_rate}")
print(f"VAT Bàn 2: {order_table2.vat_rate}")
