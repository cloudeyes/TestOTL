import os

from distutils.core import setup
from Cython.Build import cythonize

from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules=cythonize(Extension(
    "dbtransfer",
    include_dirs=[os.path.abspath("./include"), os.path.abspath("./include/oracle/11g")],
    library_dirs=[os.path.abspath("./lib/oracle/11g/x64")],
    libraries=["oci", "odbc32"],
    sources=["src/cython/dbtransfer.pyx", "src/cpp/dbtransfer.cpp"],
    language="c++",
)))
