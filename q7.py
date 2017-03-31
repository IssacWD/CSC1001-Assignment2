def under_attack(col, queens): # You do not need to fill in these fields. This is a helper function for the solve function.
    left = right = col
    for r, c in reversed(queens): # Reversing queens causes them to be iterated over in reverse order.
        left, right = left-1, right+1
        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0: return [[]]
    smaller_solutions = solve(n-1) # It appears that in solving this board, it solves all boards smaller than it in a recursive manner.
    return [solution+[(n,i+1)] # This line appears to be in error. Have you run this code and verified that it runs correctly?
        for i in range(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)]
for answer in solve(BOARD_SIZE): 
    print(answer)


def isSafe(col, existing_queens):
    for a, b in existing_queens:
        if b == col or b - 1 == col or b + 1 == col:
            return False
        else:
            return True