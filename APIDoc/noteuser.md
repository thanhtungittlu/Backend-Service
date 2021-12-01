## Các API cần làm cho service quản lý user
- Login (chỉ cho phép user có role là admin hoặc superadmin được đăng nhập, hs256)
- List danh sách user có trong hệ thống, chỉ hiển thị user có role là boss hoặc manage (cần có các trường như email, status, boxNumber, role, chỉ user có role là admin hoặc superadmin được thực hiện api này)

- Thêm user với các trường cần thiết (chỉ user có role là admin hoặc superadmin được thực hiện api này)

    + `id`: auto gen uuid (search google gen uuid with python),
    + `name`: Tên người dùng, có thể để trống
    + `email`: phải validiate xem có đúng là mail của nó hay không và không được trùng với người đã tồn tại trong DB trước
    + `passsword`: mã hóa bằng bcrypt(phải tìm được cách mã hóa và giải mã `https://zetcode.com/python/bcrypt/`)
    + `verify`: luôn bằng true (kiểu giá trị boolean)
    + `product`: luôn bằng đoạn mã này `fr,pc,hm,at,fd,lp` 
    + `phoneNumber`: là số, có thể để trống
    + `boxNumber`: luôn bằng giá trị 100
    + `mobileToken`: để rỗng,
    + `apiURL`: có thể rỗng,
    + `role`: có 2 giá trị có thể điền `boss` và `manager`
    + `status`: luôn bằng true (kiểu giá trị boolean)

- Sửa các thông tin của user có role là boss và manager (chỉ user có role là admin hoặc superadmin được thực hiện api này)

- Show thông tin chi tiết của các user (chỉ user có role là admin hoặc superadmin được thực hiện api này)








