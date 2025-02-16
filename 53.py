def get_total_amount(collection: list, currency: str) -> int:
    new_collection = []
    for i in collection:
        new_collection.append(i.split())
    summa = 0
    for j in new_collection:
        if j[0] == currency:
            summa += int(j[1])
    return summa
