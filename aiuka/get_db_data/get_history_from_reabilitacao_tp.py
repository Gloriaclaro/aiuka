import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor


def select_data():
    cursor.execute(f"select * from reabilitacao_sp")
    values = []
    for row in cursor:
        for el in row:
            values.append(el)
    values.pop(0)
    return values