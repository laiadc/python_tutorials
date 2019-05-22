
"""
In order to build the cythoned version of a function the following command can be used:

python3 setup_cython_functions.py build_ext --inplace

This command should create a file:  sum_cy.cpython-36m-darwin.so

"""

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("./cython_code/cy_func.pyx"))
setup(ext_modules = cythonize("./cython_code/cy_func2.pyx"))
#setup(ext_modules = cythonize("./cython_code/cy_func2.py"))
