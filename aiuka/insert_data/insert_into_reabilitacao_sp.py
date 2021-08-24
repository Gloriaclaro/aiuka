import dbconnector

con = dbconnector.con
cursor = dbconnector.cursor
# Data insertion
def insert_data(values):
    cursor.execute("insert into reabilitacao_sp (re, data_sp1, data_sp2, data_sp3, data_sp4, data_sp5,"
                   " data_sp6, data_sp7, data_sp8, peso_sp1, peso_sp2,"
                   " peso_sp3, peso_sp4, peso_sp5, peso_sp6, peso_sp7,"
                   " peso_sp8, condi_corp_sp1, condi_corp_sp2, condi_corp_sp3,"
                   " condi_corp_sp4, condi_corp_sp5, condi_corp_sp6,condi_corp_sp7, "
                   " condi_corp_sp8, temp_sp1, temp_sp2, temp_sp3, temp_sp4,"
                   " temp_sp5, temp_sp6, temp_sp7, temp_sp8, pcv_sp1, pcv_sp2,"
                   " pcv_sp3, pcv_sp4, pcv_sp5, pcv_sp6, pcv_sp7, pcv_sp8,"
                   " bcos_sp1, bcos_sp2, bcos_sp3, bcos_sp4, bcos_sp5, bcos_sp6,"
                   " bcos_sp7, bcos_sp8, ppt_sp1, ppt_sp2, ppt_sp3, ppt_sp4,"
                   " ppt_sp5, ppt_sp6, ppt_sp7, ppt_sp8, resp_sp1, resp_sp2,"
                   " resp_sp3, resp_sp4, resp_sp5, resp_sp6, resp_sp7, resp_sp8,"
                   " obs_sp, exad_sp) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (values['re'],values['data_sp1'], values['data_sp2'], values['data_sp3'], values['data_sp4'],
                    values['data_sp5'],values['data_sp6'], values['data_sp7'], values['data_sp8'], values['peso_sp1'],
                    values['peso_sp2'],values['peso_sp3'], values['peso_sp4'], values['peso_sp5'], values['peso_sp6'],
                    values['peso_sp7'],values['peso_sp8'], values['condi_corp_sp1'], values['condi_corp_sp2'],
                    values['condi_corp_sp3'],values['condi_corp_sp4'], values['condi_corp_sp5'],
                    values['condi_corp_sp6'],values['condi_corp_sp7'],values['condi_corp_sp8'], values['temp_sp1'],
                    values['temp_sp2'], values['temp_sp3'], values['temp_sp4'],values['temp_sp5'], values['temp_sp6'],
                    values['temp_sp7'], values['temp_sp8'], values['pcv_sp1'], values['pcv_sp2'],values['pcv_sp3'],
                    values['pcv_sp4'], values['pcv_sp5'], values['pcv_sp6'], values['pcv_sp7'], values['pcv_sp8'],
                    values['bcos_sp1'], values['bcos_sp2'], values['bcos_sp3'], values['bcos_sp4'], values['bcos_sp5'],
                    values['bcos_sp6'],values['bcos_sp7'], values['bcos_sp8'], values['ppt_sp1'], values['ppt_sp2'],
                    values['ppt_sp3'], values['ppt_sp4'],values['ppt_sp5'], values['ppt_sp6'], values['ppt_sp7'],
                    values['ppt_sp8'], values['resp_sp1'], values['resp_sp2'],values['resp_sp3'], values['resp_sp4'],
                    values['resp_sp5'], values['resp_sp6'], values['resp_sp7'], values['resp_sp8'],values['obs_sp'], values['exad_sp'] ))
    con.commit()

