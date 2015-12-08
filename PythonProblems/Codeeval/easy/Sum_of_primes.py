'''
Write a program which determines the largest prime palindrome less than 1000.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the largest prime palindrome less than 1000.

929

Using the sieve of Eratosthenes algorithm

'''
import time, math
def get_primes(n):
  m = n+1
  numbers = [True for i in range(m)]
  for i in range(2, int(math.sqrt(n))):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes


if __name__ == '__main__':
    start = time.time()
    primes = get_primes(100000)
    print(time.time() - start)
    primes = (get_primes(10000))
    print sum(primes[:1000])


