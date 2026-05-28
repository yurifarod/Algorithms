def fib_bottom_up(n):

    if n <= 1:
        return n
    anterior = 0
    atual = 1

    for _ in range(2, n + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
    return atual

n = 200
print("Resultado do Fibonacci de %d"%n)
print(fib_bottom_up(n))

