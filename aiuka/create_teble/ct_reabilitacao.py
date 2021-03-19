import sys
sys.path.insert(1, 'C:/Users/Mult-e/PycharmProjects/aiuka')

import dbconnector

# GET CURSOR
cursor = dbconnector.cursor


# CREATE TABLE
def create_table():
    cursor.execute("CREATE TABLE reabilitacao (id INT AUTO_INCREMENT PRIMARY KEY, re text NOT NULL,"
                   " idtemp text NOT NULL, idperm text NOT NULL, incidente text NOT NULL,"
                   " especie text NOT NULL, local text NOT NULL, resp text NOT NULL,"
                   " date_time text NOT NULL, hidratacao_vo text, hidratacao_sc text, "
                   " aquecimento text, estabilização_outro text, historico text NOT NULL,"
                   " num_bo text, nome_entrega text, cpf_rg text, cep_tel text,"
                   " peso text NOT NULL, freq_resp text, freq_card text, "
                   " temp text NOT NULL, hematocrio text, PPT text, glicose text,"
                   " grupo_etario text NOT NULL, sexo text, condicao_corporal text NOT NULL,"
                   " desidratacao text NOT NULL, atitude text NOT NULL, auscultacao text,"
                   " petrolizacao_extensao text, petrolizacao_profundidade text,"
                   " doc_ad_path text NOT NULL, resp_admissao text NOT NULL, "
                   " date_time_admissao text NOT NULL, cabeca_narinas_boca text, "
                   " olhos_ouvido text, fezes_cloaca_anus text,"
                   " asas_nadadeiras_patas text, pele text, palpacao_abdominal text,"
                   " obs_admissao text NOT NULL, med1 text, med2 text, med3 text,"
                   " med4 text, med5 text, dose1 text, dose2 text, dose3 text,"
                   " dose4 text, dose5 text, via1 text, via2 text, via3 text,"
                   " via4 text, via5 text, freq1 text, freq2 text, freq3 text,"
                   " freq4 text, freq5 text, data_init1 text, data_init2 text,"
                   " data_init3 text, data_init4 text, data_init5 text,  "
                   " data_term1 text, data_term2 text, data_term3 text,"
                   " data_term4 text, data_term5 text, volume1 text, volume2 text,"
                   " volume3 text, volume4 text, volume5 text, obs_tra1 text,"
                   " obs_tra2 text, obs_tra3 text, obs_tra4 text, obs_tra5 text,"
                   " hidratacao_oral text, hidratacao_sub text, ali_pas text, "
                   " ali_sol_forcada text, ali_sol_livre text, lavagem text, "
                   " piscina_ad text, piscina_as text, muda_plu text, "
                   " obs_reab text, lib text, dest_local text, "
                   " resp_dest text NOT NULL, date_time_dest text NOT NULL, obito text, "
                   " dignostico text, foto_doc_path text, nome_pop text,"
                   " ficha_biometria_path text, eutanasia text, justificativa text, transferencia text, "
                   " destino text, data_hidra_init text, data_hidra_ter text, obs_hidra text,"
                   " data_hidrasub_init text, data_hidrasub_ter text, obs_hidrasub text, data_alipas_init text,"
                   " data_alipas_ter text, obs_alipas text, data_alifor_init text, data_alifor_ter text,"
                   " obs_alifor text, data_alisl_init text, data_alisl_ter text, obs_alisl text, data_lavag_init text, "
                   " data_lavag_ter text, obs_lavag text, data_piscad_init text, data_piscad_ter text, obs_piscad text,"
                   " data_piscas_init text,  data_piscas_ter text, obs_piscas text, data_mdplu_init text, "
                   " data_mdplu_ter text)")

