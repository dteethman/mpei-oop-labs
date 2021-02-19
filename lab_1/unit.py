def check_floats(arr):
    return all(isinstance(x, float) for x in arr)


def get_max(arr):
    if not check_floats(arr):
        return None
    try:
        m = arr[0]
    except IndexError:
        return None
    for n in arr:
        if n > m:
            m = n
    return m


def get_min(arr):
    if not check_floats(arr):
        return None
    try:
        m = arr[0]
    except IndexError:
        return None
    for n in arr:
        if n < m:
            m = n
    return m


def get_s(arr):
    if not check_floats(arr):
        return None
    try:
        s = 0
    except IndexError:
        return None
    for n in arr:
        if n > 0:
            s += n
    return s


def get_k(arr):
    if not check_floats(arr):
        return None
    try:
        k = 0
    except IndexError:
        return None
    for n in arr:
        if n > 0:
            k += 1
    return k