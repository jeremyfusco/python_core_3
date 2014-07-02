#!/usr/bin/env python
# -*- coding: utf-8 -*-  # utf-8 is the default, but may specify cp-1252 for windows,
                         # The coding: line must be on the first or second line of the script.
                         # Defined as 'file local variable'
# This script will serve as a 'kata' for the core language.
# It is an attempt to incorporate most if not all of the core language into one file.

# As set by PyCharm when creating a new
__author__ = 'fusco'

# work with these.
# import site
# import os

# end replaces newline with a multiline string.
print('Hello world in English and Chinese: ', end='')
print("Hello World! 你好世界")

# Here is where I discover you must pre-declare a definition in Python. Feels like Perl 4.
# if you don't have cold folding this is going to look very, very ugly.
def simple_math():
    equations = ['2 + 2',
                 '50 - 5*6',
                 '(50 - 5*6) / 4',
                 '8 / 5',           # Division ALWAYS returns a floating point number.
                 '17 / 3',          # Another example, always a float.
                 '17 // 3',         # 'floor' division discards the fraction.
                 '17 % 3',          # modulus returns the remainder
                 '5 * 3 + 2',       # ( Result * divisor ) + remainder
                 '5 ** 2',          # 5 Squared
                 '2 ** 7',          # 2 to the power of 7
                 '3 * 3.75 / 1.5',  # Floating point operators with mixed type operands convert the integer operand to floating.for
                 '7.0 / 2',         # Continued
                 'print("Need decimal and Fraction example")'
                ]

    for i in equations:
        result = eval(i)
        print(i, ':', result)
print('Some math!')
#simple_math()

def simple_strings():
    print("\n\n***Note: Strings are immutable.***\n\n")

    foo = 'foo'

    strings = ['Single level of quotes. escapes work \'.',
                "Double level quotes. escapes work \' but not needed, '.",
                r'raw string no support for\ninterpolation\n',
                """\
String literal denoted by \"\"\"...\"\"\" or '''...'''
Line two test. To prevent indentation, string violates indentation rule.
                """,
                "text multiply by 3\n" * 3,
                'auto' 'matic' ' ' 'concatenation',
                foo + 'bar',
                ('several strings '
                'a part of one concatenation'),
               ]
    for i in strings:
        print(i)

    string = '0123456789'
    print('This is position 0:', string[0])
    print('This is position 3:', string[3])
    print('These are positions 3-4:', string[3:5])
    print('These are positions 3 through end:', string[3:])
    print('Last position:', string[-1])
    print('Out of range in slice is handled gracefully', string[12:20])

    print("Length of variable 'string' is",  len(string))
print('Some strings!')
#simple_strings()

def simple_lists():
    print("Note: Lists are mutable")

    list_of_squares = [1, 4, 9, 16, 25]
    print("List of squares 4 and 9", list_of_squares[1:3])

    concatinated_list = list_of_squares + [1, 2, 3, 4]
    print("concantinated list",concatinated_list )

    concatinated_list[0] = 10000
    print("'concantinated_list' updated so the first element is 10000:", concatinated_list[0])

    concatinated_list.append('All your appended are belong to .append')
    print("Appended a value to concantinated_list via .append", concatinated_list[-1])

    concatinated_list[0:4] = [0, 1, 2, 3, 4]
    print("Replaced elements 0 through: 4", concatinated_list[0:5] )

    concatinated_list[:] = []
    print('Completely cleared the concatenated_list -->', concatinated_list[:], '<---')

    a = [1,2,3]
    b = ['a','b','c']
    as_easy_as = [a,b]
    print('Multidimensional arrays are so much easier:', as_easy_as)

    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print("A list 'x' comprised of two lists, 'a' and 'n' respectively", x)
    print("x[0] refers to the index of the first list:",  x[0])
    print("x[0][0] refers to the first element in the first list:", x[0][0])
print("Some simple_lists")
#simple_lists()

def simple_fibonacci(max):
    a, b = 0, 1
    while b < max:
        print(b)
        a, b = b, a+b
print("fibonacci")
#simple_fibonacci(13)

def loop_over_slice_copy():
    words = ['one', 'two', 'three', 'longer_then_6_characters']

    for word in words[:]:     # Creates a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)
    print(words)
print("Creating a slice copy and modifying the original")
#loop_over_slice_copy()

def loop_over_indices():
    a = ['one', 'two', 'three', 'four']
    for i in range(len(a)):
        print(i, a[i])
print("index walking")
#loop_over_indices()

# numbers that are divisible by one and themselves are primes.
def find_primes_to_max(max):
    ++max # Include 'max' for human consumption.
    for n in range(2, max):
        for x in range(2,n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')

print("Find prime numbers")
find_primes_to_max(10)

