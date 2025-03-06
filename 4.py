from collections import defaultdict


def collect_indexes(items):
    dictionary = defaultdict(list)
    for index, value in enumerate(items):
        dictionary[value].append(index)
    return dictionary
