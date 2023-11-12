def validate_args(func):
    def wrapper(arg):
        if not isinstance(arg, int):
            return 'Wrong types'
        if arg < 0:
            return 'Negative argument'
        return func(arg)
    return wrapper

@validate_args
def my_func(arg):
    return arg