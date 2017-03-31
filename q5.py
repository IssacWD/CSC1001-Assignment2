def statusOfLocker(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        return 'closed'
    else:
        return 'open'

print("These lockers are open:", end = ' ')
for i in range(1, 101):
    if statusOfLocker(i) == 'open':
        print(str(i), end = "  ")
print('\n')