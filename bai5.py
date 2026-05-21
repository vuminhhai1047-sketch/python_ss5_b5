

# Input là kiểu dữ liệu đầu vào của chi nhán là int , còn của lớp học cũng int , con học viên cũng int
# output là số học viên của một lớp không thể là số âm
        # Nếu người dùng nhập lựa chọn không nằm trong khoảng từ 1 đến 5, hệ thống không được dừng chương trình và phải nhập lại các lựa chọn khác.
        # Khi kiểm tra lớp có sĩ số thấp, nếu toàn bộ lớp đều có từ 10 học viên trở lên, hệ thống cần thông báo rõ ràng

# Cách giải quyết vòng lặp là 
# trước tiên sử dụng vòng lặp true để tạo menu cho người nhập vô tận nếu sai thì cho nhập tiếp còn nếu đúng ok điều kiện thì break
# Tiếp trong vòng lặp while thì trong case 1 cũng sử dụng while true để nhập chi nhánh để check khoảng tỗng thì cho nhập lại
# Tiếp đến là vòng lặp for thì khi nhập chi nhánh thì vòng lặp for từ 1 đến chi nhánh + 1 khi bạn nhập
# trong vòng lặp chi nhánh thì mình sẽ bắt nó nhập phòng học thì nhập xong từ 1 đến room + 1
# xong vòng lặp room thì bắt nhập số học viên tạo ra biến count = 0
# nếu student < 10 thì count += 1 để đếm nó có hay không 
# mô tả luồng Pseudocode 
# while true 
  # for branch in range(1 , branch_count + 1):
    #room = int(input(f'Nhập số lớp học của chi nhánh {branch}:'))
    # for room in range ( 1 , room + 1 )
        # students = int(input(f'Nhập số học viên))
  # if students < 10:
     #count += 1
#  if count == 0:
#     print('LỖI')





count = 0

while True:
    print('=' * 22 , 'MENU' , '=' * 22)
    print('1.Nhập dữ liệu và xem báo cáo thống kê')
    print('2.Xem hướng dẫn sử dụng')
    print('3.Thoát chương trình')
    choice = int(input('Hãy nhập lựa chọn của bạn:'))

    while True:
        if choice < 0 or choice > 3:
            print('Bạn nhập lựa chọn menu không hợp lệ.Xin vui lòng nhập lại.')
        else:
            break
    match choice:
        case 1:
            while True:
                branch_count = int(input('Nhập số lượng chi nhánh:'))
                if branch_count == '':
                    print('Không thể để giá trị rỗng . Xin vui lòng nhập lại')
                else:
                    for branch in range(1 , branch_count + 1):
                        while True:
                            room = int(input(f'Nhập số lớp học của chi nhánh {branch}:'))
                            if room == '':
                                print('Số phòng học không thể bỏ trống. Xin vui lòng nhập lại')
                            elif room < 0:
                                print('Số phòng học không thể là số âm. Xin vui lòng nhập lại')
                            else:
                                break
                        for room in range( 1 , room + 1 ):
                            while True:
                                students = int(input(f'Nhập số học sinh của lớp {room} - Chi nhánh {branch}:'))
                                if students == '':
                                    print('Số học viên không được để trống.')
                                elif students < 0:
                                    print('Số học viên không được bé hơn 0.')
                                else:
                                    break
                            if students < 10:
                                count += 1
                    if count == 0:
                        print('LỖI - Vì không có lớp nào bé hơn 10 học viên')
        case 2:
            print('=' * 22 ,'CÁCH NHẬP DỮ LIỆU' , '=' * 22)
            print('Bạn nhập dữ liệu chi nhánh là nhập các số thỏa mãn điều kiện bé hơn 0')
            print('khi nhập các chi nhánh thì không nên để trống đoạn mã nhập. Vì lúc đó sẽ báo lỗi')
            print('Tiếp đến là nhập số lớp học thì cũng giống như chi nhánh , không được bỏ trống và < hơn 0 thì báo lỗi không thỏa mãn.')
            print('Tiếp theo là nhập học viên , cũng không được để trống và không được bé hơn không. Nhưng nếu tất cả các lớp mà không có lớp nào bé hơn 10 học viên thì báo lỗi')
        case 3:
            break
        case _:
            print('Bạn không nhập đúng chức năng mà chúng tôi đang có')
