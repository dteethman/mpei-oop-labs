def show_input_str(loaded_data):
    return f'Start point:      {loaded_data[0]:<10.2f}\n' \
           f'End point:        {loaded_data[1]:<10.2f}\n' \
           f'Number of breaks: {loaded_data[2]:<10}'


def load_from_file(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        return input_from_keyboard()
    raw_data = f.read().split(' ')
    f.close()
    try:
        loaded_data = (float(raw_data[0]), float(raw_data[1]), int(raw_data[2]))
    except ValueError:
        print('Error: can’t read data cause of wrong input file format\n'
              'Input format: float float int')
        exit(0)
    else:
        print(f'Loaded from file {filename}')
        print(show_input_str(loaded_data))
        return loaded_data


def input_from_keyboard():
    print('Input file not specified or not exist')
    start = input("Type start point: ")
    end = input("Type end point: ")
    number_of_breaks = input("Type number of breaks: ")
    try:
        loaded_data = (float(start), float(end), int(number_of_breaks))
    except ValueError:
        print('Error: can’t read data cause of bad input\n'
              'Input format: float float int')
        exit(0)
    else:
        return loaded_data


def show_arg_val_table(table_data, annotations):
    res_str = ' '
    col_width = get_max_value_length(table_data, annotations)
    res_str += ''.join(([f'{a:<{col_width[index]}}' for index, a in enumerate(annotations)])) + '\n'
    res_str += ('-' * len(res_str) + '\n')
    for i in range(len(table_data[0])):
        res_str += ' '
        for index, table in enumerate(table_data):
            if table[i] < 0:
                res_str = res_str[:-1]
            res_str += f'{table[i]:<{col_width[index]}.2f}'
            if table[i] < 0:
                res_str += ' '
        res_str += '\n'
    return res_str


def get_max_value_length(table_data, annotations):
    n = [max(5, len(f' {a}  ')) for a in annotations]
    for i in range(len(table_data[0])):
        n = [max(n[index], len(f' {(abs(table[i])):.2f}  ')) for index, table in enumerate(table_data)]
    return n


def save_to_file(filename, text):
    f = open(filename, 'w+', newline='\n')
    f.write(text)
    f.close()