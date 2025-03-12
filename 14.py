def get_first_name(name):
    first_name = name.split('_')
    return first_name[0]


def sort_by(method, list):
    new_list = list.copy()
    return sorted(new_list, key=method)
