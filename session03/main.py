count = 0



while (count < 3):
    print("Nhập mật khẩu:")
    password = input()
    if password == "secret":
        print("Đăng nhập thành công!")
        break;
    else:
        print("Sai mật khẩu, thử lại.")
        count += 1



