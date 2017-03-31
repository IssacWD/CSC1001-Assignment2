# CSC1001-Assignment2
## Question 1
In this question, a random positive number less than the n, of which the square root is to be approximate, is generated as the first guess:`nextGuess = random.uniform(0, n)`. Also, to test the programme, a sample number 9 is input into the function`sqrt(n)`:`print(sqrt(9))     #example`, and the expected value should be around 3:
```bash
bash-3.2$ python3 /Users/apple/q1.py
3.000000000016075
```

## Question 2
In this question, two functions are defined to check if a number is prime or emirp:
```Python
def IsPrime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True

def IsEmirp(x):
    if IsPrime(x):
        X = str(x)[::-1]
        if IsPrime(int(X)):
            return True
        else:
            return False
    else:
        return False
```
For the sake of formatting, a function is used to calculate the digits of the 100th emirp:
```Python
def digits_of_emirp(n):
    count = 0
    p = 13
    while count < n:
        if IsEmirp(p):
            count += 1
        p += 1
    return len(str(p-1))
```
and the digits was worked out as 4. So in the next function`find_emirp(n)`, "4" as a parameter is used in the regular expression:
```Python
if count % 10 == 0:
    print('{:>4}'.format(str(p)))
else:
    print('{:>4}'.format(str(p)), end='  ')
```

## Question 3
Four functions are defined to test the credit card number step by step. In function`sumOfDoubleEvenPlace(number)`, slicing is used to get even places from the end of the number:`even_place = number[-2::-2]`. At the beginning, if the user's input is not an integer, the programme will display:`Please enter your credit card number as an integer:`again.

## Question 4
In this question, two lists are used to keep the letters of the two strings respectively, and these two lists will be sort before they are checked if they are identical. The core codes are as follows:
```Python
def isAnagram(s1, s2):
    list1 = []
    list2 = []
    for i in s1:
        list1.append(i)
    for i in s2:
        list2.append(i)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
```
Sample output is as follows:
```bash
bash-3.2$ python3 /Users/apple/q4.py
Please enter a word:listen
Please enter another word for comparison:silent
is an anagram
```

## Quesntion 5
Though it is feasible to follow the hint, using a list to keep the previous locker status is still dull. Thus another algorithm is applied here. Suppose each locker is assigned an item number, such as 1, 2, 3, etc. In fact, the number of times that a specific locker is to be changed for depends on the number of positive factors of its item number. That is, the locker can only be changed by the student whose number is a factor of the locker's item number. Hence, the first step is to find the number of positive factors of the locker's item number, say, p. Then (-1) denotes 'closed' and 1 denotes 'open', and each change to it is recorded by times the (-1) or 1 by (-1). As all the lockers are (-1) initially, their ending status must be (-1)*(-1)^p. Finally, it can be concluded that if p is even, the locker should be (-1) – that is, closed, and if p is odd, the locker is open. 
The core codes are as follows:
```Python
def statusOfLocker(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        return 'closed'
    else:
        return 'open'
```
The the item numbers of the lockers that are open after all changes are:
`These lockers are open: 1  4  9  16  25  36  49  64  81  100`

## Question 6
In this question, the programme starts assigning the queens from the first row and move to the next row if no queen is under attacked in the previous rows. So a function is defined to check if there is queen under attacked:
```Python
def under_attack(col, existing_queens):
    a = b = col
    for r, c in reversed(existing_queens):
        a, b = a - 1, b + 1
        if c in (a, col, b):
            return True
    return False
```
The `reversed()`in it is to ensure the order of checking so that the function will not skip any possibility. And then a function is used to generate queens according to the present number of queens, say, n:
```Python
def generateQueens(n):
    if n == 0: return [[]]
    previous_solutions = generateQueens(n-1)
    return [solution + [[n, i]]
        for i in range(1, 9)
            for solution in previous_solutions
                if not under_attack(i, solution)]
```
`previous_solutions = generateQueens(n-1)`is for the sake of recursion. This function will contain a new queen and reduce the previous possible queens and keep them in a list for each step during iteration. Therefor it can return all the possible outcomes of queens. In addition, 
```Python
return [solution + [[n, i]]
        for i in range(1, 9)
            for solution in previous_solutions
                if not under_attack(i, solution)]
```
is to prevent the first run of the function when n equals zero, which will cause the function to return `None`so that the iteration`for solution in previous_solutions`cannot work due to the `Nonetype`
After randomly choosing a possibility, a display function is used to format a presentation of the positions of the queens:
```Python
def displayQueens(possible_outcome):
    for r, c in possible_outcome:
        print('|' + ' |'*(c-1) + 'Q|' + ' |'*(8-c))
```
Possible output is as follows:
```bash
bash-3.2$ python3 /Users/apple/q6.py
| | | | |Q| | | |
| | | | | | |Q| |
|Q| | | | | | | |
| | |Q| | | | | |
| | | | | | | |Q|
| | | | | |Q| | |
| | | |Q| | | | |
| |Q| | | | | | |
bash-3.2$ python3 /Users/apple/q6.py
| | |Q| | | | | |
| | | | | |Q| | |
| | | | | | | |Q|
|Q| | | | | | | |
| | | |Q| | | | |
| | | | | | |Q| |
| | | | |Q| | | |
| |Q| | | | | | |
```



