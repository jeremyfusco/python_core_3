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

from array import *

# Here is where I discover you must predeclare a definition in Python. Feels like Perl 4.
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

