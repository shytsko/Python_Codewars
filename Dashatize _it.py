# https://www.codewars.com/kata/58223370aef9fc03fd000071
# Given a variable n,
#
# If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not
# begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.
#
# If n is not an integer, return the string "None".
#
# Ex:
#
# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'

def dashatize(n):
    if not isinstance(n, int):
        return "None"
    n = abs(n)
    out = []
    for c in str(n):
        if c in {'0', '2', '4', '6', '8'}:
            out.append(c)
        else:
            if len(out) != 0 and out[-1] != '-':
                out.append('-')
            out.append(c)
            out.append('-')
    if out[-1] == '-':
        out.pop()
    return ''.join(out)


print(dashatize(274))  # "2-7-4"
print(dashatize(5311))  # "5-3-1-1"
print(dashatize(86320))  # "86-3-20"
print(dashatize(974302))  # "9-7-4-3-02"
