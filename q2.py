def IsPrime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True

def IsEmirp(x):
    if IsPrime(x):
        X = str(x)[::-1]
        if IsPrime(int(X)):
            return True
        else:
            return False
    else:
        return False

def digits_of_emirp(n):
    count = 0
    p = 13
    while count < n:
        if IsEmirp(p):
            count += 1
        p += 1
    return len(str(p-1))

def find_emirp(n):
    p = 13
    count = 0
    while count < n:
        if IsEmirp(p):
            count += 1
            if count % 10 == 0:
                print('{:>4}'.format(str(p)))
            else:
                print('{:>4}'.format(str(p)), end='  ')
        p += 1

find_emirp(100)