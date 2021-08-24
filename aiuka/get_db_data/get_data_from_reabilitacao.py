import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor


# Data insertion
def select_data(re):
    cursor.execute(f"select * from reabilitacao where re='{re}'")
    values = []
    for row in cursor:
        for el in row:
            values.append(el)
    values.pop(0)
    return values


def select_data(re):
    cursor.execute(f"select * from reabilitacao")
    values = []
    for row in cursor:
        for el in row:
            values.append(el)
    values.pop(0)
    return values

