def memoized(function):
    cache = {}

    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = function(*args, **kwargs)
        return cache[args]
    return wrapper
