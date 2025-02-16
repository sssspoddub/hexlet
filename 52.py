def get_same_parity(collection: list):
    if len(collection) == 0:
        return []
    new_collection: list = []
    even = collection[0] % 2
    for i in collection:
        if i % 2 == even:
            new_collection.append(i)
    return new_collection
