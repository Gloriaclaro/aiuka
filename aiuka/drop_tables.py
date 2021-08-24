import dbconnector
# GET CURSOR
cursor = dbconnector.cursor


# CREATE TABLE
def drop_table():
    cursor.execute("drop table if exists login")
    cursor.execute("drop table if exists necropsia")
    cursor.execute("drop table if exists reabilitacao")
    cursor.execute("drop table if exists reabilitacao_sp")
    cursor.execute("drop table if exists reabilitacao_tp")

drop_table()