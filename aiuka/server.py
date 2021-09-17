from flask import Flask, session, redirect, request, render_template
import datetime
import sys
import hashlib
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None


from delete_db_data import delete_from_reabilitacao, delete_from_reabilitacao_sp, delete_from_reabilitacao_tp
from insert_data import insert_into_reabilitacao, insert_into_necropsia, insert_into_reabilitacao_sp,\
    insert_into_reabilitacao_tp, insert_into_login
from get_db_data import get_data_from_reabilitacao, get_data_from_reabilitacao_sp, get_data_from_reabilitacao_tp, \
    get_data_from_necropsia, get_data_from_login, get_history_from_reabilitacao

app = Flask('aiuka')
app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
global logged
logged = False


@app.route('/home', methods=['GET', 'POST'])
def buscar():
    registros = get_history_from_reabilitacao.select_data()
    print(registros)
    if not logged:
        return redirect('/error')
    if request.method == 'POST':
        session['re'] = request.form['re']
        global registro
        registro = request.form['re']
        if 'atualizar' in request.form:
            return redirect('/alterar_reabilitacao')
        elif 'imprimir' in request.form:
            return redirect('/imprimir')
    return render_template('aiuka.html', value=registros, len=len(registros))


@app.route('/', methods=['GET', 'POST'])
def login():
    global logged
    logged = False
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        try:
            data = get_data_from_login.select_data(email)
        except Exception as error:
            logged = False
            return redirect('/error')
        hashed = data[1]
        senha = hashlib.sha512(bytes(senha.encode('utf-8')))
        if senha.hexdigest() == hashed:
            logged = True
            return redirect('/home')
        else:
            return redirect('/error')
    return render_template('login.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    logged = False
    if request.method == 'POST':
        values = {}
        for key in request.form.keys():
            value = str(request.form[f'{key}'])
            value = value.strip()
            values[f'{key}'] = value
            if key == 'senha':
                values[f'{key}'] = hashlib.sha512(bytes(value.encode('utf-8'))).hexdigest()
        insert_into_login.insert_data(values)
        return redirect('/')
    return render_template('register.html')


@app.route('/escolher', methods=['GET', 'POST'])
def escolher():
    if not logged:
        return redirect('/error')
    if request.method == 'POST':
        if 'reabilitacao' in request.form:
            return redirect('/print_reabilitacao')
        elif 'necropsia' in request.form:
            return redirect('/print_necropsia')
    return render_template('escolher.html')


@app.route('/reabilitacao', methods=['GET', 'POST'])
def reab():
    if not logged:
        return redirect('/error')
    if request.method == 'POST':
        year = datetime.date.today().year
        year = f"/{year}"
        values = {'re': year, 'hidratacao_vo': None, 'hidratacao_sc': None, 'aquecimento': None, 'sexo': None,
                  'auscul': None, 'petro_ex': None, 'petro': None, 'cab_na_bo': None, 'olhos_ouv': None, 'fezes': None,
                  'pes': None, 'pele': None, 'palp_abd': None, 'hidra_oral': None, 'hidra_sub': None, 'ali_pas': None,
                  'ali_for': None, 'ali_sl': None, 'lavag': None, 'pisc_ad': None, 'pisc_as': None, 'md_plu': None,
                  'lib': None,'obito': None, 'eutanasia': None, 'transf': None, 'g_et': "", 'condi_corp': "", 'att': "",
                  'desidra': "",'mhidra_tp1': None, 'mhidra_tp2': None, 'mhidra_tp3': None, 'mhidra_tp4': None, 'mhidra_tp5': None,
                  'mhidra_tp6': None, 'mhidra_tp7': None, 'mhidra_tp8': None, 'mhidra_tp9': None, 'mhidra_tp10': None,
                  'mhidra_tp11': None, 'mhidra_tp12': None, 'mhidra_tp13': None, 'mhidra_tp14': None,
                  'mhidra_tp15': None,'mhidra_tp16': None, 'mhidra_tp17': None, 'mhidra_tp18': None, 'mhidra_tp19': None,
                  'mhidra_tp20': None,'mhidra_tp21': None, 'thidra_tp1': None, 'thidra_tp2': None, 'thidra_tp3': None, 'thidra_tp4': None,
                  'thidra_tp5': None,'thidra_tp6': None, 'thidra_tp7': None, 'thidra_tp8': None, 'thidra_tp9': None,
                  'thidra_tp10': None,'thidra_tp11': None, 'thidra_tp12': None, 'thidra_tp13': None,
                  'thidra_tp14': None,'thidra_tp15': None, 'thidra_tp16': None, 'thidra_tp17': None, 'thidra_tp18': None,
                  'thidra_tp19': None,'thidra_tp20': None, 'thidra_tp21': None, 'mali_tp1': None, 'mali_tp2': None, 'mali_tp3': None,
                  'mali_tp4': None, 'mali_tp5': None, 'mali_tp6': None, 'mali_tp7': None, 'mali_tp8': None,
                  'mali_tp9': None,'mali_tp10': None, 'mali_tp11': None, 'mali_tp12': None, 'mali_tp13': None, 'mali_tp14': None,
                  'mali_tp15': None, 'mali_tp16': None, 'mali_tp17': None, 'mali_tp18': None, 'mali_tp19': None,
                  'mali_tp20': None, 'mali_tp21': None, 'tali_tp1': None, 'tali_tp2': None, 'tali_tp3': None,
                  'tali_tp4': None, 'tali_tp5': None, 'tali_tp6': None, 'tali_tp7': None, 'tali_tp8': None,
                  'tali_tp9': None,'tali_tp10': None, 'tali_tp11': None, 'tali_tp12': None, 'tali_tp13': None, 'tali_tp14': None,
                  'tali_tp15': None,'tali_tp16': None, 'tali_tp17': None, 'tali_tp18': None, 'tali_tp19': None, 'tali_tp20': None,
                  'tali_tp21': None,'mmed_tp1': None, 'mmed_tp2': None, 'mmed_tp3': None, 'mmed_tp4': None, 'mmed_tp5': None,
                  'mmed_tp6': None, 'mmed_tp7': None, 'mmed_tp8': None, 'mmed_tp9': None, 'mmed_tp10': None, 'mmed_tp11': None,
                  'mmed_tp12': None,'mmed_tp13': None, 'mmed_tp14': None, 'mmed_tp15': None, 'mmed_tp16': None, 'mmed_tp17': None,
                  'mmed_tp18': None,'mmed_tp19': None, 'mmed_tp20': None, 'mmed_tp21': None, 'tmed_tp1': None, 'tmed_tp2': None,
                  'tmed_tp3': None,'tmed_tp4': None, 'tmed_tp5': None, 'tmed_tp6': None, 'tmed_tp7': None, 'tmed_tp8': None,
                  'tmed_tp9': None, 'tmed_tp10': None, 'tmed_tp11': None, 'tmed_tp12': None, 'tmed_tp13': None, 'tmed_tp14': None,
                  'tmed_tp15': None,'tmed_tp16': None, 'tmed_tp17': None, 'tmed_tp18': None, 'tmed_tp19': None, 'tmed_tp20': None,
                  'tmed_tp21': None
                  }

        for key in request.form.keys():
            value = str(request.form[f'{key}'])
            value = value.strip()
            #value = value.replace("\n", "")
            values[f'{key}'] = value
        insert_into_reabilitacao.insert_data(values)
        insert_into_reabilitacao_sp.insert_data(values)
        insert_into_reabilitacao_tp.insert_data(values)
    return render_template('reabilitacao.html')


@app.route('/necropsia', methods=['GET', 'POST'])
def necro():
    if not logged:
        return redirect('/error')
    if request.method == 'POST':
        values = {'petro_ex': None, 'petro': None,'ectoparasitase': None, 'sexo': None, 'traq': None,
                  'alteracoes_traq': None, 'formol_traq': None, 'congel_traq': None, 'fotos_traq': None, 'saco_ae': None,
                  'normal_saco_ae': None, 'alteracoes_saco_ae': None, 'formol_saco_ae': None, 'congel_saco_ae': None,
                  'fotos_saco_ae': None, 'pulmoes': None, 'normal_pulmoes': None, 'alteracoes_pulmoes': None, 'formol_pulmoes': None,
                  'congel_pulmoes': None, 'fotos_pulmoes': None, 'linf': None,'normal_linf': None, 'alteracoes_linf': None,
                  'formol_linf': None, 'congel_linf': None, 'fotos_linf': None, 'coracao': None, 'normal_coracao': None,
                  'alteracoes_coracao': None, 'formol_coracao': None, 'congel_coracao': None, 'fotos_coracao': None,
                  'normal_baco': None,'baco': None, 'alteracoes_baco': None, 'formol_baco': None, 'congel_baco': None, 'fotos_baco': None,
                  'normal_pancreas': None,'pancreas': None, 'alteracoes_pancreas': None, 'formol_pancreas': None, 'congel_pancreas': None,
                  'fotos_pancreas': None, 'linf_mese': None,'normal_linf_mese': None, 'alteracoes_linf_mese': None, 'formol_linf_mese': None,
                  'congel_linf_mese': None, 'fotos_linf_mese': None, 'normal_figado': None, 'alteracoes_figado': None,
                  'formol_figado': None, 'figado': None, 'congel_figado': None, 'fotos_figado': None, 'normal_rins': None,
                  'alteracoes_rins': None, 'rins': None,'formol_rins': None, 'congel_rins': None, 'fotos_rins': None, 'normal_repro': None,
                  'alteracoes_repro': None, 'repro': None,'formol_repro': None, 'congel_repro': None, 'fotos_repro': None,
                  'normal_adrenais': None, 'adrenais': None,'alteracoes_adrenais': None, 'formol_adrenais': None, 'congel_adrenais': None,
                  'fotos_adrenais': None, 'esofago': None,'normal_esofago': None, 'alteracoes_esofago': None, 'formol_esofago': None,
                  'congel_esofago': None, 'fotos_esofago': None, 'normal_estomago': None, 'alteracoes_estomago': None,
                  'formol_estomago': None, 'estomago': None,'congel_estomago': None, 'fotos_estomago': None, 'normal_intestino_del': None,
                  'alteracoes_intestino_del': None, 'intestino_del': None,'formol_intestino_del': None, 'congel_intestino_del': None,
                  'fotos_intestino_del': None, 'normal_intestino_grosso': None, 'alteracoes_intestino_grosso': None,
                  'formol_intestino_grosso': None, 'congel_intestino_grosso': None, 'fotos_intestino_grosso': None,
                  'pele': None, 'formol_pele': None, 'congel_pele': None,'intestino_grosso': None,
                  'fotos_pele': None, 'musculos': None, 'alteracoes_musculos': None,'pena_alu': None,
                  'formol_musculos': None, 'congel_musculos': None, 'fotos_musculos': None, 'gordura': None,
                  'alteracoes_gordura': None, 'formol_gordura': None, 'congel_gordura': None, 'fotos_gordura': None,
                  'tireoides': None, 'alteracoes_tireoides': None, 'formol_tireoides': None, 'congel_tireoides': None,
                  'fotos_tireoides': None, 'bursa': None, 'formol_bursa': None,
                  'congel_bursa': None, 'fotos_bursa': None, 'encefalo': None, 'alteracoes_encefalo': None,
                  'formol_encefalo': None, 'congel_encefalo': None, 'fotos_encefalo': None, 'lingua': None,
                  'alteracoes_lingua': None, 'formol_lingua': None, 'congel_lingua': None, 'fotos_lingua': None,
                  'cloaca': None, 'alteracoes_cloaca': None, 'formol_cloaca': None, 'congel_cloaca': None,
                  'fotos_cloaca': None, 'glan_supra': None, 'alteracoes_glan_supra': None, 'formol_glan_supra': None,
                  'congel_glan_supra': None, 'fotos_glan_supra': None,'glan_uro': None, 'alteracoes_glan_uro': None,
                  'formol_glan_uro': None, 'congel_glan_uro': None, 'fotos_glan_uro': None, 'bico_dentes': None,
                  'alteracoes_bico_dentes': None, 'formol_bico_dentes': None, 'congel_bico_dentes': None,
                  'fotos_bico_dentes': None}
        for key in request.form.keys():
            value = str(request.form[f'{key}'])
            value = value.strip()
            values[f'{key}'] = value
        insert_into_necropsia.insert_data(values)
    return render_template('necropsia.html')


@app.route('/imprimir', methods=['GET', 'POST'])
def print_form():
    if not logged:
        return redirect('/error')
    try:
        try:
            value_necro = get_data_from_necropsia.select_data(registro)
            Necro = True
        except Exception as err:
            Necro = False
        value = get_data_from_reabilitacao.select_data(registro)
        value_sp = get_data_from_reabilitacao_sp.select_data(registro)
        value_tp = get_data_from_reabilitacao_tp.select_data(registro)
        format_value = []
        format_value_sp = []
        format_value_tp = []
        try:
            for el in value:
                if el is not None:
                    el = el.replace("\n", "<br><br>")
                format_value.append(el)
            for el in value_sp:
                if el is not None:
                    el = el.replace("\n", "<br><br>")
                format_value_sp.append(el)
            for el in value_tp:
                if el is not None:
                    el = el.replace("\n", "<br><br>")
                format_value_tp.append(el)
        except Exception as err:
            pass
        if not Necro:
            return render_template('print_reabilitacao.html', value = format_value, value_sp= format_value_sp,
                               value_tp= format_value_tp)
        else:
            return redirect('/escolher')
    except Exception as err:
        if not Necro:
            return redirect('/error')
        else:
            return redirect('/print_necropsia')


@app.route('/print_reabilitacao', methods=['GET', 'POST'])
def print_reabilitacao():
    if not logged:
        return redirect('/error')
    try:
        value = get_data_from_reabilitacao.select_data(registro)
        value_sp = get_data_from_reabilitacao_sp.select_data(registro)
        value_tp = get_data_from_reabilitacao_tp.select_data(registro)
        format_value = []
        format_value_sp = []
        format_value_tp = []
        try:
            for el in value:
                if el is not None:
                    el = el.replace("\n", "<br><br>")
                format_value.append(el)
            for el in value_sp:
                if el is not None:
                    el = el.replace("\n", "<br><br>")
                format_value_sp.append(el)
            for el in value_tp:
                if el is not None:
                    el = el.replace("\n", "<br><br>")
                format_value_tp.append(el)
            return render_template('print_reabilitacao.html', value=format_value, value_sp=format_value_sp,
                                   value_tp=format_value_tp)
        except Exception as err:
            pass
            return render_template('print_reabilitacao.html', value=value, value_sp=value_sp,
                           value_tp=value_tp)
    except Exception as err:
        return redirect('/error')


@app.route('/print_necropsia', methods=['GET', 'POST'])
def print_necropsia():
    if not logged:
        return redirect('/error')
    try:
        try:
            value = get_data_from_necropsia.select_data(registro)
            format_value = []
            for el in value:
                if el is not None:
                    el = el.replace("\n", "<br><br>")
                format_value.append(el)
            return render_template('print_necropsia.html', value=format_value)
        except Exception as err:
            pass
            return render_template('print_necropsia.html', value=format_value)
    except Exception as err:
        return redirect('/error')


@app.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'POST':
        if not logged:
            return redirect('/')
        else:
            return redirect('/home')
    return render_template('error.html')


@app.route('/alterar_reabilitacao', methods=['GET', 'POST'])
def alter_reabilitacao():
    if not logged:
        return redirect('/error')
    try:
        print(registro)
        last_files = get_data_from_reabilitacao.select_data(registro)
        if request.method == 'POST':
            values = {'hidratacao_vo': None, 'est_outro':None, 'hidratacao_sc': None, 'aquecimento': None, 'sexo': None,
                      'auscul': None, 'petro_ex': None, 'petro': None, 'cab_na_bo': None, 'olhos_ouv': None, 'fezes': None,
                      'pes': None, 'pele': None, 'palp_abd': None, 'hidra_oral': None, 'hidra_sub': None, 'ali_pas': None,
                      'ali_for': None, 'ali_sl': None, 'lavag': None, 'pisc_ad': None, 'pisc_as': None, 'md_plu': None,
                      'lib': None, 'obito': None, 'eutanasia': None, 'transf': None, 'g_et': "", 'condi_corp': "",
                      'att': "",
                      'desidra': "", 'mhidra_tp1': None, 'mhidra_tp2': None, 'mhidra_tp3': None, 'mhidra_tp4': None,
                      'mhidra_tp5': None,
                      'mhidra_tp6': None, 'mhidra_tp7': None, 'mhidra_tp8': None, 'mhidra_tp9': None, 'mhidra_tp10': None,
                      'mhidra_tp11': None, 'mhidra_tp12': None, 'mhidra_tp13': None, 'mhidra_tp14': None,
                      'mhidra_tp15': None, 'mhidra_tp16': None, 'mhidra_tp17': None, 'mhidra_tp18': None,
                      'mhidra_tp19': None,
                      'mhidra_tp20': None, 'mhidra_tp21': None, 'thidra_tp1': None, 'thidra_tp2': None, 'thidra_tp3': None,
                      'thidra_tp4': None,
                      'thidra_tp5': None, 'thidra_tp6': None, 'thidra_tp7': None, 'thidra_tp8': None, 'thidra_tp9': None,
                      'thidra_tp10': None, 'thidra_tp11': None, 'thidra_tp12': None, 'thidra_tp13': None,
                      'thidra_tp14': None, 'thidra_tp15': None, 'thidra_tp16': None, 'thidra_tp17': None,
                      'thidra_tp18': None,
                      'thidra_tp19': None, 'thidra_tp20': None, 'thidra_tp21': None, 'mali_tp1': None, 'mali_tp2': None,
                      'mali_tp3': None,
                      'mali_tp4': None, 'mali_tp5': None, 'mali_tp6': None, 'mali_tp7': None, 'mali_tp8': None,
                      'mali_tp9': None, 'mali_tp10': None, 'mali_tp11': None, 'mali_tp12': None, 'mali_tp13': None,
                      'mali_tp14': None,
                      'mali_tp15': None, 'mali_tp16': None, 'mali_tp17': None, 'mali_tp18': None, 'mali_tp19': None,
                      'mali_tp20': None, 'mali_tp21': None, 'tali_tp1': None, 'tali_tp2': None, 'tali_tp3': None,
                      'tali_tp4': None, 'tali_tp5': None, 'tali_tp6': None, 'tali_tp7': None, 'tali_tp8': None,
                      'tali_tp9': None, 'tali_tp10': None, 'tali_tp11': None, 'tali_tp12': None, 'tali_tp13': None,
                      'tali_tp14': None,
                      'tali_tp15': None, 'tali_tp16': None, 'tali_tp17': None, 'tali_tp18': None, 'tali_tp19': None,
                      'tali_tp20': None,
                      'tali_tp21': None, 'mmed_tp1': None, 'mmed_tp2': None, 'mmed_tp3': None, 'mmed_tp4': None,
                      'mmed_tp5': None,
                      'mmed_tp6': None, 'mmed_tp7': None, 'mmed_tp8': None, 'mmed_tp9': None, 'mmed_tp10': None,
                      'mmed_tp11': None,
                      'mmed_tp12': None, 'mmed_tp13': None, 'mmed_tp14': None, 'mmed_tp15': None, 'mmed_tp16': None,
                      'mmed_tp17': None,
                      'mmed_tp18': None, 'mmed_tp19': None, 'mmed_tp20': None, 'mmed_tp21': None, 'tmed_tp1': None,
                      'tmed_tp2': None,
                      'tmed_tp3': None, 'tmed_tp4': None, 'tmed_tp5': None, 'tmed_tp6': None, 'tmed_tp7': None,
                      'tmed_tp8': None,
                      'tmed_tp9': None, 'tmed_tp10': None, 'tmed_tp11': None, 'tmed_tp12': None, 'tmed_tp13': None,
                      'tmed_tp14': None,
                      'tmed_tp15': None, 'tmed_tp16': None, 'tmed_tp17': None, 'tmed_tp18': None, 'tmed_tp19': None,
                      'tmed_tp20': None,
                      'tmed_tp21': None
                      }
            for key in request.form.keys():
                value = str(request.form[f'{key}'])
                value = value.strip()
                #value = value.replace("\n", "")
                values[f'{key}'] = f'{value}'

            if values['doc_ad'] == "":
                values['doc_ad'] = f'{last_files[32]}'
            if values['foto_doc_dest'] == "":
                values['foto_doc_dest'] = f'{last_files[98]}'
            if values['file_bio'] == "":
                values['file_bio'] = f'{last_files[100]}'

            delete_from_reabilitacao.delete_data(registro)
            delete_from_reabilitacao_sp.delete_data(registro)
            delete_from_reabilitacao_tp.delete_data(registro)
            keep_id = registro.split('/')[1]
            print(keep_id)
            values['re'] = "/" + keep_id
            insert_into_reabilitacao.insert_data(values)
            insert_into_reabilitacao_sp.insert_data(values)
            insert_into_reabilitacao_tp.insert_data(values)
            return redirect('../home')

        return render_template('alter_reabilitacao.html', value=get_data_from_reabilitacao.select_data(registro),
                               value_sp=get_data_from_reabilitacao_sp.select_data(registro),
                               value_tp=get_data_from_reabilitacao_tp.select_data(registro))
    except Exception as err:
        print(err)
        return redirect('/error')


if __name__ == '__main__':
    app.run()