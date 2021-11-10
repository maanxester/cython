# cython: profile=True

# Cython compilando

# -a gera um HTML do código convertido e mostra as chamadas
# -i cria um módulo que podemos importar no python
# $ cythonize -a -i fib_py.py

# def fib(n: int) -> int:  # Implementação de type hints
#     a: int = 0
#     b: int = 1
#
#     # Não existe em C
#     for i in range(n):
#         a, b = a + b, a
#
#     return a

import cython


def fib(n: cython.int):  # Tipagem em C
    i: cython.int
    a: cython.ulonglongint = 0
    b: cython.ulonglongint = 1

    for i in range(n):
        a, b = a + b, a


# Retorna um arquivo C com muitas linhas de código, pois o C precisa entender a tipagem, erros etc.
# Evitando NullPointer, Stack OverFlow.
