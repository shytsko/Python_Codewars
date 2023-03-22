# https://www.codewars.com/kata/52b757663a95b11b3d00062d
# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even
# indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
# The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper
# cased and you need to start over for each word.
#
# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if
# there are multiple words. Words will be separated by a single space(' ').
#
# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

def to_weird_case(words: str) -> str:
    word_list = words.split()
    for i, word in enumerate(word_list):
        word_list[i] = ''.join([char.upper() if j % 2 == 0 else char.lower() for j, char in enumerate(word)])
    return ' '.join(word_list)


print(to_weird_case('This'))
print(to_weird_case('is'))
print(to_weird_case('THIs iS a TEST'))
