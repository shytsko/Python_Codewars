# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.
# Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.
# The sum of these squares is 84100 which is 290 * 290.
#
# Task
# Find all integers between m and n (m and n integers with 1 <= m <= n)
# such that the sum of their squared divisors is itself a square.
#
# We will return an array of subarrays or of tuples (in C an array of Pair) or a string.
# The subarrays (or tuples or Pairs) will have two elements: first the number
# the squared divisors of which is a square and then the sum of the squared divisors.
#
# Example:
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]

def list_squared(m, n):
    result = []
    for x in range(m, n + 1):
        dividers = set()
        if int(x ** 0.5) ** 2 == x:
            dividers.add(int(x ** 0.5))
        for d in range(1, int(x ** 0.5)+1):
            if x % d == 0:
                dividers.add(d)
                dividers.add(x // d)
        sum_dividers = sum(d ** 2 for d in dividers)
        if int(sum_dividers ** 0.5) ** 2 == sum_dividers:
            result.append([x, sum_dividers])
    return result


print(list_squared(1, 250))     # [[1, 1], [42, 2500], [246, 84100]]
print(list_squared(42, 250))    # [[42, 2500], [246, 84100]]
print(list_squared(250, 500))   # [[287, 84100]]
