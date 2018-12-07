import pandas as pd


def delete_all_spec_symbol(*args):
    data = []
    symbols = '/.,"}][# !$%^&\*;:{=+-_~}('
    for arg in args:
        arg = str(arg)
        for char in symbols:
            arg = arg.replace(char, '')
        data.append(arg)
    return data


def delete_en_and_num_symbol(lst):
    data = []

    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    for el in lst:
        el_orig = str(el)
        el_repl = el_orig.upper()
        gen = (char for char in symbols)
        for f in gen:
            el_repl = el_repl.replace(f, '')
        string = el_orig + ";" + el_repl
        data.append(string)

    return data


def cut_big_file(file, rows, skip, names):
    try:
        df = pd.read_csv(file, sep=';', names=names, skiprows=skip, nrows=rows)
        df.to_csv(path_or_buf=file[:-4]+str(skip)+file[-4:], sep=';', index=False)
        return 1
    except:
        df = pd.read_csv(file, sep=';', names=names, skiprows=skip)
        df.to_csv(path_or_buf=file[:-4]+str(skip)+file[-4:])

# file='tec_doc_2017_2_cross.csv'
# rows=1000000
# skip=1
# df_names=pd.read_csv(file, sep=';', nrows=0)
# res=1
# while res:
#     cut(file, rows, skip, names=df_names.columns)
#     skip+=rows