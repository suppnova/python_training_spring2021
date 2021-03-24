def cache(times):
    def inner(func):
        counter = 0
        cache_dict = {}

        def wrapped_func(*args):
            nonlocal counter
            nonlocal cache_dict
            counter += 1
            if counter > times:
                counter = 1
                result = func(*args)
                cache_dict[args] = result
            if args in cache_dict:
                return cache_dict[args]
            result = func(*args)
            cache_dict[args] = result
            return result

        return wrapped_func

    return inner


@cache(times=3)
def function(a, b):
    return (a ** b) ** 2
