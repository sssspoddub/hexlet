def add_prefix(names: list, prefix: str):
    new_names = []
    for name in names:
        new_names.append(prefix + ' ' + name)
    return new_names
