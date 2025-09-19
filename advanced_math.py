import math

def power(base, exponent):
    return base ** exponent

def square_root(number):
    return math.sqrt(number)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print("2^3 =", power(2, 3))
    print("sqrt(16) =", square_root(16))
    print("5! =", factorial(5))
