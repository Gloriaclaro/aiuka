import dbconnector

# GET CURSOR
cursor = dbconnector.cursor


# CREATE TABLE
def create_table():
    cursor.execute("CREATE TABLE login (id INT AUTO_INCREMENT PRIMARY KEY, user text NOT NULL, "
                   "senha text NOT NULL, base text NOT NULL, email text NOT NULL)")

