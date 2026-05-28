import random

def troco_minimo(moedas, valor):

    dp = [float('inf')] * (valor + 1)

    dp[0] = 0

    for x in range(1, valor + 1):

        for moeda in moedas:

            if moeda <= x:
                dp[x] = min(dp[x], dp[x - moeda] + 1)

    return dp[valor]

notas = [1, 2, 5, 10, 20, 50, 100, 200]
print(troco_minimo(notas, 1123))

random_list = random.sample(range(101, 10101), 20)
print(random_list)