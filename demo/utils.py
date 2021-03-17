from math import sqrt


def is_prime(x: int) -> bool:
    if x < 0:
        return is_prime(-x)
    if x < 5 or x % 2 == 0 or x % 3 == 0:
        return x == 2 or x == 3
    max_i = sqrt(x) + 2
    i = 5
    while i < max_i:
        if x % i == 0 or x % (i + 2) == 0:
            return False
            break
        i += 6
    return True
