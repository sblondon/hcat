#! /usr/bin/env python
#
# this script is provided under GPL v3 or upper

import sys

import pygments

from pygments.lexers import get_lexer_for_filename, guess_lexer
from pygments.formatters import Terminal256Formatter


def main():
    OFFSET = 1
    numbers_of_files = len(sys.argv) - OFFSET
    if numbers_of_files:
        for i in range(numbers_of_files):
            filename = sys.argv[i + OFFSET]
            if filename == "-":
                data, lexer = parse_stdin()
            else:
                data, lexer = parse_file(filename)
            display(data, lexer)
    else:
        data, lexer = parse_stdin()
        display(data, lexer)

def parse_stdin():
    f = sys.stdin
    data = f.read()
    try:
       lexer = guess_lexer(data)
    except pygments.util.ClassNotFound:
       lexer = None
    return data, lexer

def parse_file(filename):
    with open(filename) as f:
        data = f.read()
    try:
        lexer = get_lexer_for_filename(filename)
    except pygments.util.ClassNotFound:
        try:
            lexer = guess_lexer(data)
        except pygments.util.ClassNotFound:
            lexer = None
    return data, lexer

def display(data, lexer):
    if lexer:
        print(pygments.highlight(data, lexer, Terminal256Formatter()))
    else:
        print(data)


if __name__ == '__main__':
    main()

