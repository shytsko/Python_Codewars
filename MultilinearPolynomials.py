# https://www.codewars.com/kata/55f89832ac9a66518f000118
# When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x"
# (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!
#
# Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial
# in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression
# has been simplified in the following way ( -> means application of simplify):
#
# All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
# "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"
#
# All monomials appears in order of increasing number of variables, e.g.:
# "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"
#
# If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
# "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"
#
# There is no leading + sign if the first coefficient is positive, e.g.:
# "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"
#
# N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials,
# so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.
#
# Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english
# alphabet.

def simplify(poly: str):
    if poly[0] != '-' and poly[0] != '+':
        poly = '+' + poly
    start = 0
    poly_list = []
    while start < len(poly):
        end = start + 1
        while end < len(poly) and poly[end] != '+' and poly[end] != '-':
            end += 1
        poly_list.append(poly[start:end])
        start = end

    poly_dict = {}
    for item in poly_list:
        k = 1 if item[0] == '+' else -1
        try:
            k *= int(''.join(c for c in item if c.isdigit()))
        except:
            pass
        v = ''.join(sorted([c for c in item if c.islower()]))
        if v in poly_dict:
            poly_dict[v] += k
        else:
            poly_dict[v] = k

    variables = sorted(poly_dict.keys())
    variables.sort(key=len)

    res = []
    for v in variables:
        if poly_dict[v] == -1:
            res.append(f'-{v}')
        elif poly_dict[v] == 1:
            res.append(f'+{v}')
        elif poly_dict[v] != 0:
            res.append(f'{poly_dict[v]:+}{v}')
    return (''.join(res)).lstrip("+")


print(simplify("-a+5ab+3a-c-2a"))  # '-c+5ab'
print(simplify("3a+b+4ac+bc-ab+3a-cb-a-a"))  # '4a+b-ab+4ac'
print(simplify("+n-5hn+7tjhn-4nh-3n-6hnjt+2jhn+9hn"))  # '-2n+2hjn+hjnt'
print(simplify("-y+x"))  # 'x-y'
print(simplify("xzy+zby"))  # 'byz+xyz'
print(simplify("-8fk+5kv-4yk+7kf-qk+yqv-3vqy+4ky+4kf+yvqkf"))  # '3fk-kq+5kv-2qvy+fkqvy'
