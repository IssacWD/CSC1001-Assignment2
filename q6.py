import random
def under_attack(col, existing_queens):
    a = b = col
    for r, c in reversed(existing_queens):
        a, b = a - 1, b + 1
        if c in (a, col, b):
            return True
    return False

def generateQueens(n):
    if n == 0: return [[]]
    previous_solutions = generateQueens(n-1)
    return [solution + [[n, i]]
        for i in range(1, 9)
            for solution in previous_solutions
                if not under_attack(i, solution)]

def displayQueens(possible_outcome):
    for r, c in possible_outcome:
        print('|' + ' |'*(c-1) + 'Q|' + ' |'*(8-c))

k = random.randint(1, 9)
possible_outcome = generateQueens(8)[k]
displayQueens(possible_outcome)