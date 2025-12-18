def calcular(v1, v2):
    soma = v1 + v2

    return soma
# refatoração
"""def calcular(v1, v2):
    return v1 + v2"""


if __name__ == '__main__':
    n1 = int(input('Informe o valor 1: '))
    n2 = int(input('Informe o valor 2: '))
    print(f'A soma dos valores {n1} e {n2} é {calcular(n1, n2)}')