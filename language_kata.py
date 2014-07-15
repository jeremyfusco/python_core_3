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

# end replaces newline with a multi-line string.
print('Hello world in English and Chinese: ', end='')
print("Hello World! 你好世界")

# Here is where I discover you must pre-declare a definition in Python. Feels like Perl 4.
# if you don't have cold folding this is going to look very, very ugly.
def simple_math():
    equations = ['2 + 2',
                 '50 - 5*6',
                 '(50 - 5*6) / 4',
                 '8 / 5',  # Division ALWAYS returns a floating point number.
                 '17 / 3',  # Another example, always a float.
                 '17 // 3',  # 'floor' division discards the fraction.
                 '17 % 3',  # modulus returns the remainder
                 '5 * 3 + 2',  # ( Result * divisor ) + remainder
                 '5 ** 2',  # 5 Squared
                 '2 ** 7',  # 2 to the power of 7
                 '3 * 3.75 / 1.5',  # Floating point operators with mixed type operands convert the integer operand to
                 # floating
                 '7.0 / 2',  # Continued
                 'print("Need decimal and Fraction example")'
                 ]

    for i in equations:
        result = eval(i)
        print(i, ':', result)


print('Some math!')
# simple_math()

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
               'automatic' ' ' 'concatenation',
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

    print("Length of variable 'string' is", len(string))


print('Some strings!')
# simple_strings()

def simple_lists():
    print("Note: Lists are mutable")

    list_of_squares = [1, 4, 9, 16, 25]
    print("List of squares 4 and 9", list_of_squares[1:3])

    concatenated_list = list_of_squares + [1, 2, 3, 4]
    print("concatenated list", concatenated_list)

    concatenated_list[0] = 10000
    print("'concatenated_list' updated so the first element is 10000:", concatenated_list[0])

    concatenated_list.append('All your appended are belong to .append')
    print("Appended a value to concatenated_list via .append", concatenated_list[-1])

    concatenated_list[0:4] = [0, 1, 2, 3, 4]
    print("Replaced elements 0 through: 4", concatenated_list[0:5])

    concatenated_list[:] = []
    print('Completely cleared the concatenated_list -->', concatenated_list[:], '<---')

    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    as_easy_as = [a, b]
    print('Multidimensional arrays are so much easier:', as_easy_as)

    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print("A list 'x' comprised of two lists, 'a' and 'n' respectively", x)
    print("x[0] refers to the index of the first list:", x[0])
    print("x[0][0] refers to the first element in the first list:", x[0][0])


print("Some simple_lists")
# simple_lists()

def simple_fibonacci(max):
    a, b = 0, 1
    while b < max:
        print(b)
        a, b = b, a + b


print("fibonacci")
# simple_fibonacci(13)

def loop_over_slice_copy():
    words = ['one', 'two', 'three', 'longer_then_6_characters']

    for word in words[:]:  # Creates a slice copy of the entire list.
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
    max = max + 1  # Include 'max' for human consumption.
    for n in range(2, max):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
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

def scope_l():
    l = [1]

    # Defines a default value for l. This effectively creates a local instance of 'l' that is
    # Persistent between calls.
    # If l is specified on the call to this routine functional_persistence_local(1, 2) for example.
    # The persistent value will be overwritten.

    # Make a copy of the global L as opposed to (a, local_l=l) as this will create a reference
    # To the global and MODIFY IT.
    def functional_persistence_local(a, local_l=l[:]):
        local_l.append(a)
        return local_l

    # L is overwritten with [] for every subsequent call, if L is not passed. that is to say:
    #   functional_persistence_local_L(1), as opposed to (1, [11]).
    #  Declaring a variable in the def string localizes the named variable to the lexical scope of
    #  The function. Which acts a closure.
    def functional_persistence_local_l(a, l=None):
        if l is None:
            l = []  # Define a local instance of L
        l.append(a)
        return l

    if True:
        print("Persistence local", functional_persistence_local(1))
        print("Persistence local", functional_persistence_local(2))

    if True:
        print("l is overwritten for every call", functional_persistence_local_l(1, [11]))
        print("l is overwritten for every call", functional_persistence_local_l(2, [12]))

# *formal is is  'variadic' argument which scoops up non keyword and non specified keyword arguments that would normally
# precede it.
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

def make_lambda_incrementer(n):
    return lambda x: x + n


print('lambda!')
f_incrementer = make_lambda_incrementer(1)

pairs = [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# lambda defines x, and performs the x[1] evaluation to sort.
# In this case x[1] will always be the 2nd value of the list being passed.
pairs.sort(key=lambda x: x[1])
print(pairs)

# List methods.
def list_examples():
    a = [66.25, 333, 333, 1, 1234.5]
    print("Initial list: ", a)
    print("Result of .count methods: ", a.count(333), a.count(66.25), a.count('x'))

    a.insert(2, -1)
    a.append(333)
    print("List a after insert and append operations: ", a)
    print("index of the first instance of '333': ", a.index(333))

    a.remove(333)
    print("First instance of '333' removed via .remove: ", a)

    a.reverse()
    print("'.reverse' applied to a", a)

    a.sort()
    print("'.sort', applied to a", a)

print("List methods")
list_examples()

def list_stack():
    stack = [3, 4, 5]
    print("'stacks' initial state", stack)
    stack.append(6)
    stack.append(7)
    print("6 and 7 appended by seperate .append method calls: ", stack)
    stack.pop()
    stack.pop()
    stack.pop()
    print("3 consecutive calls", stack)

print("Using a list as a stack")
list_stack()

def lists_as_queues():
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    print("queue is a deque type. Initial list:", queue)
    queue.append("Terry")
    queue.append("Graham")
    print("We've '.append'ed Terry and Graham to the queue:", queue)
    currently_serving = queue.popleft()
    print(currently_serving, "has been popleft from the queue:", queue)
    currently_serving = queue.popleft()
    print(currently_serving, "has been popleft from the queue:", queue)
    print("'queue' after the above operations:", queue)

print("Using a deque object from 'collections'")
lists_as_queues()

def create_list_of_squares():
    squares = [x ** 2 for x in range(10)]
    print("entire comprehension assignment:", squares)
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print("Iterative '.append' method call:", squares)

print("List comprehensions. Lists can be created iteratively or")
print("by generating the entire list and assigning.")
create_list_of_squares()

# returns a list of tuples.
def compare_two_lists_by_for_loops(passed_x, passed_y):
    combs = []
    for x in passed_x:
        for y in passed_y:
            if x != y:
                combs.append((x, y))
    return combs

# returns a list of tuples.
def compare_two_lists_by_list_comprehension(passed_x, passed_y):
    combs = [(x, y) for x in passed_x for y in passed_y if x != y]
    return combs

print("Compare by for loops:", compare_two_lists_by_for_loops([1, 2, 3], [3, 1, 4]))
print("By list comprehension:", compare_two_lists_by_list_comprehension([1, 2, 3], [3, 1, 4]))

# Simple strip applied via a comprehension list.
def strip_method(passed_list):
    return [item.strip() for item in passed_list]

print("Stripped list:", strip_method(['one ', 'two  ', 'three   ']))

def transpose_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    return [[row[column] for row in matrix] for column in range(4)]

print("tranpose_matrix:", transpose_matrix())

def delete_from_list(x):
    list = [0, 1, 2, 3, 4, 5]
    del list[x]
    return list

print("this list had element 2 deleted:", delete_from_list(2))

def null_and_single_tuple_declaration():
    singleton = 'hello',  # the ',' denotes that this is a list with one indexed item at location 0.
                          # We would have a string otherwise.
    empty = ()

    print("lengths of singleton and empty:", len(singleton), len(empty))

null_and_single_tuple_declaration()

def basic_sets():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    check_for = ['orange', 'crabgrass']
    for item in check_for:
        if item in basket:
            print("Checking for", item, end=' ')
            print("have", item)

basic_sets()

def set_comprehension():
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)

set_comprehension()

def additional_set_operations_unique_letters_two_words():
    a = set('abracadabra')
    b = set('alacazam')

    print("set a:", a)
    print("set b:", b)
    print("a-b", a - b)
    print("a | b", a | b)
    print("a & b", a & b)
    print("a ^ b", a ^ b)

print("mathematical and logical operators performed on sets.")
additional_set_operations_unique_letters_two_words()

def simple_dictionaries():
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print("entire dictionary tel:", tel)

    del tel['sape']
    print("tel after deletion of sape:", tel)

    tel['irv'] = 4127

    print("All of the dictionaries keys:", list(tel.keys()))
    print("sorted list of keys:", sorted(tel.keys()))

    if 'guido' in tel:
            print("'guido' has an entry")
    if 'jack' not in tel:
        print("'jack' not in tel")

    tel2 = dict([
        ('sape', 4139),
        ('guido', 4127),
        ('jack', 4098)
       ])
    print("tel2 defined with dict constructor", tel2)

    tel3 = dict(sape=4139, guido=4127, jack=4098)
    print("tel3 created with paris of keyword args", tel3)

simple_dictionaries()

def looping_techniques():
    print("Dictionary printed")
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)

    print("Enumerated list")
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']

    for q, a in zip(questions, answers):
        print('What is your {0}? It is {1}.'.format(q,a))

    numbers = [1, 2, 3]
    for i in reversed(numbers):
        print(i)

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)

    words = ['cat', 'window', 'defenestrate']
    print("Word(s) longer then 6 characters long will be prepended:", words)
    for w in words[:]:
        if len(w) > 6:
            words.insert(0, w)
    print(words)
looping_techniques()

import fibo

fibo.fib(1000)
print(fibo.fib2(1000))

def print_fib_from_module():
    fib = fibo.fib
    fib(1000)
print_fib_from_module()

# List all names currently defined.
if(False):
    print(dir())

import sys
print(sys.path)

def simple_string_examples():
    s = 'Hello, world.\n'
    print(str(s))
    print(repr(s))
    object = ('one', 'two')
    print(str(object))
    print(repr(object))

    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

    print('Test {0} of the formatting method.'.format('one'))

    print('Test {test} of the formatting method.'.format(test='two'))
    print('Test {!r} of the formatting method.'.format('three\n'))
    import math
    print('Floating point test, 5 places of PI, NOTE .format rounds up!!! {0:.5f}'.format(math.pi))

    table = {'one': 1, 'two': 2, 'three': 3}
    for name, phone in table.items():
        print('{0:10} --- {1:10d}'.format(name, phone))

    print('one is here {0[one]:d}'.format(table))

print("Simple strings!")
simple_string_examples()

def simple_file_operations():
    # Defaults to a text file in utf-8.
    # Append 'b' to the mode, (mode)b to write binary.
    # Modes: (r)ead, over(w)rite, (a)ppend, (r+)ead and write.
    f = open('pykatafile', 'w+')

    f.write('Hello file!\n')
    f.write('second line')

    print("reading from file", f.readline(), f.readline())

    for line in f:
        print(line)

    b = open('binary.file', 'wb+')
    b.write(b'0123456789abcdef')
    b.seek(5)
    print(b.read(1))

    f.close()
    b.close()

simple_file_operations()

def store_an_object_via_pickle():
    import pickle
    simple_dictionary = {'one': 1, 'two': 2, 'three': 3}

    p = open('pickled', 'wb+')
    pickle.dump(simple_dictionary, p)
    p.close()

#store_an_object_via_pickle()

def load_an_object_via_pickle():
    import pickle
    p = open('pickled', 'rb')
    pickled = pickle.load(p)
    print(pickled)


load_an_object_via_pickle()
