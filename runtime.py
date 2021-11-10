
from timeit import timeit

py = timeit('fib(93)', number=1_000_000, setup='from fib_py import fib')
cy = timeit('fib(93)', number=1_000_000, setup='from fib_cy import fib')
px = timeit('fib(93)', number=1_000_000, setup='from fib_x import fib')
cc = timeit('fib(93)', number=1_000_000, setup='from c_fib_import import fib')

print("Tempo do Python Puro: ", py)
# 5.0648235

print("Tempo do Cython/Python: ", cy)
# 0.0482075

print("Tempo do Cython Puro: ", px)
# 0.06385587

print("Tempo do C Puro rodando com Wrapper Python: ", cc)
# 0.05352033

print(f'{py/cy}')
# 78.39785144 Python/Cython mais rápido que o Python Puro

print(f'{py/px}')
# 81.40682543

print(f'{py/cc}')
# 103.820361
