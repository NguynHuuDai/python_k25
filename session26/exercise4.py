# 1. Abstract Base Class
# Equipment là lớp trừu tượng.
# Không cho phép tạo trực tiếp Equipment().
# Mọi loại vũ khí đều phải cài đặt calculate_total_damage().
# 2. Multiple Inheritance & MRO

# MagicSword kế thừa:

# Equipment
#      ↑
#   Weapon      MagicMixin
#       \       /
#       MagicSword

# Thứ tự khởi tạo:

# Weapon.__init__()
# MagicMixin.__init__()

# để đảm bảo có đầy đủ:

# name
# base_damage
# upgrade_level
# magic_power
# 3. Polymorphism

# Trong chức năng xem kho:

# for item in inventory:
#     item.calculate_total_damage()

# Python sẽ tự gọi đúng hàm của Weapon hoặc MagicSword.

# Không cần dùng if...else.

# 4. Operator Overloading
# __gt__() dùng toán tử >
# __add__() dùng toán tử +

# Khi cộng:

# weapon1 + weapon2

# trả về Weapon mới có:

# base_damage = tổng base_damage
# upgrade_level = tổng upgrade_level


from abc import ABC, abstractmethod

class Equipment(ABC):
    @abstractmethod
    def calculate_total_damage(self):
        pass

class Weapon(Equipment):
    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể so sánh giữa các trang bị!")
            return False
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp giữa các trang bị!")
            return None
        new_name = f"Fusion({self.name} + {other.name})"
        new_damage = self.base_damage + other.base_damage
        new_upgrade = self.upgrade_level + other.upgrade_level
        return Weapon(
            new_name,
            new_damage,
            new_upgrade
        )

class MagicMixin:

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} phát sáng bởi ma thuật!")

class MagicSword(Weapon, MagicMixin):
    def __init__(self,
                 name,
                 base_damage,
                 upgrade_level,
                 magic_power):

        Weapon.__init__(
            self,
            name,
            base_damage,
            upgrade_level
        )

        MagicMixin.__init__(
            self,
            magic_power
        )

    def calculate_total_damage(self):

        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )

inventory = []
