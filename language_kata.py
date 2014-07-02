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
        print(i, ': ', result)
print('Some math!')
simple_math()

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
    print('This is position 0: ', string[0])
    print('This is position 3: ', string[3])
    print('These are positions 3-4: ', string[3:5])
    print('These are positions 3 through end: ', string[3:])
    print('Last position: ', string[-1])
    print('Out of range in slice is handled gracefully', string[12:20])

    print("Length of variable 'string' is",  len(string))
simple_strings()

