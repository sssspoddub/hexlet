def remove_first_level(tree):
    new_tree = []
    for node in tree:
        if isinstance(node, int):
            continue
        else:
            new_tree.extend(node)
    return new_tree
