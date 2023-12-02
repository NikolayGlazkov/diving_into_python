# import doctest
# doctest.testfile('prime.md', verbose=True)

def is_prime(p: int) -> bool:
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than one')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take along time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
        return True