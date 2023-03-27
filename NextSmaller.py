# https://www.codewars.com/kata/5659c6d896bc135c4c00021e
# Write a function that takes a positive integer and returns the next smaller positive integer containing
# the same digits.
#
# For example:
#
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains
# the same digits. Also return -1 when the next smaller number with the same digits would require the leading
# digit to be zero.
#
# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros


def next_smaller(n):
    digits = list(str(n))
    res = -1
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            tmp = sorted(digits[i + 1:], reverse=True)
            for j in range(len(tmp)):
                if digits[i] > tmp[j]:
                    digits[i], tmp[j] = tmp[j], digits[i]
                    tmp.sort(reverse=True)
                    break
            if digits[0] == '0':
                break
            res = int(''.join(digits[:i + 1] + tmp))
            break
    return res


print(next_smaller(907))  # 790
print(next_smaller(531))  # 513
print(next_smaller(135))  # -1
print(next_smaller(2071))  # 2017
print(next_smaller(414))  # 144
print(next_smaller(123456798))  # 123456789
print(next_smaller(123456789))  # -1
print(next_smaller(1234567908))  # 1234567890
