test_link = 'https://petstore.swagger.io/v2'

obj_links = {
    'pet': 'pet',
    'order': 'store/order',
    'user': 'user'
}

params_to_check = {
    'pet': ['name', 'photoUrls', 'status'],
    'order': ['petId', 'quantity', 'status', 'complete'],
    'user': ['username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus']
}

payload = {
    'pet': {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "bubenchik",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "my_test_available"
    },

    'order': {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2024-09-19T16:09:54.714Z",
        "status": "placed",
        "complete": True
    },

    'user': {
        "id": 0,
        "username": "UncommonUserName200924",
        "firstName": "Valdemar",
        "lastName": "Valdemarov",
        "email": "emailaddress",
        "password": "not12345",
        "phone": "9876543210",
        "userStatus": 0
    },

    'user_list': [
        {
            "id": 0,
            "username": "UncommonUserName200924",
            "firstName": "Valdemar",
            "lastName": "Valdemarov",
            "email": "emailaddress",
            "password": "not12345",
            "phone": "9876543210",
            "userStatus": 0
        },
        {
            "id": 0,
            "username": "UncommonUserName2009242",
            "firstName": "Svyatozar",
            "lastName": "Svyatozarov",
            "email": "emailaddress2",
            "password": "not54321",
            "phone": "9876543210",
            "userStatus": 0
        }
    ]
}

payload_updt = {
    'pet': {
        "id": 0,
        "category": {
            "id": 1,
            "name": "new_string"
        },
        "name": "bubenchik",
        "photoUrls": [
            "link_text"
        ],
        "tags": [
            {
                "id": 2,
                "name": "another_new_string"
            }
        ],
        "status": "my_test_sold"},

    'order': {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2024-09-19T16:09:54.714Z",
        "status": "placed",
        "complete": True
    }
}
