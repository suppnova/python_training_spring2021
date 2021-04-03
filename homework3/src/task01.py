def cache(times):
    def inner(func):
        cache_dict = {}

        def wrapped_func(*args):
            nonlocal times, cache_dict
            if args not in cache_dict or times == 0:
                cache_dict[args] = func(*args)
            else:
                times -= 1
            return cache_dict[args]

        return wrapped_func

    return inner
