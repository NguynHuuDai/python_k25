products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def printMenu():
    print("""
=======================================
    QUẢN LÝ CỬA HÀNG - MINI STORE
=======================================
1. Xem danh sách sản phẩm hiện có
2. Thêm mới một sản phẩm
3. Cập nhập giá sản phẩm theo ID
4. Thoát chương trình
=======================================

""")
def printProduct():
    print(f"_____Danh sách sản phẩm_____")
    print(f"ID     |Tến sản phẩm   | Giá bán")
    for product in products:
        print(
            f"{product["id"]}  | {product["name"]}  | {product["price"]}")

def addProduct():
    print(f"--- THÊM SẢN PHẨM MỚI ---")
    id_input = ""
    while id_input == "":
        id_input = input("Nhập mã sản phẩm (ID): ")
        if id_input == "":
            print("ID không được để trống. Vui lòng nhập lại!")
    
    name_input = ""
    while name_input == "":
        name_input = input("Nhập tên sản phẩm: ")
        if name_input == "":
            print("Tên sản phẩm không được để trống. Vui lòng nhập lại!")

    price_input = ""
    while price_input == "" or price_input <= 0:
        price_input = int(input("Nhập giá bán: "))
        if price_input == "":
            print("Giá sản phẩm không được để trống hoặc nhỏ hơn 0. Vui lòng nhập lại!")

    print("Thêm sản phẩm thành công!")
    products.append({
        "id": id_input,
        "name": name_input,
        "price": price_input
    })
    

def updateProductById():
    input_searchId = input("Nhập vào id cần thay đổi giá: ")

    for product in products:
        if input_searchId == product["id"]:
            print(
                f"Tìm thấy sản phẩm: {product['name']} (Giá hiện tại: {product['price']})")

            updatePrice = float(input("Nhập giá mới: "))

            if updatePrice <= 0:
                print("Giá mới không hợp lệ!")
                return

            product["price"] = updatePrice
            print("Cập nhật giá thành công!")
            return

    print(f"Không tìm thấy sản phẩm có mã: {input_searchId}")


while True:
    printMenu()
    choice = input("Nhập vào lựa chọn của bạn(1-4): ")
    if choice == "1":
        if products == "":
            print("Cửa hàng hiện chưa có sản phẩm nào!")
        else:
            printProduct()
    elif choice == "2":
        addProduct()
    elif choice == "3":
        updateProductById()
    elif choice == "4":
        print("Thoát chương trình thành công!")
        break
    else:
        print("Lựa chọn không hợp lệ vui lòng thử lại!")