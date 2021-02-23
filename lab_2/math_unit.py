def get_agruments_array(start, end, num_of_breaks):
    if start == end:
        return [start]
    elif start > end:
        start, end = end, start
    result = []
    step = (end - start) / (num_of_breaks + 1)
    cur = start
    while cur <= end:
        result.append(cur)
        cur += step
    return result


def get_values_array(function, arguments):
    try:
        return list(map(function, arguments))
    except Exception:
        print('Error: can’t calculate values on interval')
        exit(0)
