# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
# Example:
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
#
# The output expected would be:
# apples, pears
# grapes
# bananas
#
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"


def strip_comments(strng: str, markers: list[str]):
    lines = strng.split("\n")
    lines_out = []
    for line in lines:
        comment_start_position = len(line)
        for marker in markers:
            marker_position = line.find(marker, 0, comment_start_position)
            if marker_position != -1:
                comment_start_position = marker_position
        lines_out.append(line[:comment_start_position].rstrip(" "))
    return "\n".join(lines_out)


print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples",
                     ["#", "!"]))  # 'apples, pears\ngrapes\nbananas'
print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))  # 'a\nc\nd'
print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))  # ' a\nc\nd'
print(strip_comments(
    "  oranges watermelons lemons\n' , lemons lemons strawberries pears\n' cherries strawberries oranges cherries cherries",
    ['-', '.', '!']))  #
