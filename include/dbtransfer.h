#pragma once
#include "stdafx.h"

namespace dbtransfer {
    odbc::otl_connect& connect(const char* dsn);
    void select(odbc::otl_connect& db, const int af1);
    void insert(odbc::otl_connect& db);
    void update(odbc::otl_connect& db, const int af1);
}
