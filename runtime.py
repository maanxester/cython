
from timeit import timeit

py = timeit('fib(93)', number=1_000_000, setup='from fib_py import fib')
cy = timeit('fib(93)', number=1_000_000, setup='from fib_cy import fib')
px = timeit('fib(93)', number=1_000_000, setup='from fib_x import fib')

print("Tempo do Python Puro: ", py)
# 4.9648235

print("Tempo do Cython/Python: ", cy)
# 0.0482075

print("Tempo do Cython Puro: ", px)
# 0.05941158


print(f'{py/cy}')
# 103.39785144 Python/Cython mais rápido que o Python Puro

print(f'{py/px}')
# 84.98682543
