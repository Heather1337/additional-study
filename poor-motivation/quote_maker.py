import sys
from random import choice


quotes = []
def open_and_read_file(file_name):
    """Take list of files. Open them, read them, and return one long string."""

    text_file = open(file_name)
    for line in text_file:
        quotes.append(line)

    return quotes

def choose_random_quote(quotes):
    quote = choice(quotes)
    return quote

open_and_read_file('motivation.txt')
# choose_random_quote(quotes)