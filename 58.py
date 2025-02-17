def unique(collection):
    seen = set()
    unique_items = []
    for item in collection:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items


# BEGIN (write your solution here)
def get_same_count(collection1: list, collection2: list) -> int:
    if len(collection1) == 0 or len(collection2) == 0:
        return 0
    same = set()
    for item in collection1:
        if item in collection2:
            same.add(item)
    return len(same)
