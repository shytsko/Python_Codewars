# https://www.codewars.com/kata/55983863da40caa2c900004e

# Create a function that takes a positive integer and returns the next bigger number that can be formed by
# rearranging its digits. For example:
#
#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):
#
#   9 ==> -1
# 111 ==> -1
# 531 ==> -1
from itertools import permutations


def next_bigger(n: int):
    digits = list(str(n))
    res = -1
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            tmp = sorted(digits[i + 1:])
            for j in range(len(tmp)):
                if digits[i] < tmp[j]:
                    digits[i], tmp[j] = tmp[j], digits[i]
                    tmp.sort()
                    break
            res = int(''.join(digits[:i + 1] + tmp))
            break
    return res


print(next_bigger(12))  # 21
print(next_bigger(21))  # -1
print(next_bigger(513))  # 531
print(next_bigger(2017))  # 2071
print(next_bigger(414))  # 441
print(next_bigger(144))  # 414
print(next_bigger(1234567890))  # 1234567908
