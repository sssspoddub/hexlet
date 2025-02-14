def has_char(string: str, char: str) -> bool:
    new_char = char.lower()
    for i in string:
        if i.lower() == new_char:
            return True
        continue
    return False
