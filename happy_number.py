"""
Happy Number
============

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number either equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.

For example:

7*7 -> 49, 4*4 + 9*9 -> 97
7 => 49 => 97 => 130 => 10 => 1 => Happy!
2 => 4 => 16 => 37 => 58 => 89 => 145 => 42 => 20 => 4 => Loop encountered => Not Happy!

(Full description at https://en.wikipedia.org/wiki/Happy_number.)

Write a method that takes a positive integer and that returns True if the
number is happy, False otherwise.
"""

# Test Cases
if __name__ == '__main__':
    # Happy numbers from 1 to 100, inclusive
    happy_numbers = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82,
                     86, 91, 94, 97, 100]

    # Test each number from 1 to 100
    for n in range(1, 101):
        expected = n in happy_numbers
        assert is_happy(n) is expected
