
from random import randint
from fib_py import fib

numeros = [randint(0, 93) for x in range(100_000)]


for x in numeros:
    fib(x)

# python -m cProfile -o prof run2.py
# python -m pstats prof

# cProfile "profila" o código Python e retorna um arquivo binário
# pstats torna o arquivo binário legível, para questões de performace
