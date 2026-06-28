# 1. Sơ đồ kế thừa

#           Champion(ABC)--------------------Warrior
#                 │----------------------------Mage
#         
# Champion là lớp trừu tượng chứa các thuộc tính chung và các phương thức dùng chung.
# Warrior và Mage kế thừa từ Champion và ghi đè calculate_skill_damage().

# 2. Đa hình (Polymorphism)

# Hai lớp Warrior và Mage đều có phương thức calculate_skill_damage() nhưng cách tính khác nhau.

# Khi gọi:

# champion.calculate_skill_damage()

# Python sẽ tự gọi đúng phương thức của từng đối tượng mà không cần dùng if...else.

# 3. Nạp chồng toán tử

# __add__() giúp cộng chiến lực của 2 tướng hoặc cộng với số để tính tổng đội hình.
# __gt__() giúp so sánh hai tướng bằng toán tử >

from abc import ABC, abstractmethod


class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
]


def find_champion(champion_id):
    for champion in champion_pool:
        if champion.champion_id == champion_id:
            return champion
    return None


def show_pool():
    print("\n--- DANH SÁCH QUÂN CỜ ---")
    print(f"{'Mã':<8}{'Tên':<20}{'Hệ':<10}{'HP':<8}{'ATK':<8}{'Chỉ số riêng':<20}{'Chiến lực'}")

    for champion in champion_pool:
        if isinstance(champion, Warrior):
            role = "Warrior"
            info = f"Armor: {champion.shield_bonus}"
        else:
            role = "Mage"
            info = f"Mana: {champion.ability_power}"

        print(f"{champion.champion_id:<8}"
              f"{champion.name:<20}"
              f"{role:<10}"
              f"{champion.base_hp:<8}"
              f"{champion.base_atk:<8}"
              f"{info:<20}"
              f"{champion.get_combat_power():.0f}")


def add_champion():
    print("\n1. Warrior")
    print("2. Mage")

    choice = input("Chọn hệ: ")

    champion_id = input("Nhập mã: ")

    if find_champion(champion_id):
        print("Mã tướng đã tồn tại!")
        return

    name = input("Nhập tên: ")
    hp = int(input("Nhập HP: "))
    atk = int(input("Nhập ATK: "))

    if choice == "1":
        armor = int(input("Nhập Armor: "))
        champion = Warrior(champion_id, name, hp, atk, armor)

    elif choice == "2":
        ap = float(input("Nhập Ability Power: "))
        champion = Mage(champion_id, name, hp, atk, ap)

    else:
        print("Lựa chọn không hợp lệ!")
        return

    champion_pool.append(champion)

    print("Thêm tướng thành công!")
    print(f"Mã: {champion.champion_id} | Tên: {champion.name} | Chiến lực: {champion.get_combat_power():.0f}")


def compare():
    print("\n--- SO SÁNH ---")

    id1 = input("Nhập mã tướng 1: ")
    id2 = input("Nhập mã tướng 2: ")

    champion1 = find_champion(id1)
    champion2 = find_champion(id2)

    if champion1 is None:
        print(f"Mã tướng {id1} không hợp lệ!")
        return

    if champion2 is None:
        print(f"Mã tướng {id2} không hợp lệ!")
        return

    print(f"{champion1.champion_id} - {champion1.name}: {champion1.get_combat_power():.0f}")
    print(f"{champion2.champion_id} - {champion2.name}: {champion2.get_combat_power():.0f}")

    if champion1 > champion2:
        print(f"{champion1.name} mạnh hơn!")
    else:
        print(f"{champion2.name} mạnh hơn!")


def team_power():
    print("\n--- TÍNH CHIẾN LỰC ĐỘI HÌNH ---")

    ids = input("Nhập các mã (cách nhau bởi dấu phẩy): ").split(",")

    total = 0

    for champion_id in ids:
        champion = find_champion(champion_id.strip())

        if champion is None:
            print(f"Mã tướng {champion_id.strip()} không hợp lệ, bỏ qua!")
            continue

        print(
            f"{champion.champion_id} - {champion.name} : {champion.get_combat_power():.0f}")

        total += champion

    print(f"Tổng chiến lực: {total:.0f}")


# ================== MENU ==================
while True:
    print("""
========== AUTO BATTLER ==========
1. Hiển thị bể tướng
2. Thêm tướng
3. So sánh 2 tướng
4. Tính chiến lực đội hình
5. Thoát
""")

    choice = input("Chọn: ")

    if choice == "1":
        show_pool()

    elif choice == "2":
        add_champion()

    elif choice == "3":
        compare()

    elif choice == "4":
        team_power()

    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
