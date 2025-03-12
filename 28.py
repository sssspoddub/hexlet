def diff_keys(data1, data2):
    return {
        'kept': data1.keys() & data2.keys(),
        'added': data2.keys() - data1.keys(),
        'removed': data1.keys() - data2.keys()
    }
