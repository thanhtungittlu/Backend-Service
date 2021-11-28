## Validate cho BoxAi

- Thêm BoxAI với các trường cần thiết 
    + `id`: auto gen uuid 
    + `name`: Tên Box, có thể để trống
    + `group`: Trùng với 1 idGroup trong db group
    + `module`: Là 1 Array con trong ["hm","rm","pc","fr","att"]
    + `userid`: Trùng với 1 idUser trong db user
    + `registedDate`: Auto gen datenow
    + `status`: 2 lựa chọn: - Module installed
                            - Module is not installed
    + `ip`: Có thể để trống.
    + `ipVPN`: Có thể để trống.

## Validate cho chuỗi Camera, 1 Box có thể có nhiều camera
- Thêm chuỗi camera với các trường cần thiết 
    + `id`: auto gen uuid 
    + `name`: Tên camera, không thể để trống
    + `boxID`: Là id của BoxAI
    + `userID`: Là userid của BoxAi
    + `link_stream`: link stream của camera
    + `module`: Là 1 Array con module của BoxAI
    + `status`: 2 lựa chọn: - true
                            - false
    
## Validate cho chuỗi zone của camera, 1 camera có thể có nhiều zone
- Nếu module của camera mà có ["pc"] thì thêm zone các trường cần thiết 
    + `id`: auto gen uuid 
    + `name`: Tên zone, không thể để trống
    + `boxID`: Là id của BoxAI
    + `camID`: Là id của Camera
    + `location`: Có 3 lựa chọn: ` "gate", "shop", "way" `
    + `groupID`: Là group của BoxAI
    + `offset`: Là 1 Array có thể có nhiều phần tử `x` ,    0 < `x` là float < 1
    
## Validate cho chuỗi route của camera, 1 camera có thể có nhiều route
- Nếu module của camera mà có ["rm"] thì thêm route các trường cần thiết 
    + `id`: auto gen uuid 
    + `boxID`: Là id của BoxAI
    + `camID`: Là id của Camera
    + `start`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1
    + `end`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1
    + `mid`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1, có thể có mid hoặc không có
    + `cluster`: Không để trống
    
    





