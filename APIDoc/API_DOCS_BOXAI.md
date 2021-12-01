# Trước khi sử dụng API thì Login để lấy token. 
Dùng phương thức POST http://192.168.100.168:5000/login
``` json 
{
    "email" : "thanh191997@gmail.com",
    "password" : "meditech1234"
}
```

# List BOXAI

### GET BOXAI : Show infomation Box AI bao gồm cả Camera, zone, route
**URL** : `http://192.168.100.168:5000/boxs`

**Method** : `GET`

**Headers**: `Authorization`

**Key**: `Authorization`

**Value** : `TOKEN REQUIRED`

**Data constraints**

**Data example**

## Success Response

**Code** : `Status 200 OK`

## Erorr response : 
**Lỗi khi truyền sai token, hoặc thiếu token**
``` json
{
    "code": 401,
    "message": "Unauthorized"
}
```

# Details BOXAI

### GET BOXAI : Show infomation Box AI bao gồm cả Camera, zone, route
**URL** : `http://192.168.100.168:5000/`

**ENDPOINT** : ` box?id=77767772-7559-477f-b95f-cab2101b5d50 `

**Method** : `GET`

**Headers**: `Authorization`

**Key**: `Authorization`

**Value** : `TOKEN REQUIRED`

**Data constraints**

**Data example**

## Success Response

**Code** : `Status 200 OK`

**Content example**

``` json
{
    "id": "77767772-7559-477f-b95f-cab2101b5d50",
    "name": "co-op mart2",
    "group": "433fed09-0290-455d-9a2b-18e2e44b36h3",
    "boxToken": "1235",
    "module": [
        "hm",
        "pc"
    ],
    "userID": "3",
    "registedDate": "03-05-2021",
    "status": "module installed",
    "ip": "",
    "ipVPN": "",
    "cameras": [
        {
            "id": "c059dd7e-29b7-4378-ae7c-ee941886a0c3",
            "status": true,
            "link_stream": "rtsp://guest:hd19012019@14.241.236.171:2552/Streaming/channels/101",
            "boxID": "77767772-7559-477f-b95f-cab2101b5d50",
            "userID": "3",
            "module": [
                "pc",
                ""
            ],
            "name": "HL Vera_Papka",
            "zones": [
                {
                    "id": "2",
                    "name": "Shop VERA",
                    "offset": [
                        0.2800000011920929,
                        0.5699999928474426,
                        0.5199999809265137,
                        0.23999999463558197
                    ],
                    "location": "gate"
                },
                {
                    "id": "03f18ebb-6881-4a75-9d54-dd5adf10b630",
                    "name": "",
                    "offset": [
                        0.800000011920929,
                        0.8999999761581421,
                        0.6000000238418579,
                        0.699999988079071
                    ],
                    "location": ""
                }
            ],
            "routes": [
                {
                    "id": "4447a821-81c0-4ca4-9eea-c97ecc67ed0c",
                    "start": [
                        0.3,
                        0.23
                    ],
                    "end": [
                        0.98,
                        0.65
                    ],
                    "mid": [],
                    "cluster": "5"
                },
                {
                    "id": "881a027a-0c2c-4f0b-a89c-fcd542e91688",
                    "start": [
                        0.5,
                        0.67
                    ],
                    "end": [
                        0.8,
                        0.9
                    ],
                    "mid": [],
                    "cluster": "6"
                },
                {
                    "id": "3030d72b-a931-4174-a790-d0e4c517a083",
                    "start": [
                        0.5,
                        0.67
                    ],
                    "end": [
                        0.8,
                        0.9
                    ],
                    "mid": [],
                    "cluster": "6"
                },
                {
                    "id": "b282605e-ea5a-484a-982a-a56c8f7bbf46",
                    "start": [
                        0.5,
                        0.67
                    ],
                    "end": [
                        0.8,
                        0.9
                    ],
                    "mid": [],
                    "cluster": "6"
                },
                {
                    "id": "93d18832-aad2-476a-a920-4735c88327dd",
                    "start": [
                        0.3,
                        0.2
                    ],
                    "end": [
                        0.1,
                        0.15
                    ],
                    "mid": [],
                    "cluster": "5"
                }
            ]
        },
        {
            "id": "31157d7b-bc3c-4455-b6ec-9fcefbdb3e41",
            "status": true,
            "link_stream": "rtsp://guest:hd19012019@14.241.236.171:2551/Streaming/channels/101",
            "boxID": "77767772-7559-477f-b95f-cab2101b5d50",
            "userID": "3",
            "module": [
                "pc",
                "hm"
            ],
            "name": "Sảnh Aldo",
            "zones": [
                {
                    "id": "4feb2ad5-4fed-46bf-acc0-1a07ceee27a9",
                    "name": "ADIDAS",
                    "offset": [
                        0.23000000417232513,
                        0.20000000298023224,
                        0.6899999976158142,
                        0.07000000029802322
                    ],
                    "location": "gate"
                },
                {
                    "id": "d4a386d2-381a-44ae-8547-423e570a34ce",
                    "name": "",
                    "offset": [
                        0.10000000149011612,
                        0.20000000298023224,
                        0.30000001192092896,
                        0.4000000059604645
                    ],
                    "location": "shop"
                },
                {
                    "id": "5dbad714-c185-4308-8d0d-0776779b527e",
                    "name": "",
                    "offset": [
                        0.20000000298023224,
                        0.30000001192092896,
                        0.30000001192092896,
                        0.4000000059604645
                    ],
                    "location": "gate"
                }
            ],
            "routes": [
                {
                    "id": "b6f3a763-2d8e-4345-a91a-a103e35087b9",
                    "start": [
                        0.441,
                        0.713
                    ],
                    "end": [
                        0.557,
                        0.381
                    ],
                    "mid": [],
                    "cluster": "18"
                },
                {
                    "id": "b60cd57f-b536-4d62-8671-659d50e3b185",
                    "start": [
                        0.36,
                        0.285
                    ],
                    "end": [
                        0.572,
                        0.243
                    ],
                    "mid": [],
                    "cluster": "19"
                },
                {
                    "id": "65a1eeb8-990e-485e-807f-a65aa7933491",
                    "start": [
                        0.362,
                        0.303
                    ],
                    "end": [
                        0.32,
                        0.658
                    ],
                    "mid": [],
                    "cluster": "20"
                },
                {
                    "id": "b8eb58fa-58a6-4cb6-98c5-0baede25c90",
                    "start": [
                        0.615,
                        0.21
                    ],
                    "end": [
                        0.387,
                        0.242
                    ],
                    "mid": [],
                    "cluster": "21"
                }
            ]
        },
        {
            "id": "09ccb670-7a5b-454c-98e7-87558fe8e577",
            "status": true,
            "link_stream": "rtsp://guest:hd19012019@14.241.236.171:2553/Streaming/channels/101",
            "boxID": "77767772-7559-477f-b95f-cab2101b5d50",
            "userID": "3",
            "module": [
                "pc",
                "hm"
            ],
            "name": "Sảnh XTRA T3",
            "zones": [
                {
                    "id": "3",
                    "name": "GH mỹ phẩm",
                    "offset": [
                        0.24,
                        0.21,
                        0.13,
                        0.21
                    ],
                    "location": "gate"
                }
            ],
            "routes": []
        }
    ]
}
```

## Erorr response : 
**Lỗi khi truyền sai token, hoặc thiếu token**
``` json
{
    "code": 401,
    "message": "Unauthorized"
}
```
**Lỗi khi truyền sai id**
``` json
{
    "code": 400,
    "message": "Bad Request, Box not found."
}
```



### POST BOXAI : Đăng ký một Box mới.
**URL** : `http://192.168.100.168:5000/`

**ENDPOINT** : `box`

**Method** : `POST`

**Headers**: `Authorization`

**Key**: `Authorization` , `Content-Type`

**Value** : `TOKEN REQUIRED` , `application/json`

**Data constraints**

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

- Thêm chuỗi camera với các trường cần thiết 
    + `id`: auto gen uuid 
    + `name`: Tên camera, không thể để trống
    + `boxID`: Là id của BoxAI
    + `userID`: Là userid của BoxAi
    + `link_stream`: link stream của camera
    + `module`: Là 1 Array con module của BoxAI
    + `status`: 2 lựa chọn: - true
                            - false

- Nếu module của camera mà có ["pc"] thì thêm zone các trường cần thiết 
    + `id`: auto gen uuid 
    + `name`: Tên zone, không thể để trống
    + `boxID`: Là id của BoxAI
    + `camID`: Là id của Camera
    + `location`: Có 3 lựa chọn: ` "gate", "shop", "way" `
    + `groupID`: Là group của BoxAI
    + `offset`: Là 1 Array có thể có nhiều phần tử `x` ,    0 < `x` là float < 1
    

- Nếu module của camera mà có ["rm"] thì thêm route các trường cần thiết 
    + `id`: auto gen uuid 
    + `boxID`: Là id của BoxAI
    + `camID`: Là id của Camera
    + `start`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1
    + `end`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1
    + `mid`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1, có thể có mid hoặc không có
    + `cluster`: Không để trống
    
**Data example**
```json
{
    "boxai": {
        "name": "TestBoxx",
        "group": "124",
        "module": [
            "rm","att","pc"
        ],
        "userID": "2",
        "status": "Module is not installed",
        "ip": "",
        "ipVPN": ""
    },
    "cameras": [
        {
            "status": true,
            "link_stream": "http://...",
            "module": [
                "rm","pc"
            ],
            "name": "Camara1",
            "zones": [
                { 
                    "name": "Adidas",
                    "offset": [0.1,0.2,0.3,0.4],
                    "location": "gate"
                },
                {
                    "name": "Adidas",
                    "offset": [0.1,0.2,0.3,0.4],
                    "location": "gate"
                }
            ],
            "routes": [
                {
                    "start": [0.1,0.2],
                    "end": [0.1,0.2],
                    "mid": [0.1,0.2],
                    "cluster": "13"
                },                
                {
                    "start": [0.1,0.2],
                    "end": [0.1,0.2],
                    "mid": [0.1,0.2],
                    "cluster": "14"
                }
            ]
        },
        {
            "status": true,
            "link_stream": "http://...",
            "module": [
                "rm"
            ],
            "name": "Camara2",
            "routes": [
                {
                    "start": [0.1,0.2],
                    "end": [0.1,0.1111112],
                    "mid": [],
                    "cluster": "26"
                },
                {
                    "start": [0.1,0.2],
                    "end": [0.1,0.1111112],
                    "mid": [],
                    "cluster": "27"
                },
            ]
        }
    ]
}
```



## Success Response

**Code** : `Status 200 OK`

**Content example**
```json
{
    "code": 200,
    "message": "Operation success"
}
```

## Erorr response : 
**Lỗi khi truyền sai token, hoặc thiếu token**
``` json
{
    "code": 401,
    "message": "Unauthorized"
}
```
**Lỗi khi truyền thiếu boxai hoặc cameras**

``` json
{
    "code": 400,
    "message": "Bad request, filed empty."
}
```
**Lỗi khi điền rỗng các trường name,cluster,link_stream...**
```json
{
    "code": 400,
    "message": "Bad Request, ..... empty"
}
```

**Lỗi khi điền group(user) không có sẵn trong db Group**
```json
{
    "code": 400,
    "message": "Bad Request, Group(User) not exist"
}
```
**Lỗi khi điền sai module BoxAi**
```json
{
    "code": 400,
    "message": "Bad Request, Module not satisfied."
}
```

**Lỗi khi điền sai Status của Box**
```json
{
    "code": 400,
    "message": "Bad Request, Status: Module installed or Module is not installed"
}
```

**Lỗi khi không insert Box  do hệ thống**
```json
{
    "code": 500,
    "message":  "Error!!! Insert Box failed."
}
```

**Lỗi khi điền sai module của camera không thuộc module của BoxAi**
```json
{
    "code": 400,
    "message": "Bad Request, Module camera (name: {}) is must belong to Module Box"
}
```

**Lỗi khi điền module của camera**
```json
{
    "code": 400,
    "message": "Bad Request, Status is boolean"
}
```

**Lỗi khi không insert Camera do hệ thống**
```json
{
    "code": 500,
    "message":  "Error!!! Insert camera failed."
}
```

**Lỗi khi điền location của Zone**
```json
{
    "code": 400,
    "message": "Bad Request, Location: gate or shop or way"
}
```

**Lỗi khi điền offet của Zone**
```json
{
    "code": 400,
    "message": "Bad Request, offset is array from 0 to 1, Error: {}"
}
```

**Lỗi khi không insert Zone do hệ thống**
```json
{
    "code": 500,
    "message":  "Error!!! Insert Zone failed."
}
```


**Lỗi khi nhập sai start,end,mid**
```json
{
    "code": 400,
    "message":  "Bad Request, Start(End,Mid) length is 2,  Error: {}"
}

{
    "code": 400,
    "message": "Bad Request, Start(End,Mid) is array from 0 to 1, 
    Error: "
}
```




### PUT BOXAI : Chỉnh sửa một Box hiện có, có thể chỉnh sửa, hoặc xóa camera, zone, route.
**URL** : `http://192.168.100.168:5000/`

**ENDPOINT** : `box?id=04b5abab-cef4-41db-abf6-7b857d188ec4`

**Method** : `PUT`

**Headers**: `Authorization`

**Key**: `Authorization` , `Content-Type`

**Value** : `TOKEN REQUIRED` , `application/json`

**Data constraints**

- Chỉnh BoxAI với các trường cần thiết  
    + `name`: Tên Box, có thể để trống
    + `group`: Trùng với 1 idGroup trong db group
    + `module`: Là 1 Array con trong ["hm","rm","pc","fr","att"]
    + `userid`: Trùng với 1 idUser trong db user
    + `registedDate`: Auto gen datenow
    + `status`: 2 lựa chọn: - Module installed
                            - Module is not installed
    + `ip`: Có thể để trống.
    + `ipVPN`: Có thể để trống.

- Chỉnh hoặc xóa chuỗi camera với các trường cần thiết 
    + `id`: Truyền id của camera cần chỉnh sửa, nếu truyền vào rỗng thì thêm mới camera
    + `remove`: Truyền vào giá trị boolean, nếu là true thì xóa camera 
    + `name`: Tên camera, không thể để trống
    + `link_stream`: link stream của camera
    + `module`: Là 1 Array con module của BoxAI
    + `status`: 2 lựa chọn: - true
                            - false

- Nếu module của camera mà có ["pc"] thì thêm zone các trường cần thiết 
    + `id`: Truyền id của Zone cần chỉnh sửa, nếu truyền vào rỗng thì thêm mới Zone
    + `remove`: Truyền vào giá trị boolean, nếu là true thì xóa Zone
    + `name`: Tên zone, không thể để trống
    + `location`: Có 3 lựa chọn: ` "gate", "shop", "way" `
    + `offset`: Là 1 Array có thể có nhiều phần tử `x` ,    0 < `x` là float < 1
    

- Nếu module của camera mà có ["rm"] thì thêm route các trường cần thiết 
    + `id`: Truyền id của Route cần chỉnh sửa, nếu truyền vào rỗng thì thêm mới Route
    + `remove`: Truyền vào giá trị boolean, nếu là true thì xóa Route
    + `start`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1
    + `end`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1
    + `mid`: Là 1 Array 2 phần tử   0 < [x,y] là float < 1, có thể có mid hoặc không có
    + `cluster`: Không để trống
    

**Data example**

```json
{
    "boxai": {
        "name": "TextN1",
        "group": "124",
        "module": [
            "rm","att","pc"
        ],
        "userID": "2",
        "status": "Module is not installed",
        "ip": "",
        "ipVPN": ""
    },
    "cameras": [
        {
            "id":"bbccbf45-8742-4e14-9f9a-92c0b2bbc223",
            "remove": false,
            "status": true,
            "link_stream": "http://camera1new...",
            "module": [
                "rm","pc"
            ],
            "name": "Camara1",
            "zones": [
                { 
                    "remove": true,
                    "id":"df75a9b3-cd53-48a9-b293-ccb3294b39e0",
                    "name": "Adidas1",
                    "offset": [0.1,0.2,0.3,0.4],
                    "location": "gate"
                },
                {
                    "remove": false,
                    "id":"5a13c7aa-c88e-46af-9374-4781878259a7",
                    "name": "Adidas2",
                    "offset": [0.1,0.2,0.3,0.4],
                    "location": "shop"
                },
                {
                    "id":"",
                    "remove": false,
                    "name": "AdidasZone3",
                    "offset": [0.1,0.2,0.3,0.4],
                    "location": "way"
                }
            ],
            "routes": [
                {
                    "remove": true,
                    "id":"56e83ab6-1a5d-4eff-b7ec-903d71f91aa8",
                    "start": [0.1,0.2],
                    "end": [0.1,0.2],
                    "mid": [0.1,0.2],
                    "cluster": "50"
                },                
                {
                    "remove": false,
                    "id": "15373937-9213-424b-87f1-1412cc8a6fab",
                    "start": [0.1,0.2],
                    "end": [0.1,0.2],
                    "mid": [0.1,0.2],
                    "cluster": "7"
                }
            ]
        },
        {
            "id":"56217478-46ec-4f4d-a05a-e6e7723b2207",
            "remove": true,
            "status": true,
            "link_stream": "http://camera2new...",
            "module": [
                "rm"
            ],
            "name": "Camara2",
            "routes": [
                {
                    "id": "88616646-e5d3-4d06-a638-fbbe563f4779",
                    "start": [0.1,0.2],
                    "end": [0.1,0.1111112],
                    "mid": [],
                    "cluster": "6"
                }
            ]
        },
        {
            "id": "",
            "remove": false,
            "status": true,
            "link_stream": "http://camera3....",
            "module": [
                "rm","pc"
            ],
            "name": "Camara3Dele",
            "zones": [
                {
                    "id":"",
                    "remove": false,
                    "name": "Nike",
                    "offset": [0.1,0.2,0.3],
                    "location": "gate"
                }
            ],
            "routes": [
                {
                    "id":"",
                    "remove": false,
                    "start": [0.1,0.2],
                    "end": [0.1,0.1111112],
                    "mid": [],
                    "cluster": "6"
                }
            ]
        }
    ]
}
```


## Success Response

**Code** : `Status 200 OK`

**Content example**
```json
{
    "code": 200,
    "message": "Operation success"
}
```

## Error Response : Các lỗi validate giống phương thức post
**Lỗi không truyền trường "id", "remove" của các camera,zone,route**
```json
{
    "Error": "Bad request"
}
```

**Lỗi truyền vào id camera, zone, route sai**
```json
{
    "message": "Error!!! route not found."
}
```