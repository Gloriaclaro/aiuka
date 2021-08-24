import dbconnector

# GET CURSOR
cursor = dbconnector.cursor


# CREATE TABLE
def create_table():
    cursor.execute("CREATE TABLE reabilitacao_sp (id INT AUTO_INCREMENT PRIMARY KEY, re text NOT NULL,"
                   " data_sp1 text, data_sp2 text, data_sp3 text, data_sp4 text, data_sp5 text,"
                   " data_sp6 text, data_sp7 text, data_sp8 text, peso_sp1 text, peso_sp2 text,"
                   " peso_sp3 text, peso_sp4 text, peso_sp5 text, peso_sp6 text, peso_sp7 text,"
                   " peso_sp8 text, condi_corp_sp1 text, condi_corp_sp2 text, condi_corp_sp3 text,"
                   " condi_corp_sp4 text, condi_corp_sp5 text, condi_corp_sp6 text,condi_corp_sp7 text, "
                   " condi_corp_sp8 text, temp_sp1 text, temp_sp2 text, temp_sp3 text, temp_sp4 text,"
                   " temp_sp5 text, temp_sp6 text, temp_sp7 text, temp_sp8 text, pcv_sp1 text, pcv_sp2 text,"
                   " pcv_sp3 text, pcv_sp4 text, pcv_sp5 text, pcv_sp6 text, pcv_sp7 text, pcv_sp8 text,"
                   " bcos_sp1 text, bcos_sp2 text, bcos_sp3 text, bcos_sp4 text, bcos_sp5 text, bcos_sp6 text,"
                   " bcos_sp7 text, bcos_sp8 text, ppt_sp1 text, ppt_sp2 text, ppt_sp3 text, ppt_sp4 text,"
                   " ppt_sp5 text, ppt_sp6 text, ppt_sp7 text, ppt_sp8 text, resp_sp1 text, resp_sp2 text,"
                   " resp_sp3 text, resp_sp4 text, resp_sp5 text, resp_sp6 text, resp_sp7 text, resp_sp8 text,"
                   " obs_sp text, exad_sp text)")


# ADD COLUMN
def add_new_column():
    cursor.execute("ALTER TABLE reabilitacao_sp ADD COLUMN destino text")

