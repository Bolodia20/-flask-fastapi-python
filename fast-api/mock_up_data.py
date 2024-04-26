from interfaces import HealthStatuses


mock_up_health_data = [
    {"id": 1, "name": "health one", "status": HealthStatuses.BAD},
    {"id": 2, "name": "health two", "status": HealthStatuses.NORMAL},
    {"id": 3, "name": "health three", "status": HealthStatuses.BAD},
    {"id": 4, "name": "health 4", "status": HealthStatuses.NONE},
    {"id": 5, "name": "health 5", "status": HealthStatuses.GOOD},
]

my_user = {
    "name": "Volodya",
    "surname": "Diachuk",
    "email": "bolodian@gmail.com",
    "age": 23,
    "password": "1122",
}


fake_users = {
    "john": {
        "username": "john",
        "surname": "Doe",
        "email": "johndoe@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    },
    "alice": {
        "username": "alice",
        "surname": "Wonderson",
        "email": "alice@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    },
    "volodya": {
        "username": "volodya",
        "surname": "Diachuk",
        "email": "boldi4@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    },
    "taras": {
        "username": "taras",
        "surname": "Gpt",
        "email": "tgpt@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    },
}
