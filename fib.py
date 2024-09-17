def fib(n):
    print(f"fib({n}) called")
    
    if n == 0:
        print(f"fib({n}) returning 0")
        return 0
    if n == 1:
        print(f"fib({n}) returning 1")
        return 1
    
    result = fib(n-1) + fib(n-2)
    print(f"fib({n}) returning {result}")
    
    return result

fib(5)
