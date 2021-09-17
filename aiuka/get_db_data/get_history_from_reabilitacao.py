import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor


def select_data():
    cursor.execute(f"select re from reabilitacao")
    values = []
    for row in cursor:
        for el in row:
            values.append(el)
    return values