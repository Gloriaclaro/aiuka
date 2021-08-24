import dbconnector

# GET CURSOR
cursor = dbconnector.cursor


# CREATE TABLE
def create_table():
    cursor.execute("CREATE TABLE reabilitacao_tp (id INT AUTO_INCREMENT PRIMARY KEY, re text NOT NULL,"
                   " data_tp1 text, data_tp2 text, data_tp3 text, data_tp4 text, data_tp5 text, data_tp6 text,"
                   " data_tp7 text, data_tp8 text, data_tp9 text, data_tp10 text, data_tp11 text, data_tp12 text,"
                   " data_tp13 text, data_tp14 text, data_tp15 text, data_tp16 text, data_tp17 text, data_tp18 text,"
                   " data_tp19 text, data_tp20 text, data_tp21 text, peso_tp1 text, peso_tp2 text, peso_tp3 text,"
                   " peso_tp4 text, peso_tp5 text, peso_tp6 text, peso_tp7 text, peso_tp8 text, peso_tp9 text,"
                   " peso_tp10 text, peso_tp11 text, peso_tp12 text, peso_tp13 text, peso_tp14 text, peso_tp15 text,"
                   " peso_tp16 text, peso_tp17 text, peso_tp18 text, peso_tp19 text, peso_tp20 text, peso_tp21 text,"
                   " temp_tp1 text, temp_tp2 text, temp_tp3 text, temp_tp4 text, temp_tp5 text, temp_tp6 text,"
                   " temp_tp7 text, temp_tp8 text, temp_tp9 text, temp_tp10 text, temp_tp11 text, temp_tp12 text,"
                   " temp_tp13 text, temp_tp14 text, temp_tp15 text, temp_tp16 text, temp_tp17 text, temp_tp18 text,"
                   " temp_tp19 text, temp_tp20 text, temp_tp21 text, mhidra_tp1 text, mhidra_tp2 text, mhidra_tp3 text,"
                   " mhidra_tp4 text, mhidra_tp5 text, mhidra_tp6 text, mhidra_tp7 text, mhidra_tp8 text, mhidra_tp9 text,"
                   " mhidra_tp10 text, mhidra_tp11 text, mhidra_tp12 text, mhidra_tp13 text, mhidra_tp14 text, mhidra_tp15 text,"
                   " mhidra_tp16 text, mhidra_tp17 text, mhidra_tp18 text, mhidra_tp19 text, mhidra_tp20 text, mhidra_tp21 text,"
                   " thidra_tp1 text, thidra_tp2 text, thidra_tp3 text, thidra_tp4 text, thidra_tp5 text, thidra_tp6 text,"
                   " thidra_tp7 text, thidra_tp8 text, thidra_tp9 text, thidra_tp10 text, thidra_tp11 text, thidra_tp12 text,"
                   " thidra_tp13 text, thidra_tp14 text, thidra_tp15 text, thidra_tp16 text, thidra_tp17 text, thidra_tp18 text,"
                   " thidra_tp19 text, thidra_tp20 text, thidra_tp21 text, mali_tp1 text, mali_tp2 text, mali_tp3 text,"
                   " mali_tp4 text, mali_tp5 text, mali_tp6 text, mali_tp7 text, mali_tp8 text, mali_tp9 text, mali_tp10 text,"
                   " mali_tp11 text, mali_tp12 text, mali_tp13 text, mali_tp14 text, mali_tp15 text, mali_tp16 text, mali_tp17 text,"
                   " mali_tp18 text, mali_tp19 text, mali_tp20 text, mali_tp21 text, tali_tp1 text, tali_tp2 text, tali_tp3 text,"
                   " tali_tp4 text, tali_tp5 text, tali_tp6 text, tali_tp7 text, tali_tp8 text, tali_tp9 text, tali_tp10 text,"
                   " tali_tp11 text, tali_tp12 text, tali_tp13 text, tali_tp14 text, tali_tp15 text, tali_tp16 text, tali_tp17 text,"
                   " tali_tp18 text, tali_tp19 text, tali_tp20 text, tali_tp21 text, mmed_tp1 text, mmed_tp2 text, mmed_tp3 text,"
                   " mmed_tp4 text, mmed_tp5 text, mmed_tp6 text, mmed_tp7 text, mmed_tp8 text, mmed_tp9 text, mmed_tp10 text,"
                   " mmed_tp11 text, mmed_tp12 text, mmed_tp13 text, mmed_tp14 text, mmed_tp15 text, mmed_tp16 text, mmed_tp17 text,"
                   " mmed_tp18 text, mmed_tp19 text, mmed_tp20 text, mmed_tp21 text, tmed_tp1 text, tmed_tp2 text, tmed_tp3 text,"
                   " tmed_tp4 text, tmed_tp5 text, tmed_tp6 text, tmed_tp7 text, tmed_tp8 text, tmed_tp9 text, tmed_tp10 text,"
                   " tmed_tp11 text, tmed_tp12 text, tmed_tp13 text, tmed_tp14 text, tmed_tp15 text, tmed_tp16 text, tmed_tp17 text,"
                   " tmed_tp18 text, tmed_tp19 text, tmed_tp20 text, tmed_tp21 text, obs_tp text, acompanhamento text)")


# ADD COLUMN
def add_new_column():
    cursor.execute("ALTER TABLE reabilitacao_tp ADD COLUMN destino text")


