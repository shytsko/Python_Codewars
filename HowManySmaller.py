# https://www.codewars.com/kata/56a1c63f3bc6827e13000006
# This is a hard version of How many are smaller than me?. If you have troubles solving this one,
# have a look at the easier kata first.
#
# Write function smaller(arr) that given an array arr, you have to return the amount of numbers that are smaller
# than arr[i] to the right.
#
# For example:
#
# smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
# smaller([1, 2, 0]) === [1, 1, 0]


def smaller(arr: list):
    res = []
    for i, item in enumerate(arr):
        res.append(len([x for x in arr[i + 1:] if x < item]))
    return res


print(smaller([5, 4, 3, 2, 1])) # [4, 3, 2, 1, 0]
print(smaller([1, 2, 0]))       # [1, 1, 0]
print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]))       # [5, 2, 6, 6, 1, 1, 0, 0, 0, 0]
