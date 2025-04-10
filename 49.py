def remove_first_level(tree):
    new_tree = []
    for child in tree:
        if isinstance(child, int):
            continue
        else:
            new_tree.extend(child)
    return new_tree


tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))  # [5, 3, 4]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))
