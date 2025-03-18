
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print("Args:", args, kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper

@debug_decorator
def sum(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(sum(1, 2))