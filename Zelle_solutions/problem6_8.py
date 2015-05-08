def nextGuess(guess, x, n):
    count = 0
    while count < n:
        guess = (guess + (x / guess)) / 2.
        count += 1
    return guess

print nextGuess(1, 25, 10)