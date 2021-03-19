import sys
sys.path.insert(1, 'C:/Users/Mult-e/PycharmProjects/aiuka')
import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor
# Data insertion
def select_data(re):
    cursor.execute(f"select * from reabilitacao_tp where re='{re}'")
    values = []
    for row in cursor:
        for el in row:
            values.append(el)
    values.pop(0)
    return values


