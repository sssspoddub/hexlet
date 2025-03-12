def make_user(name: str, age: int):
    user = {
        'name': name,
        'age': age
    }
    return user


def format_user(user: dict):
    return f'{user['name']}, {user['age']}'


phil = make_user('Phil', 25)
print(type(phil))
print(format_user(phil))
