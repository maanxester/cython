
from timeit import timeit

py = timeit('fib(93)', number=1_000_000, setup='from fib_py import fib')

print("Tempo do Python Puro: ", py)
# 4.7648235
