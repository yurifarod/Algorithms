import numpy as np

#transfer function
def stepfunction(soma):
    if(soma >= 1):
        return 1
    return 0

def sigmoidfunction(soma):
    return 1/(1 + np.exp(-soma))

def tahnfunction(soma):
    vl = (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))
    return vl
    
def linearfunction(soma):
    return soma

def relufunction(soma):
    if soma >= 0:
        return soma
    return 0

def softmaxfunction(x):
    ex = np.exp(x)
    return ex / ex.sum()

teste = stepfunction(30)
teste2 = sigmoidfunction(2.1)
teste3 = tahnfunction(2.1)
teste4 = relufunction(2.1)
teste5 = linearfunction(2.1)

valores = [5.0, 2.0, 1.3]
teste6 = softmaxfunction(valores)

print(teste)
print(teste2)
print(teste3)
print(teste4)
print(teste5)
print(teste6)
