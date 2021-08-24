import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor


def trigger_id():
    cursor.execute("""  CREATE TRIGGER trigger1
                        BEFORE INSERT
                        ON reabilitacao
                        FOR EACH ROW
                        BEGIN
                        SET @lastID = (SELECT id FROM reabilitacao ORDER BY id DESC LIMIT 1);
                        SET NEW.re = CONCAT(@lastID, NEW.re);
                        END""")

