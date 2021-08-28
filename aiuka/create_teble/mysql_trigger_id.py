import dbconnector
con = dbconnector.con
cursor = dbconnector.cursor


def trigger_reabilitacao():
    cursor.execute("""  CREATE TRIGGER trigger1
                        BEFORE INSERT
                        ON reabilitacao
                        FOR EACH ROW
                        BEGIN
                        SET @lastID = (SELECT id FROM reabilitacao ORDER BY id DESC LIMIT 1);
                        IF @lastID IS NULL OR @lastID = '' THEN
                            SET @lastID = 0;
                        END IF;
                        SET @lastID = @lastID +1;
                        SET NEW.re = CONCAT(@lastID, NEW.re);
                        END""")


def trigger_reabilitacao_sp():
    cursor.execute("""  CREATE TRIGGER trigger2
                        BEFORE INSERT
                        ON reabilitacao_sp
                        FOR EACH ROW
                        BEGIN
                        SET @lastID = (SELECT id FROM reabilitacao_sp ORDER BY id DESC LIMIT 1);
                        IF @lastID IS NULL OR @lastID = '' THEN
                            SET @lastID = 0;
                        END IF;
                        SET @lastID = @lastID +1;
                        SET NEW.re = CONCAT(@lastID, NEW.re);
                        END""")


def trigger_reabilitacao_tp():
    cursor.execute("""  CREATE TRIGGER trigger3
                        BEFORE INSERT
                        ON reabilitacao_tp
                        FOR EACH ROW
                        BEGIN
                        SET @lastID = (SELECT id FROM reabilitacao_tp ORDER BY id DESC LIMIT 1);
                        IF @lastID IS NULL OR @lastID = '' THEN
                            SET @lastID = 0;
                        END IF;
                        SET @lastID = @lastID +1;
                        SET NEW.re = CONCAT(@lastID, NEW.re);
                        END""")


def trigger_necropsia():
    cursor.execute("""  CREATE TRIGGER trigger4
                        BEFORE INSERT
                        ON necropsia
                        FOR EACH ROW
                        BEGIN
                        SET @lastID = (SELECT id FROM necropsia ORDER BY id DESC LIMIT 1);
                        IF @lastID IS NULL OR @lastID = '' THEN
                            SET @lastID = 0;
                        END IF;
                        SET @lastID = @lastID +1;
                        SET NEW.re = CONCAT(@lastID, NEW.re);
                        END""")
