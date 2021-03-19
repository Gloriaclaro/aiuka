import sys
sys.path.insert(1, 'C:/Users/Mult-e/PycharmProjects/aiuka')

import dbconnector

con = dbconnector.con
cursor = dbconnector.cursor
# Data insertion
def insert_data(values):
    cursor.execute("insert into reabilitacao_tp (re, data_tp1, data_tp2, data_tp3, data_tp4, data_tp5, data_tp6,"
                   " data_tp7, data_tp8, data_tp9, data_tp10, data_tp11, data_tp12,"
                   " data_tp13, data_tp14, data_tp15, data_tp16, data_tp17, data_tp18,"
                   " data_tp19, data_tp20, data_tp21, peso_tp1, peso_tp2, peso_tp3,"
                   " peso_tp4, peso_tp5, peso_tp6, peso_tp7, peso_tp8, peso_tp9,"
                   " peso_tp10, peso_tp11, peso_tp12, peso_tp13, peso_tp14, peso_tp15,"
                   " peso_tp16, peso_tp17, peso_tp18, peso_tp19, peso_tp20, peso_tp21,"
                   " temp_tp1, temp_tp2, temp_tp3, temp_tp4, temp_tp5, temp_tp6,"
                   " temp_tp7, temp_tp8, temp_tp9, temp_tp10, temp_tp11, temp_tp12,"
                   " temp_tp13, temp_tp14, temp_tp15, temp_tp16, temp_tp17, temp_tp18,"
                   " temp_tp19, temp_tp20, temp_tp21, mhidra_tp1, mhidra_tp2, mhidra_tp3,"
                   " mhidra_tp4, mhidra_tp5, mhidra_tp6, mhidra_tp7, mhidra_tp8, mhidra_tp9,"
                   " mhidra_tp10, mhidra_tp11, mhidra_tp12, mhidra_tp13, mhidra_tp14, mhidra_tp15,"
                   " mhidra_tp16, mhidra_tp17, mhidra_tp18, mhidra_tp19, mhidra_tp20, mhidra_tp21,"
                   " thidra_tp1, thidra_tp2, thidra_tp3, thidra_tp4, thidra_tp5, thidra_tp6,"
                   " thidra_tp7, thidra_tp8, thidra_tp9, thidra_tp10, thidra_tp11, thidra_tp12,"
                   " thidra_tp13, thidra_tp14, thidra_tp15, thidra_tp16, thidra_tp17, thidra_tp18,"
                   " thidra_tp19, thidra_tp20, thidra_tp21, mali_tp1, mali_tp2, mali_tp3,"
                   " mali_tp4, mali_tp5, mali_tp6, mali_tp7, mali_tp8, mali_tp9, mali_tp10,"
                   " mali_tp11, mali_tp12, mali_tp13, mali_tp14, mali_tp15, mali_tp16, mali_tp17,"
                   " mali_tp18, mali_tp19, mali_tp20, mali_tp21, tali_tp1, tali_tp2, tali_tp3,"
                   " tali_tp4, tali_tp5, tali_tp6, tali_tp7, tali_tp8, tali_tp9, tali_tp10,"
                   " tali_tp11, tali_tp12, tali_tp13, tali_tp14, tali_tp15, tali_tp16, tali_tp17,"
                   " tali_tp18, tali_tp19, tali_tp20, tali_tp21, mmed_tp1, mmed_tp2, mmed_tp3,"
                   " mmed_tp4, mmed_tp5, mmed_tp6, mmed_tp7, mmed_tp8, mmed_tp9, mmed_tp10,"
                   " mmed_tp11, mmed_tp12, mmed_tp13, mmed_tp14, mmed_tp15, mmed_tp16, mmed_tp17,"
                   " mmed_tp18, mmed_tp19, mmed_tp20, mmed_tp21, tmed_tp1, tmed_tp2, tmed_tp3,"
                   " tmed_tp4, tmed_tp5, tmed_tp6, tmed_tp7, tmed_tp8, tmed_tp9, tmed_tp10,"
                   " tmed_tp11, tmed_tp12, tmed_tp13, tmed_tp14, tmed_tp15, tmed_tp16, tmed_tp17,"
                   " tmed_tp18, tmed_tp19, tmed_tp20, tmed_tp21, obs_tp, acompanhamento) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                   "%s,%s,%s,%s,%s,%s,%s)",
                   (values['re'],values['data_tp1'], values['data_tp2'], values['data_tp3'], values['data_tp4'],
                    values['data_tp5'], values['data_tp6'],values['data_tp7'], values['data_tp8'],
                    values['data_tp9'], values['data_tp10'], values['data_tp11'], values['data_tp12'],
                    values['data_tp13'], values['data_tp14'], values['data_tp15'], values['data_tp16'],
                    values['data_tp17'], values['data_tp18'],values['data_tp19'], values['data_tp20'],
                    values['data_tp21'], values['peso_tp1'], values['peso_tp2'], values['peso_tp3'],
                    values['peso_tp4'], values['peso_tp5'], values['peso_tp6'], values['peso_tp7'],
                    values['peso_tp8'], values['peso_tp9'], values['peso_tp10'],values['peso_tp11'],
                    values['peso_tp12'], values['peso_tp13'], values['peso_tp14'], values['peso_tp15'],
                    values['peso_tp16'], values['peso_tp17'], values['peso_tp18'], values['peso_tp19'],
                    values['peso_tp20'], values['peso_tp21'],values['temp_tp1'], values['temp_tp2'],
                    values['temp_tp3'], values['temp_tp4'], values['temp_tp5'], values['temp_tp6'],
                    values['temp_tp7'], values['temp_tp8'], values['temp_tp9'], values['temp_tp10'],
                    values['temp_tp11'], values['temp_tp12'],values['temp_tp13'], values['temp_tp14'],
                    values['temp_tp15'],values['temp_tp16'], values['temp_tp17'], values['temp_tp18'],
                    values['temp_tp19'], values['temp_tp20'], values['temp_tp21'], values['mhidra_tp1'],
                    values['mhidra_tp2'], values['mhidra_tp3'],values['mhidra_tp4'], values['mhidra_tp5'],
                    values['mhidra_tp6'], values['mhidra_tp7'], values['mhidra_tp8'], values['mhidra_tp9'],
                    values['mhidra_tp10'], values['mhidra_tp11'], values['mhidra_tp12'], values['mhidra_tp13'],
                    values['mhidra_tp14'], values['mhidra_tp15'],values['mhidra_tp16'], values['mhidra_tp17'],
                    values['mhidra_tp18'], values['mhidra_tp19'], values['mhidra_tp20'], values['mhidra_tp21'],
                    values['thidra_tp1'], values['thidra_tp2'], values['thidra_tp3'], values['thidra_tp4'],
                    values['thidra_tp5'], values['thidra_tp6'],values['thidra_tp7'], values['thidra_tp8'],
                    values['thidra_tp9'], values['thidra_tp10'], values['thidra_tp11'], values['thidra_tp12'],
                    values['thidra_tp13'], values['thidra_tp14'], values['thidra_tp15'], values['thidra_tp16'],
                    values['thidra_tp17'], values['thidra_tp18'],values['thidra_tp19'],values['thidra_tp20'],
                    values['thidra_tp21'], values['mali_tp1'], values['mali_tp2'], values['mali_tp3'],values['mali_tp4'],
                    values['mali_tp5'], values['mali_tp6'], values['mali_tp7'], values['mali_tp8'], values['mali_tp9'],
                    values['mali_tp10'],values['mali_tp11'], values['mali_tp12'], values['mali_tp13'], values['mali_tp14'],
                    values['mali_tp15'], values['mali_tp16'], values['mali_tp17'],values['mali_tp18'], values['mali_tp19'],
                    values['mali_tp20'], values['mali_tp21'], values['tali_tp1'], values['tali_tp2'],values['tali_tp3'],
                    values['tali_tp4'], values['tali_tp5'], values['tali_tp6'], values['tali_tp7'], values['tali_tp8'],
                    values['tali_tp9'], values['tali_tp10'],values['tali_tp11'], values['tali_tp12'], values['tali_tp13'],
                    values['tali_tp14'], values['tali_tp15'], values['tali_tp16'], values['tali_tp17'],values['tali_tp18'],
                    values['tali_tp19'], values['tali_tp20'], values['tali_tp21'], values['mmed_tp1'], values['mmed_tp2'],
                    values['mmed_tp3'],values['mmed_tp4'], values['mmed_tp5'], values['mmed_tp6'], values['mmed_tp7'],
                    values['mmed_tp8'], values['mmed_tp9'], values['mmed_tp10'],values['mmed_tp11'], values['mmed_tp12'],
                    values['mmed_tp13'], values['mmed_tp14'], values['mmed_tp15'], values['mmed_tp16'], values['mmed_tp17'],
                    values['mmed_tp18'], values['mmed_tp19'], values['mmed_tp20'], values['mmed_tp21'], values['tmed_tp1'],
                    values['tmed_tp2'], values['tmed_tp3'],values['tmed_tp4'], values['tmed_tp5'], values['tmed_tp6'],
                    values['tmed_tp7'], values['tmed_tp8'], values['tmed_tp9'], values['tmed_tp10'],values['tmed_tp11'],
                    values['tmed_tp12'], values['tmed_tp13'], values['tmed_tp14'], values['tmed_tp15'], values['tmed_tp16'],
                    values['tmed_tp17'], values['tmed_tp18'], values['tmed_tp19'], values['tmed_tp20'], values['tmed_tp21'],
                    values['obs_tp'], values['acompanhamento']))
    con.commit()

