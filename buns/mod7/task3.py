import time

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    memoized_func.__name__ = func.__name__
    memoized_func.__doc__ = func.__doc__
    return memoized_func

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

@timer
@memoize
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))

@timer
def fibonacci_no_memo(n):
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci_no_memo(n - 1) + fibonacci_no_memo(n - 2)

print(fibonacci_no_memo(20))