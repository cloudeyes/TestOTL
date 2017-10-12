cdef extern from "dbtransfer.h" namespace "dbtransfer":
    cdef extern from "otlv4.h" namespace "odbc":
        cdef cppclass otl_connect:
            pass
    cdef otl_connect& connect(const char* dsn)
    cdef void insert(otl_connect& db)
    cdef void select(otl_connect& db, const int n)
