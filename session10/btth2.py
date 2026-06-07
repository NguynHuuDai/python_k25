playlist = []

while True:

    print("\n========== MENU QUẢN LÝ DANH SÁCH PHÁT ==========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
        continue

    choice = int(choice)

    if choice == 1:

        print("\n--- THÊM BÀI HÁT ---")
        print("1. Thêm vào cuối danh sách")
        print("2. Chèn vào vị trí cụ thể")

        sub_choice = input("Nhập lựa chọn: ")

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
            continue

        sub_choice = int(sub_choice)

        song_name = input("Nhập tên bài hát: ")

        if sub_choice == 1:

            playlist.append(song_name)

            print("Thêm bài hát thành công!")
            print("Tổng số bài hát:", len(playlist))

        elif sub_choice == 2:

            position = input("Nhập vị trí muốn chèn: ")

            if not position.isdigit():
                print("Vị trí không hợp lệ.")
                continue

            position = int(position)

            if position < 1 or position > len(playlist) + 1:
                print("Vị trí không hợp lệ.")
            else:
                playlist.insert(position - 1, song_name)

                print("Chèn bài hát thành công!")
                print("Tổng số bài hát:", len(playlist))

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

    elif choice == 2:

        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
        else:

            print("\n--- DANH SÁCH PHÁT ---")

            for i in range(len(playlist)):
                print(f"{i + 1}. {playlist[i]}")

            print("\nTổng số bài hát:", len(playlist))

    elif choice == 3:

        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n--- XÓA BÀI HÁT ---")
        print("1. Xóa theo tên bài hát")
        print("2. Xóa theo số thứ tự")

        sub_choice = input("Nhập lựa chọn: ")

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
            continue

        sub_choice = int(sub_choice)

        if sub_choice == 1:

            song_name = input("Nhập tên bài hát cần xóa: ")

            if song_name in playlist:

                playlist.remove(song_name)

                print(f"Đã xóa bài hát {song_name} khỏi danh sách")

            else:
                print("Không tìm thấy bài hát trong danh sách phát.")

        elif sub_choice == 2:

            position = input("Nhập số thứ tự cần xóa: ")

            if not position.isdigit():
                print("Vị trí không hợp lệ.")
                continue

            position = int(position)

            if position < 1 or position > len(playlist):
                print("Vị trí không hợp lệ.")
            else:

                deleted_song = playlist.pop(position - 1)

                print(f"Đã xóa bài hát {deleted_song} khỏi danh sách")

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

    elif choice == 4:

        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n--- SẮP XẾP VÀ TRÍCH XUẤT ---")
        print("1. Sắp xếp danh sách theo bảng chữ cái A-Z")
        print("2. Hiển thị 3 bài hát đầu tiên")

        sub_choice = input("Nhập lựa chọn: ")

        if not sub_choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
            continue

        sub_choice = int(sub_choice)

        if sub_choice == 1:

            playlist.sort()

            print("Danh sách sau khi sắp xếp A-Z:")

            for song in playlist:
                print(song)


        elif sub_choice == 2:

            print("3 bài hát đầu tiên:")

            for song in playlist[:3]:
                print(song)

        else:
            print("Lựa chọn không hợp lệ")

    elif choice == 5:

        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
