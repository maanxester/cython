# cython: profile=True

# Cython compilando

# -a gera um HTML do código convertido e mostra as chamadas
# -i cria um módulo que podemos importar no python
# $ cythonize -a -i fib_py.py

def fib(n):
    a = 0
    b = 1

    # Não existe em C
    for i in range(n):
        a, b = a + b, a

    return a

# Retorna um arquivo C com muitas linhas de código, pois o C precisa entender a tipagem, erros etc.
# Evitando NullPointer, Stack OverFlow.
