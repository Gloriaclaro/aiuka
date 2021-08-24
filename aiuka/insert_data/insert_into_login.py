import dbconnector

con = dbconnector.con
cursor = dbconnector.cursor
# Data insertion


def insert_data(values):
    cursor.execute("insert into login (user, senha, base, email ) values ( %s,%s,%s,%s)",
                   (values['nome'], values['senha'], values['base'], values['email']))
    con.commit()

