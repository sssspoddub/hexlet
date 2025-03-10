def id_generator(prefix):
    id = 0

    def generate_id():
        nonlocal id
        id += 1
        return f"{prefix}-{id:03}"
    return generate_id
