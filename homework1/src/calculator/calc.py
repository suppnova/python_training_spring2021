def check_power_of_2(a: int) -> bool:
    if not isinstance(a, int):
        raise ValueError
    return a > 0 and (a & (a - 1)) == 0
