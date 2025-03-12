def count_all(collection):
    dictionary = {}
    for item in collection:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


print(count_all(["cat", "dog", "cat"]))
