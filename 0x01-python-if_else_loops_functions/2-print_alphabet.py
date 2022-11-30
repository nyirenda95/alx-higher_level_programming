#!/usr/bin/python3
# 2-print_alphabet.py
for letter in range(97, 123):
    """Print the alphabet in lowercase, not followed by a new line."""
    print("{}".format(chr(letter)), end="")
