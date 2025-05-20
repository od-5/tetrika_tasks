def strict(func):
    def wrapper(*args):
        allowed_types = (bool, int, float, str)
        func_args = tuple(func.__annotations__.values())
        for index, arg in enumerate(args):
            if (type(arg) != func_args[index]) or type(arg) not in allowed_types:
                raise TypeError
        return func(*args)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
