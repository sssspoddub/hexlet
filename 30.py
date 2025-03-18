def id_generator(prefix):
    counter = 0

    def id_continuation():
        nonlocal counter
        counter += 1
        return f'{prefix}-{counter:03d}'
    return id_continuation


user_id = id_generator("USER")
print(user_id())
print(user_id())
print(user_id())
print(user_id())
print(user_id())
print(user_id())
