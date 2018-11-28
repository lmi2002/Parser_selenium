def delete_all_spec_symbol(*args):
    data = []
    symbols = '/.,"}][# !$%^&\*;:{=+-_~}('
    for arg in args:
        arg = str(arg)
        for char in symbols:
            arg = arg.replace(char, '')
        data.append(arg)
    return data