def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a = sumcount(100)

print(a)

def greeting(name):
    'Issues a greeting'
    print('Hello', name)


greeting('Ronto')
        