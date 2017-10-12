#include "dbtransfer.h"

using namespace dbtransfer;

int main()
{
    odbc::otl_connect& db = dbtransfer::connect("DSN=test.db");

    insert(db); // insert records into the table
    update(db, 10); // update records in the table
    select(db, 8); // select records from the table

    db.logoff(); // disconnect from the database

    return 0;

}
