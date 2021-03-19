import mysql.connector

# DATABASE connection
config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'aiuka',
    'charset': 'utf8'
}
con = mysql.connector.connect(**config)
cursor = con.cursor()

