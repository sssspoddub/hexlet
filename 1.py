def make_user(name: str, age: int):
    return {"name": name, "age": age}


def format_user(user):
    return f'{user["name"]}, {user["age"]}'
