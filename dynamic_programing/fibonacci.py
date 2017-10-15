# Source https://www.youtube.com/watch?v=OQ5jsbhAv_M&t=2315s
#DP "careful brute force"
#DP subproblems + "reuse"

# Navie recursive algorightm

def fib(n):
    if n <= 2:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
        return f

print(fib(10))

# Bad algorithm = exponential time

# Memoized DP alogrithm

memo = {}

def fib2(n):
    if n in memo:
        return memo(n)
    elif n <= 2:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
        memo[n] = f
        return f

print(fib2(15))
