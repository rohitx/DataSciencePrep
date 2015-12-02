'''
Write a program which determines the sum of the first 1000 prime numbers.
'''
import math
def generate_prime(the_range):
    the_range = the_range + 1
    range2 = int(math.sqrt(the_range))
    noprimes = set(j for i in xrange(2, range2) for j in xrange(i*2, the_range, i))
    primes = [x for x in range(2,the_range) if x not in noprimes]
    print sum(primes)
    return primes


if __name__ == '__main__':
    primes = generate_prime(1001)
    print primes
    print len(primes)
    #pass
