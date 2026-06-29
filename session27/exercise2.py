from abc import ABC, abstractmethod


class BaseProduct(ABC):
    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000

    def __init__(self, product_code, product_name, stock_quantity=0):
        self.product_code = product_code
        self.product_name = product_name
        self.__stock_quantity = stock_quantity

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value.strip().upper()

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    def _set_stock_quantity(self, quantity):
        self.__stock_quantity = quantity

    @abstractmethod
    def import_stock(self, quantity):
        pass

    @abstractmethod
    def export_stock(self, quantity):
        pass

    def __add__(self, other):
        if isinstance(other, BaseProduct):
            return self.stock_quantity + other.stock_quantity
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BaseProduct):
            return self.stock_quantity < other.stock_quantity
        return NotImplemented

    @staticmethod
    def validate_product_code(product_code):
        return (
            len(product_code) == 10
            and product_code[0].isalpha()
            and product_code[1:].isalnum()
        )

    @classmethod
    def update_warehouse_name(cls, new_name):
        cls.warehouse_name = new_name


class ColdStorageProduct(BaseProduct):

    def __init__(
        self,
        product_code,
        product_name,
        required_temperature,
        stock_quantity=0,
    ):
        super().__init__(product_code, product_name, stock_quantity)
        self.required_temperature = required_temperature

    def import_stock(self, quantity):
        if quantity <= 0:
            print("So luong nhap khong hop le!")
            return

        self._set_stock_quantity(
            self.stock_quantity + quantity
        )

        print("Nhap kho thanh cong!")
        print(f"So luong ton kho: {self.stock_quantity}")

    def export_stock(self, quantity):
        if quantity <= 0:
            print("So luong xuat khong hop le!")
            return

        loss = quantity * 0.05
        total = quantity + loss

        if self.stock_quantity >= total:

            self._set_stock_quantity(
                self.stock_quantity - total
            )

            print("Xuat kho thanh cong!")
            print(f"So luong yeu cau: {quantity}")
            print(f"Hao hut bao quan: {loss}")
            print(f"Tong khau tru: {total}")
            print(f"Ton kho con lai: {self.stock_quantity}")

        else:
            print("Khong du hang trong kho!")

    def apply_cooling_cost(self):
        cost = self.stock_quantity * 3000

        print("\n----- PHI BAO QUAN -----")
        print(f"So luong ton kho: {self.stock_quantity}")
        print(f"Nhiet do: {self.required_temperature} do C")
        print(f"Chi phi lam lanh: {cost:,.0f} VND")


class HazardousProduct(BaseProduct):

    def __init__(
        self,
        product_code,
        product_name,
        max_safety_limit,
        stock_quantity=0,
    ):
        super().__init__(product_code, product_name, stock_quantity)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if quantity <= 0:
            print("So luong nhap khong hop le!")
            return

        if self.stock_quantity + quantity > self.max_safety_limit:
            print("Giao dich that bai!")
            print(
                f"Vuot qua han muc an toan ({self.max_safety_limit})"
            )
            return

        self._set_stock_quantity(
            self.stock_quantity + quantity
        )

        print("Nhap kho thanh cong!")
        print(f"Ton kho: {self.stock_quantity}")

    def export_stock(self, quantity):
        if quantity <= 0:
            print("So luong xuat khong hop le!")
            return

        if self.stock_quantity >= quantity:

            self._set_stock_quantity(
                self.stock_quantity - quantity
            )

            print("Xuat kho thanh cong!")
            print(f"Ton kho: {self.stock_quantity}")

        else:
            print("Khong du hang trong kho!")


class HybridPremiumProduct(
    ColdStorageProduct,
    HazardousProduct
):

    def __init__(
        self,
        product_code,
        product_name,
        required_temperature,
        max_safety_limit,
        stock_quantity=0,
    ):
        ColdStorageProduct.__init__(
            self,
            product_code,
            product_name,
            required_temperature,
            stock_quantity,
        )

        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):

        if quantity <= 0:
            print("So luong nhap khong hop le!")
            return

        if self.stock_quantity + quantity > self.max_safety_limit:
            print("Nhap kho that bai!")
            print(
                f"Vuot qua han muc {self.max_safety_limit}"
            )
            return

        self._set_stock_quantity(
            self.stock_quantity + quantity
        )

        print("Nhap kho Hybrid thanh cong!")
        print(f"Ton kho: {self.stock_quantity}")


class FedExCarrier:

    def ship_package(self, product, quantity):
        print(
            f"[FedEx] Dang tiep nhan ma san pham {product.product_code}"
        )
        print(
            f"So luong ban giao: {quantity}"
        )


class DHLCarrier:

    def ship_package(self, product, quantity):
        print(
            f"[DHL] Dang tiep nhan ma san pham {product.product_code}"
        )
        print(
            f"So luong ban giao: {quantity}"
        )


def dispatch_to_carrier(
    carrier_agent,
    product,
    quantity,
):

    try:
        carrier_agent.ship_package(
            product,
            quantity,
        )

        print("Duck Typing thanh cong!")

    except AttributeError:
        print(
            "Don vi van chuyen khong hop le hoac chua ky hop dong!"
        )


products = []

current_product = None


def menu():

    print("\n===== AMAZON INVENTORY SIMULATOR PRO =====")
    print("1. Dang ky ma hang hoa moi")
    print("2. Xem thong tin & MRO")
    print("3. Nhap / Xuat kho")
    print("4. Tinh phi bao quan")
    print("5. Operator Overloading")
    print("6. Dieu pho van chuyen")
    print("7. Thoat")


def register_product():

    print("\n--- CHON LOAI SAN PHAM ---")
    print("1. Cold Storage Product")
    print("2. Hazardous Product")
    print("3. Hybrid Premium Product")

    choice = input("Chon loai san pham (1-3): ")

    product_code = input("Nhap ma san pham: ")

    if not BaseProduct.validate_product_code(product_code):
        print("Ma san pham khong hop le!")
        return None

    product_name = input("Nhap ten san pham: ")

    if choice == "1":

        required_temperature = float(
            input("Nhap nhiet do bao quan: ")
        )

        product = ColdStorageProduct(
            product_code,
            product_name,
            required_temperature,
        )

    elif choice == "2":

        max_safety_limit = int(
            input("Nhap han muc luu tru toi da: ")
        )

        product = HazardousProduct(
            product_code,
            product_name,
            max_safety_limit,
        )

    elif choice == "3":

        required_temperature = float(
            input("Nhap nhiet do bao quan: ")
        )

        max_safety_limit = int(
            input("Nhap han muc luu tru toi da: ")
        )

        product = HybridPremiumProduct(
            product_code,
            product_name,
            required_temperature,
            max_safety_limit,
        )

    else:
        print("Lua chon khong hop le!")
        return None

    print("\nDang ky san pham thanh cong!")
    print("Ten san pham:", product.product_name)

    return product


def show_product(current_product):

    if current_product is None:
        print("Chua co san pham!")
        return

    print("\n------ THONG TIN SAN PHAM ------")
    print("Loai:", type(current_product).__name__)
    print("Kho:", current_product.warehouse_name)
    print("Ma:", current_product.product_code)
    print("Ten:", current_product.product_name)
    print("Ton kho:", current_product.stock_quantity)

    if isinstance(
        current_product,
        (ColdStorageProduct, HybridPremiumProduct),
    ):
        print(
            "Nhiet do:",
            current_product.required_temperature,
        )

    if isinstance(
        current_product,
        (HazardousProduct, HybridPremiumProduct),
    ):
        print(
            "Han muc:",
            current_product.max_safety_limit,
        )

    print("\nMRO")

    for cls in current_product.__class__.mro():
        print(cls.__name__)


def transaction(current_product):

    if current_product is None:
        print("Chua co san pham!")
        return

    print("\n1. Nhap kho")
    print("2. Xuat kho")

    choice = input("Chon giao dich: ")

    quantity = float(
        input("Nhap so luong: ")
    )

    if choice == "1":
        current_product.import_stock(quantity)

    elif choice == "2":
        current_product.export_stock(quantity)

    else:
        print("Lua chon khong hop le!")


def cooling_cost(current_product):

    if current_product is None:
        print("Chua co san pham!")
        return

    if isinstance(
        current_product,
        (ColdStorageProduct, HybridPremiumProduct),
    ):
        current_product.apply_cooling_cost()

    else:
        print("San pham khong ho tro bao quan dong lanh!")


def compare_product(
    products,
    current_product,
):

    if current_product is None:
        print("Chua co san pham!")
        return

    if len(products) < 2:
        print("Can it nhat 2 san pham!")
        return
    print("\n------ DANH SACH SAN PHAM ------")

    for i, product in enumerate(products):
        print(
            f"{i + 1}. {product.product_code} - "
            f"{product.product_name} "
            f"(Ton kho: {product.stock_quantity})"
        )

    choice = int(
        input("Chon san pham de so sanh: ")
    ) - 1

    if choice < 0 or choice >= len(products):
        print("Lua chon khong hop le!")
        return

    other = products[choice]

    if other == current_product:
        print("Khong the chon cung mot san pham!")
        return

    print(
        f"\nTong ton kho: "
        f"{current_product + other}"
    )

    if current_product < other:
        print("Ton kho san pham hien tai it hon.")

    elif other < current_product:
        print("Ton kho san pham hien tai nhieu hon.")

    else:
        print("Hai san pham co cung ton kho.")


def shipping(current_product):

    if current_product is None:
        print("Chua co san pham!")
        return

    print("\n1. FedEx")
    print("2. DHL")

    choice = input("Chon doi tac: ")

    quantity = float(
        input("Nhap so luong ban giao: ")
    )

    if quantity <= 0:
        print("So luong khong hop le!")
        return

    if current_product.stock_quantity < quantity:
        print("Khong du hang trong kho!")
        return

    current_product.export_stock(quantity)

    if choice == "1":
        carrier = FedExCarrier()

    elif choice == "2":
        carrier = DHLCarrier()

    else:
        print("Lua chon khong hop le!")
        return

    dispatch_to_carrier(
        carrier,
        current_product,
        quantity,
    )


while True:

    menu()

    choice = input(
        "Chon chuc nang (1-7): "
    )

    if choice == "1":

        product = register_product()

        if product is not None:
            products.append(product)
            current_product = product

    elif choice == "2":

        show_product(current_product)

    elif choice == "3":

        transaction(current_product)

    elif choice == "4":

        cooling_cost(current_product)

    elif choice == "5":

        compare_product(
            products,
            current_product,
        )

    elif choice == "6":

        shipping(current_product)

    elif choice == "7":

        print(
            "Cam on da su dung Amazon Inventory Simulator Pro!"
        )

        break

    else:

        print("Lua chon khong hop le!")
