def nth_power(n, fn = lambda x: x**3):
    '''calculates power for number upto n
    args:
        n: highest number in the list of numbers
        power: power for numbers to false, default is 3'''
    return [fn(i) for i in range(n)]


print(nth_power(10))
