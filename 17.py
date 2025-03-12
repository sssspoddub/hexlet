def get_children(users):
    children = []

    for user in users:
        if 'children' in user:
            children.extend(user['children'])
    return children
