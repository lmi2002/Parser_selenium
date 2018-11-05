import re


def lower_register(*args):
    data = []
    for arg in args:
        arg = str(arg).lower()
        data.append(arg)
    return data


def delete_all_spec_symbol(*args):
    data = []
    symbols = '/.,"}][# !$%^&\*;:{=+-_~}('
    for arg in args:
        arg = str(arg)
        for char in symbols:
            arg = arg.replace(char, '')
        data.append(arg)
    return data