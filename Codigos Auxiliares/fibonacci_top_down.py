def fib_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]

n = 200
print("Resultado do Fibonacci de %d"%n)
print(fib_top_down(n))

