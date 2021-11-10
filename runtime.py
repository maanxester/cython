
from timeit import timeit

py = timeit('fib(93)', number=1_000_000, setup='from fib_py import fib')
cy = timeit('fib(93)', number=1_000_000, setup='from fib_cy import fib')

print("Tempo do Python Puro: ", py)
# 4.7648235

print("Tempo do Cython: ", cy)
# 2.46563233

print(f'{py/cy}')
# 2.029194894 mais rápido que o Python Puro
