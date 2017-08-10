from functools import reduce

def addDigits(num):

    def fn(x, y):
        return x + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    while num >= 10:
        s = str(num)
        num = reduce(fn, map(char2num, s))
    return num

print(addDigits(38))


