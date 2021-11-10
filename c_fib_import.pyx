cdef extern from 'c_fib.h':
    unsigned long long c_fib(int n)

# Wrapper
def fib(n):
    return c_fib(n)