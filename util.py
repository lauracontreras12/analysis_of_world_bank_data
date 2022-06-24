def nth_power(n, power):
    '''calculates power for number upto n'''
    return [i**power for i in range(n)]


print(nth_power(10, 4))