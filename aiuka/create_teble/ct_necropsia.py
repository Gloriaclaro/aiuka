import sys
sys.path.insert(1, 'C:/Users/Mult-e/PycharmProjects/aiuka')

import dbconnector

# GET CURSOR
cursor = dbconnector.cursor


# CREATE TABLE
def create_table():
    cursor.execute("CREATE TABLE necropsia (id INT AUTO_INCREMENT PRIMARY KEY, re text NOT NULL,"
                   " idtemp text NOT NULL, idperm text NOT NULL, incidente text NOT NULL,"
                   " especie text NOT NULL, ani_inter text , data_obito text, ani_exter text, "
                   " bo_cpf_rg text, cep_tel text, local text, arm_carcaca text, contexto_morte text, "
                   " obs_hist text, necropsista text, data_necropsia text, g_et text, peso text, "
                   " condi_corp text, comp_retilineo text, petro_ex text, petro text, condi_carcaca text, "
                   " ectoparasitase text, obs_exame_ext text, traq text, "
                   " formol_traq text, congel_traq text, fotos_traq text, saco_ae text, formol_saco_ae text, "
                   " congel_saco_ae text, fotos_saco_ae text,"
                   " pulmoes text, formol_pulmoes text, congel_pulmoes text, "
                   " fotos_pulmoes text, linf text, formol_linf text, "
                   " congel_linf text, fotos_linf text,  coracao text, "
                   " formol_coracao text, congel_coracao text, fotos_coracao text, baco text, formol_baco text, "
                   " congel_baco text, fotos_baco text, pancreas text, formol_pancreas text, congel_pancreas text, "
                   " fotos_pancreas text, linf_mese text, formol_linf_mese text, "
                   " congel_linf_mese text, fotos_linf_mese text, figado text, "
                   " formol_figado text, congel_figado text, fotos_figado text, rins text, formol_rins text, "
                   " congel_rins text, fotos_rins text, repro text, formol_repro text, congel_repro text, "
                   " fotos_repro text, adrenais text, formol_adrenais text, "
                   " congel_adrenais text, fotos_adrenais text, esofago text, "
                   " formol_esofago text, congel_esofago text, fotos_esofago text, estomago text,"
                   " formol_estomago text, congel_estomago text, fotos_estomago text, intestino_del text, "
                   " formol_intestino_del text, congel_intestino_del text, fotos_intestino_del text, "
                   " intestino_grosso text, formol_intestino_grosso text, congel_intestino_grosso text, "
                   " fotos_intestino_grosso text, pele text, formol_pele text, congel_pele text, "
                   " fotos_pele text,  musculos text, formol_musculos text, congel_musculos text, fotos_musculos text,"
                   " gordura text, formol_gordura text, congel_gordura text, fotos_gordura text,"
                   " tireoides text, formol_tireoides text, congel_tireoides text,"
                   " fotos_tireoides text, bursa text, formol_bursa text, "
                   " congel_bursa text, fotos_bursa text, encefalo text, "
                   " formol_encefalo text, congel_encefalo text, fotos_encefalo text, lingua text, formol_lingua text, "
                   " congel_lingua text, fotos_lingua text, cloaca text, formol_cloaca text, congel_cloaca text, "
                   " fotos_cloaca text, glan_supra text, "
                   " formol_glan_supra text, congel_glan_supra text, fotos_glan_supra text, "
                   " glan_uro text, formol_glan_uro text, congel_glan_uro text, "
                   " fotos_glan_uro text, bico_dentes text, "
                   " formol_bico_dentes text, congel_bico_dentes text, fotos_bico_dentes text, diag_pre text,"
                   " sexo text, file_ext text, file_int text, file_bio text, pena_alu text, obs_conclusao text, "
                   " achados_necropsia text, nome_pop text)")

