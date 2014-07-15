# Fibonacci numbers module from the Python tutorial 3
# https://docs.python.org/3.2/tutorial/modules.html
# With minor correction. b <= n, whereas the tutorial states
# b < n

def fib(n): # Write Fibonacci series up to n
    a, b = 0, 1
    while b <= n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b <=n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))