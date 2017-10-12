cimport dbtransfer
from dbtransfer cimport otl_connect

cdef class TestDB:
    cdef otl_connect* __conn

    def __cinit__(self, dsn):
        self.__conn = &dbtransfer.connect(dsn.encode())

    def insert(self):
        dbtransfer.insert(<otl_connect&>self.__conn[0])

    def select(self, n):
        dbtransfer.select(<otl_connect&>self.__conn[0], 10)

    def __dealloc__(self):
        if self.__conn is not NULL:
            print('deallocate the wrapped otl_connect pointer...')
            del self.__conn
