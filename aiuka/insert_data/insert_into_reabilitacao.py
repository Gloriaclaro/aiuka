import dbconnector

con = dbconnector.con
cursor = dbconnector.cursor
# Data insertion

def insert_data(values):
    cursor.execute("insert into reabilitacao (re, idtemp, idperm, incidente, especie, local, resp, date_time,"
                   " re_comple, tipo_idtemp, tipo_idperm, tipo_incidente, classe, "
                   " hidratacao_vo, hidratacao_sc, aquecimento, estabilização_outro, historico, num_bo,"
                   " nome_entrega, cpf_rg, cep_tel, peso, freq_resp, freq_card, temp, hematocrio, PPT, glicose,"
                   " grupo_etario, sexo, condicao_corporal, desidratacao, atitude, auscultacao,"
                   " petrolizacao_extensao, petrolizacao_profundidade, doc_ad_path, resp_admissao, "
                   " date_time_admissao, cabeca_narinas_boca, olhos_ouvido, fezes_cloaca_anus,"
                   " asas_nadadeiras_patas, pele, palpacao_abdominal, obs_admissao, med1, med2, med3, med4, med5, "
                   " dose1, dose2, dose3, dose4, dose5, via1, via2, via3, via4, via5, freq1, freq2, freq3, freq4, "
                   " freq5, data_init1, data_init2, data_init3, data_init4, data_init5, data_term1, data_term2, "
                   " data_term3, data_term4, data_term5, volume1, volume2, volume3, volume4, volume5, obs_tra1,"
                   " obs_tra2, obs_tra3, obs_tra4, obs_tra5, hidratacao_oral, hidratacao_sub, ali_pas, "
                   " ali_sol_forcada, ali_sol_livre, lavagem, piscina_ad, piscina_as, muda_plu, obs_reab, lib, "
                   " dest_local, resp_dest, date_time_dest, obito, dignostico, foto_doc_path, nome_pop,"
                   " ficha_biometria_path, eutanasia, justificativa, transferencia, destino,  data_hidra_init,"
                   " data_hidra_ter, obs_hidra, data_hidrasub_init, data_hidrasub_ter, obs_hidrasub, data_alipas_init,"
                   " data_alipas_ter, obs_alipas, data_alifor_init, data_alifor_ter,"
                   " obs_alifor, data_alisl_init, data_alisl_ter, obs_alisl, data_lavag_init, "
                   " data_lavag_ter, obs_lavag, data_piscad_init, data_piscad_ter, obs_piscad,"
                   " data_piscas_init,  data_piscas_ter, obs_piscas, data_mdplu_init, "
                   " data_mdplu_ter)"
                   " values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   " %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   " %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   " %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   " %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )",
                   (values['re'], values['idtemp'], values['idperm'], values['incidente'], values['especie'],
                    values['local'], values['resp'], values['time'], values['re_comple'], values['tipo_idtemp'],
                    values['tipo_idperm'], values['tipo_incidente'], values['classe'], values['hidratacao_vo'],
                    values['hidratacao_sc'], values['aquecimento'], values['est_outro'], values['historico'], values['num_bo'], values['nome_entrega'],
                    values['cpf_rg'], values['cep_tel'], values['peso'], values['freq_resp'], values['freq_card'],
                    values['temp'], values['hema'], values['ppt'], values['glic'], values['g_et'],
                    values['sexo'], values['condi_corp'], values['desidra'], values['att'], values['auscul'],
                    values['petro_ex'], values['petro'], values['doc_ad'], values['resp_ad'], values['time_ad'],
                    values['cab_na_bo'], values['olhos_ouv'], values['fezes'], values['pes'], values['pele'],
                    values['palp_abd'], values['obs_ad'], values['med1'], values['med2'], values['med3'],
                    values['med4'], values['med5'], values['dose1'], values['dose2'], values['dose3'],
                    values['dose4'], values['dose5'], values['via1'], values['via2'], values['via3'],
                    values['via4'], values['via5'], values['freq1'], values['freq2'], values['freq3'],
                    values['freq4'], values['freq5'], values['data_init1'], values['data_init2'], values['data_init3'],
                    values['data_init4'], values['data_init5'], values['data_term1'], values['data_term2'], values['data_term3'],
                    values['data_term4'], values['data_term5'], values['volume1'], values['volume2'], values['volume3'],
                    values['volume4'], values['volume5'], values['obs_tra1'], values['obs_tra2'], values['obs_tra3'],
                    values['obs_tra4'], values['obs_tra5'], values['hidra_oral'], values['hidra_sub'], values['ali_pas'],
                    values['ali_for'], values['ali_sl'], values['lavag'], values['pisc_ad'], values['pisc_as'],
                    values['md_plu'], values['obs_reab'], values['lib'], values['local_dest'], values['resp_dest'],
                    values['time_dest'], values['obito'], values['pre_diag'], values['foto_doc_dest'], values['nome_pop'],
                    values['file_bio'], values['eutanasia'], values['justif'], values['transf'], values['dest'],
                    values['data_hidra_init'], values['data_hidra_ter'], values['obs_hidra'], values['data_hidrasub_init'],
                    values['data_hidrasub_ter'], values['obs_hidrasub'], values['data_alipas_init'],
                    values['data_alipas_ter'], values['obs_alipas'], values['data_alifor_init'], values['data_alifor_ter'],
                    values['obs_alifor'], values['data_alisl_init'], values['data_alisl_ter'], values['obs_alisl'],
                    values['data_lavag_init'], values['data_lavag_ter'], values['obs_lavag'], values['data_piscad_init'],
                    values['data_piscad_ter'], values['obs_piscad'], values['data_piscas_init'],  values['data_piscas_ter'],
                    values['obs_piscas'], values['data_mdplu_init'], values['data_mdplu_ter']))
    con.commit()
