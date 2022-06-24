def nth_power(n, power):
    '''calculates power for number upto n
    args:
        n: highest number in the list of numbers
        power: power for numbers to false, default is 2'''
    return [i**power for i in range(n)]


print(nth_power(10, 4))
