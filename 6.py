def diff_keys(old_items, new_items):
    new_dictionary = {
        'kept': set(old_items.keys()) & set(new_items.keys()),
        'added': set(new_items.keys()) - set(old_items.keys()),
        'removed': set(old_items.keys()) - set(new_items.keys())
    }
    return new_dictionary
