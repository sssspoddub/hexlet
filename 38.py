def get_first_name(name):
    first_name = name.split('_')[0]
    return first_name


def sort_by(function, collection):
    return sorted(collection, key=function)
