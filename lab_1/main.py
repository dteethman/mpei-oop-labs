import unit
from sys import argv


def make_floats_array(str_arr):
    try:
        a = [float(num) for num in str_arr]
    except ValueError:
        print('Error: can’t make array of floats cause of wrong input')
        exit(0)
    return a


def input_from_keyboard():
    print('Input file non specified or not exist\n'
          'Type 3 arrays from keyboard in single line divided by return:')
    v = []
    for i in range (3):
        str_arr = input().strip().split(' ')
        arr = make_floats_array(str_arr)
        v.append(arr)
    if v:
        return v
    else:
        return None


def load_from_file(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        return input_from_keyboard()
    v_raw = f.read().split('\n')
    f.close()
    v = []
    for i in range(len(v_raw)):
        v.append(make_floats_array(v_raw[i].strip().split(' ')))
    if v:
        print(f'Loaded from file {filename}')
        print(show_vectors(v))
        return v
    else:
        return None


def show_vectors(arr):
    text = ''
    for i in range(len(arr)):
        text += f'Vector {i + 1}: {arr[i]}\n'
    return text


def save_to_file(filename, text):
    f = open(filename, 'w+', newline='\n')
    f.write(text)
    f.close()


if __name__ == '__main__':
    vectors = []
    if len(argv) < 2:
        vectors = input_from_keyboard()
    else:
        vectors = load_from_file(argv[1])
    if vectors and len(vectors) == 3:
        sa = unit.get_s(vectors[0])
        kb = unit.get_k(vectors[1])
        min_c = unit.get_min(vectors[2])
        sc = unit.get_s(vectors[2])
        kc = unit.get_k(vectors[2])
        try:
            result = sa / kb + min_c + sc / kc
        except ZeroDivisionError:
            print('Error: divided by zero')
            exit(0)
        except TypeError:
            print('Error: bad input value')
            exit(0)
        res_str = f'Sa/Kb + Min_c + Sc/Kc = {result}'
        print(res_str)
        save_to_file('out.txt', f'{show_vectors(vectors)}\n{res_str}')
    else:
        print('Error: loaded more or less that 3 vectors')

