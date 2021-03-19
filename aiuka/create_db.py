import dbconnector
# GET CURSOR
cursor = dbconnector.cursor


# CREATE TABLE
def create_db():
    cursor.execute("CREATE SCHEMA `aiuka` ")

create_db()