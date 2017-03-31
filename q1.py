import random

def sqrt(n):
    while True:
        nextGuess = random.uniform(0, n)
        if nextGuess != 0:
            break
    while True:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n/lastGuess)) / 2
        if abs(nextGuess - lastGuess) <= 0.00001:
            break
    return nextGuess

print(sqrt(9))     #example