def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

n = 5
for i in range(n+1):
    print(f"fib({i}) = {fib(i)}")
