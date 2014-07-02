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
    max = max + 1 # Include 'max' for human consumption.
    for n in range(2, max):
        for x in range(2,n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:  # Else executes for loops not broken out of 'break'. ( poorly named ).
            print(n, 'is a prime number')

print("Find prime numbers")
#find_primes_to_max(11)

def simple_prompt(prompt, retries=4, complaint='Yes or no.'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 1:
            raise OSError('no answer provided.')
        print(complaint)

print("Simple prompt example.")
#simple_prompt('Do you want that neighbors dog to stop barking?')

L = [1]

# Defines a default value for L. This effectively creates a local instance of 'L' that is
# Persistent between calls.
# If L is specified on the call to this routine functional_persistence_local(1, 2) for example.
# The persistent value will be overwritten.

# Make a copy of the global L as opposed to (a, local_L=L) as this will create a reference
# To the global and MODIFY IT.
def functional_persistence_local(a, local_L=L[:]):
    local_L.append(a)
    return local_L

# L is overwritten with [] for every subsequent call, if L is not passed. that is to say:
#   functional_persistence_local_L(1), as opposed to (1, [11]).
#  Declaring a variable in the def string localizes the named variable to the lexical scope of
#  The function. Which acts a closure.


def functional_persistence_local_L(a, L=None):
    if L is None:
        L = [] # Define a local instance of L
    L.append(a)
    return L

if False:
    print("Persistence local", functional_persistence_local(1))
    print("Persistence local", functional_persistence_local(2))

if False:
    print("L is overwritten for every call", functional_persistence_local_L(1, [11]))
    print("L is overwritten for every call", functional_persistence_local_L(2, [12]))

# *formal is is  variadic argument which scoopes up non keyword and non specified keyword arguments that would normally
# preceed it.
def keyword_args(one, two='two', three='three', *formal, **remaining_keywords):
    print('printing contents of one, two, three', one, two, three)
    for entry in formal:
        print('entry', entry)
    print("-" * 80)
    keys = sorted(remaining_keywords.keys())
    for key in keys:
        print(key, ':', remaining_keywords[key])

print('Passing args to a function!')
#keyword_args('one','two','three', "another extra arg", "another arg with no owner", keyword1='one', keyword2='two')

def make_lambda_incrementor(n):
    return lambda x: x + n

print('lambda!')
f_incrementor = make_lambda_incrementor(1)

pairs = [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# lambda defines x, and performs the x[1] evaluation to sort.
# In thise case x[1] will always be the 2nd value of the list being passed.
pairs.sort(key=lambda x: x[1])
print(pairs)