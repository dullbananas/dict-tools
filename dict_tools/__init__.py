def map_keys(function, dictionary):
    return {
        function(key): value
        for key, value in dictionary.items()
    }


def map_values(function, dictionary):
    return {
        key: function(value)
        for key, value in dictionary.items()
    }


def iter_multi_values(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, (tuple, list)):
            for subvalue in value:
                yield (key, subvalue)
        else:
            yield (key, value)


def invert_dict(dictionary):
    return {
        value: key
        for key, value in dictionary.items()
    }
