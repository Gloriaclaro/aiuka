import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor


def trigger_id():
    cursor.execute("""  CREATE TRIGGER trigger1
                        BEFORE INSERT
                        ON reabilitacao
                        FOR EACH ROW
                        BEGIN
                        SET NEW.re = CONCAT(NEW.id, NEW.re);
                        END""")

