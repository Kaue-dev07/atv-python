def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def fatorial(n):
    resultado = 1

    for x in range(1, n + 1):
        resultado *= x

    return resultado