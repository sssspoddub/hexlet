def count_all(data):
    dictionary = {}
    for i in data:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary
