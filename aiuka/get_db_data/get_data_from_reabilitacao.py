import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor


def select_data(re):
    cursor.execute(f"select * from reabilitacao where re='{re}'")
    values = []
    for row in cursor:
        for el in row:
            values.append(el)
    values.pop(0)
    return values



