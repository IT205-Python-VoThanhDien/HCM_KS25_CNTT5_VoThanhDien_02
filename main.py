product_list = [
    {
        'id': 'SP001', 
        'name': 'Chuot khong day Logitech',
        'price': 250000,
        'stock': 15,
        'safety_stock': 20,
        'total_stock': 3750000,
        'status': 'Cảnh báo'
     }
    ]

def show_list(list):
    print("                                                                  ---- DANH SÁCH HÀNG HÓA -----")
    print()
    header = f"{'Mã sản phẩm':<20} | {'Tên sản phẩm':<40} | {'Đơn giá vốn':<20} | {'Số lượng tồn':<20} | {'Định mức tối thiểu':<20} | {'Tổng giá trị tồn kho':<20} | {'Trạng thái tồn kho':<20}"
    print(header)
    print("-"*len(header))
    for item in list:
        print(f"{item['id']:<20} | {item['name']:<40} | {item['price']:<20} | {item['stock']:<20} | {item['safety_stock']:<20} | {item['total_stock']:<20} | {item['status']:<20}")


def add_product(list):
    while True:
        new_id = input("Nhập mã sản phẩm: ")
        if not new_id:
            print("Mã sản phẩm không được để trống")
            continue
        for item in list:
            if new_id == item['id']:
                print("Mã sản phẩm đã tồn tại")
                continue

        new_name = input("Nhập tến sản phẩm: ")
        if not new_name:
            print("Tên sản phẩm không để trống")
            continue

        new_price = input("Nhập đơn giá: ")
        new_price = int(new_price)
        if new_price < 0:
            print("Phải lớn hơn 0")
            continue

        new_stock = input("Số lượng tồn đầu kỳ: ")
        new_stock = int(new_stock)
        if new_stock < 0:
            print("Phải lớn hơn 0")
            continue

        new_safety_stock = input("Nhập định mức tối thiểu: ")
        new_safety_stock = int(new_safety_stock)
        if new_safety_stock < 0:
            print("phải lớn hơn 0")
            continue
        break

    new_total_stock = new_price *  new_stock

    if new_stock >  new_safety_stock * 3:
        new_status = 'Quá tải'
    elif new_stock > new_safety_stock:
        new_status = 'An toàn'
    elif new_stock > 0:
        new_status = 'Cảnh báo'
    else:
        new_status = 'Hết hàng'

    new_product = {'id': new_id, 'name': new_name, 'price': new_price, 'stock': new_stock, 'safety_stock': new_safety_stock, 'total_stock': new_total_stock, 'status': new_status}
    list.append(new_product)
    print("Đã thêm sản phẩm thành công")

def update_product(list):
    update_id = input("Nhập mã sản phẩm cần cập nhật: ")

    for item in list:
        if update_id == item['id']:
            update_price = input("Nhập giá vốn mới: ")
            update_price = int(update_price)
            
            update_stock = input("Nhập số lượng tồn kho mới: ")
            update_stock = int(update_stock)

            update_safety_stock = input("Nhập định mức tối thiểu mới: ")
            update_safety_stock = int(update_safety_stock)

            item['price'] = update_price
            item['stock'] = update_stock
            item['safety_stock'] = update_safety_stock
            print("Đã cập nhật thành công")
        break
    else:
        print("Không tìm thấy mã sản phẩm")

def delete_product(list):
    delete_id = input("Nhập mã sản phẩm cần xóa: ")
    for item in list:
        if delete_id == item['id']:
            list.remove(item)
            print("Đã xóa sản phẩm thành công")

def search_product(list):
    search_id = input("Nhập mã sản phẩm cần tìm: ")
    for item in list:
        if search_id == item['id']:
            show_list(list)

while True:
    print("---- MENU QUẢN LÝ KHO HÀNG ----")
    print("="*40)
    print("1. Hiển thị danh sách kho hàng")
    print("2. Khai báo sản phẩm mới")
    print("3. Cập nhật số lượng và giá vốn")
    print("4. Xóa sản phẩm khỏi danh mục")
    print("5. Tìm kiếm sản phẩm")
    print("6. Thống kê trạng thái kho hàng")
    print("7. Phân loại trạng thái tự động")
    print("8. Thoát chương trình")
    print("="*40)
    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case '1':
            show_list(product_list)
        case '2':
            add_product(product_list)
        case '3':
            update_product(product_list)
        case '4':
            delete_product(product_list)
        case '5':
            search_product(product_list)
        case '8':
            print("Cảm ơn bạn đã sử dụng chương trình")
            break
        case _:
            break
            


