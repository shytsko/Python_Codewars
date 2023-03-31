# https://www.codewars.com/kata/537e18b6147aa838f600001b
# Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined
# text and the expected justification width. The longest word will never be greater than this width.
#
# Here are the rules:
#
# Use spaces to fill in the gaps between words.
# Each line should contain as many words as possible.
# Use '\n' to separate lines.
# Gap between words can't differ by more than one space.
# Lines should end with a word not a space.
# '\n' is not included in the length of a line.
# Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
# Last line should not be justified, use only one space between words.
# Last line should not contain '\n'
# Strings with one word do not need gaps ('somelongword\n').

def justify(text: str, width: int) -> str:
    text_words = text.split()
    lines = []
    while text_words:
        sum_word_lens = 0
        words_in_line = []
        while text_words and sum_word_lens + len(words_in_line) + len(text_words[0]) <= width:
            words_in_line.append(text_words.pop(0))
            sum_word_lens += len(words_in_line[-1])

        if not text_words or len(words_in_line) < 2:
            lines.append(' '.join(words_in_line))
        else:
            space_btw_word = (width - sum_word_lens) // (len(words_in_line) - 1)
            more_spaces = width - (sum_word_lens + space_btw_word * (len(words_in_line) - 1))
            line_p1 = (" " * (space_btw_word + 1)).join(words_in_line[:more_spaces + 1])
            line_p2 = (" " * space_btw_word).join(words_in_line[more_spaces + 1:])
            line = line_p1 + " " * space_btw_word + line_p2
            lines.append(line)
    return "\n".join(lines)


print(justify(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum " \
    "ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. " \
    "Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat " \
    "c. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse " \
    "rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. " \
    "In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. " \
    "Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla " \
    "et dolor.", 15))
