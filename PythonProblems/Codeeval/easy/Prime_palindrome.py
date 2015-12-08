'''
Write a program which determines the largest prime palindrome less than 1000.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the largest prime palindrome less than 1000.

929
'''
import math,time
N = 100000
start = time.time()
for i in xrange(2,N):
    non_primes = []
    nrange = int(math.sqrt(N))
    for i in xrange(2,nrange+1):
        for j in xrange(2,N):
            if i*j < N:
                non_primes.append(i*j)
    non_primes = set(non_primes)
primes = [i for i in xrange(2,N) if i not in non_primes]

result = []
for prime in primes:
    st_prime = str(prime)
    if st_prime == st_prime[::-1]:
        result.append(int(st_prime))
print result

print(time.time() - start)
#print sorted(non_primes)
#print sorted(primes)
