import dbconnector

con = dbconnector.con
cursor = dbconnector.cursor
# Delete data
def delete_data(re):
    cursor.execute(f'delete from reabilitacao_tp where re="{re}"')
    con.commit()

