def is_prime(x):
    if x < 2:
        return False
    else:
        primes = []
        for n in xrange(2, x-1):
            primes.append(x%n)
        if 0 in primes:
            return False
        else:
            return True

print is_prime(4)