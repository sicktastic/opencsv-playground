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


def fib2(n):
    memo = {}
    if n in memo:
        return memo(n)
    elif n <= 2:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
        memo[n] = f
        return f

print(fib2(15))

# Bottom up approach

# fib = {}
# for k in range(1, n+1):
#     if k <= 2: f = 1
#     else: f = fib[k-1]+fib[k+2]
#     fib[k] = f
# return fib[n]

