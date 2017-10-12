import os

from distutils.core import setup
from Cython.Build import cythonize

from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules=cythonize(Extension(
    "dbtransfer",
    include_dirs=[os.path.abspath("."), os.path.abspath("./oracle/include")],
    library_dirs=[os.path.abspath("./oracle/lib/x64")],
    libraries=["oci", "odbc32"],
    sources=["python/dbtransfer.pyx", "dbtransfer.cpp"],
    language="c++",
)))
