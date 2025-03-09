def apply_diff(items, dictionary):
    if "add" in dictionary:
        items |= dictionary['add']
    if "remove" in dictionary:
        items -= dictionary['remove']
