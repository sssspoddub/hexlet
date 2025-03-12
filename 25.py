def toggle(flag, data):
    if flag in data:
        data.remove(flag)
    else:
        data.add(flag)


def toggled(flag, data):
    new_data = data.copy()
    toggle(new_data)
    return new_data
