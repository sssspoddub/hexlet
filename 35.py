def get_average(*args):
    if not args:
        return None
    else:
        return sum(args) / len(args)
