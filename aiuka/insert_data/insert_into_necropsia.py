import dbconnector

con = dbconnector.con
cursor = dbconnector.cursor
# Data insertion


def insert_data(values):
    cursor.execute("insert into necropsia (re, idtemp, idperm, incidente,"
                   " especie, ani_inter , data_obito, ani_exter, "
                   " bo_cpf_rg, cep_tel, local, arm_carcaca, contexto_morte, "
                   " obs_hist, necropsista, data_necropsia, g_et, peso, "
                   " condi_corp, comp_retilineo, petro_ex, petro, condi_carcaca, "
                   " ectoparasitase, obs_exame_ext, traq, "
                   " formol_traq, congel_traq, fotos_traq, saco_ae, formol_saco_ae, "
                   " congel_saco_ae, fotos_saco_ae,"
                   " pulmoes, formol_pulmoes, congel_pulmoes, "
                   " fotos_pulmoes, linf, formol_linf, "
                   " congel_linf, fotos_linf,  coracao, "
                   " formol_coracao, congel_coracao, fotos_coracao, baco, formol_baco, "
                   " congel_baco, fotos_baco, pancreas, formol_pancreas, congel_pancreas, "
                   " fotos_pancreas, linf_mese, formol_linf_mese, "
                   " congel_linf_mese, fotos_linf_mese, figado, "
                   " formol_figado, congel_figado, fotos_figado, rins, formol_rins, "
                   " congel_rins, fotos_rins, repro, formol_repro, congel_repro, "
                   " fotos_repro, adrenais, formol_adrenais, "
                   " congel_adrenais, fotos_adrenais, esofago, "
                   " formol_esofago, congel_esofago, fotos_esofago, estomago,"
                   " formol_estomago, congel_estomago, fotos_estomago, intestino_del, "
                   " formol_intestino_del, congel_intestino_del, fotos_intestino_del, "
                   " intestino_grosso, formol_intestino_grosso, congel_intestino_grosso, "
                   " fotos_intestino_grosso, pele, formol_pele, congel_pele, "
                   " fotos_pele,  musculos, formol_musculos, congel_musculos, fotos_musculos,"
                   " gordura, formol_gordura, congel_gordura, fotos_gordura,"
                   " tireoides, formol_tireoides, congel_tireoides,"
                   " fotos_tireoides, bursa, formol_bursa, "
                   " congel_bursa, fotos_bursa, encefalo, "
                   " formol_encefalo, congel_encefalo, fotos_encefalo, lingua, formol_lingua, "
                   " congel_lingua, fotos_lingua, cloaca, formol_cloaca, congel_cloaca, "
                   " fotos_cloaca, glan_supra, "
                   " formol_glan_supra, congel_glan_supra, fotos_glan_supra, "
                   " glan_uro, formol_glan_uro, congel_glan_uro, "
                   " fotos_glan_uro, bico_dentes, "
                   " formol_bico_dentes, congel_bico_dentes, fotos_bico_dentes, diag_pre,"
                   " sexo, file_ext, file_int, file_bio, pena_alu, obs_conclusao, "
                   " achados_necropsia, nome_pop) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (values['re'], values['idtemp'], values['idperm'], values['incidente'], values['especie'],
                    values['ani_inter'], values['data_obito'], values['ani_exter'], values['bo_cpf_rg'],
                    values['cep_tel'], values['local'], values['arm_carcaca'], values['contexto_morte'], values['obs_hist'],
                    values['necropsista'], values['data_necropsia'], values['g_et'], values['peso'], values['condi_corp'],
                    values['comp_retilineo'], values['petro_ex'], values['petro'], values['condi_carcaca'],
                    values['ectoparasitase'], values['obs_exame_ext'], values['traq'],
                    values['formol_traq'], values['congel_traq'], values['fotos_traq'], values['saco_ae'], values['formol_saco_ae'], values['congel_saco_ae'], values['fotos_saco_ae'],
                    values['pulmoes'], values['formol_pulmoes'], values['congel_pulmoes'],
                    values['fotos_pulmoes'], values['linf'], values['formol_linf'],
                    values['congel_linf'], values['fotos_linf'], values['coracao'],
                    values['formol_coracao'], values['congel_coracao'], values['fotos_coracao'],
                    values['baco'], values['formol_baco'], values['congel_baco'], values['fotos_baco'],
                    values['pancreas'], values['formol_pancreas'], values['congel_pancreas'],
                    values['fotos_pancreas'], values['linf_mese'], values['formol_linf_mese'],
                    values['congel_linf_mese'], values['fotos_linf_mese'], values['figado'],
                    values['formol_figado'], values['congel_figado'], values['fotos_figado'],
                    values['rins'], values['formol_rins'], values['congel_rins'], values['fotos_rins'],
                    values['repro'], values['formol_repro'], values['congel_repro'],
                    values['fotos_repro'], values['adrenais'], values['formol_adrenais'],
                    values['congel_adrenais'], values['fotos_adrenais'], values['esofago'],
                    values['formol_esofago'], values['congel_esofago'], values['fotos_esofago'],
                    values['estomago'], values['formol_estomago'], values['congel_estomago'], values['fotos_estomago'],
                    values['intestino_del'], values['formol_intestino_del'],
                    values['congel_intestino_del'], values['fotos_intestino_del'],
                    values['intestino_grosso'], values['formol_intestino_grosso'], values['congel_intestino_grosso'],
                    values['fotos_intestino_grosso'], values['pele'], values['formol_pele'],
                    values['congel_pele'], values['fotos_pele'],  values['musculos'],
                    values['formol_musculos'], values['congel_musculos'], values['fotos_musculos'],
                    values['gordura'], values['formol_gordura'], values['congel_gordura'], values['fotos_gordura'],
                    values['tireoides'], values['formol_tireoides'], values['congel_tireoides'], values['fotos_tireoides'],
                    values['bursa'], values['formol_bursa'], values['congel_bursa'],
                    values['fotos_bursa'], values['encefalo'], values['formol_encefalo'], values['congel_encefalo'],
                    values['fotos_encefalo'],values['lingua'], values['formol_lingua'],
                    values['congel_lingua'], values['fotos_lingua'], values['cloaca'], values['formol_cloaca'], values['congel_cloaca'],
                    values['fotos_cloaca'], values['glan_supra'],
                    values['formol_glan_supra'], values['congel_glan_supra'], values['fotos_glan_supra'],
                    values['glan_uro'], values['formol_glan_uro'],
                    values['congel_glan_uro'], values['fotos_glan_uro'],
                    values['bico_dentes'],values['formol_bico_dentes'], values['congel_bico_dentes'],
                    values['fotos_bico_dentes'], values['diag_pre'], values['sexo'], values['file_ext'],
                    values['file_int'], values['file_bio'], values['pena_alu'], values['obs_conclusao'],
                    values['achados_necropsia'], values['nome_pop']))
    con.commit()

