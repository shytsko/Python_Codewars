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

def next_bigger(n: int):
    digits = list(str(n))
    next_big = n
    for i in range(len(digits) - 1):
        if digits[i] < digits[i + 1]:
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
            temp = int(''.join(digits))
            if next_big == n or next_big > temp:
                next_big = temp
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
    return next_big if next_big > n else -1


print(next_bigger(12))  # 21
print(next_bigger(21))  # -1
print(next_bigger(513))  # 531
print(next_bigger(2017))  # 2071
print(next_bigger(414))  # 441
print(next_bigger(144))  # 414
print(next_bigger(1234567890))  # 1234567908
