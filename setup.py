from Cython.Build import cythonize
from distutils.core import setup, Extension

exts = cythonize(
    [Extension(
        'c_fib_import',
        sources=['c_fib.c', 'c_fib_import.pyx']
    )]
)

setup(
    ext_modules=exts
)
