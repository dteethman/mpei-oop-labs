from random import randint
import os
import datetime


def input_quantity():
    n = input('Type number of elements in array: ')
    try:
        quantity = int(n)
    except ValueError:
        print('Type error: not an integer')
        exit(0)

    if quantity > 100 or quantity < 1:
        print('Value error: quantity more than 100 or less than 1')
        exit(0)
    else:
        return quantity


def generate_number():
    return randint(-50, 50)


def show_array(arr):
    text = ' '.join([f'{num}' for num in arr])
    return text


def save_to_file(filename, arr):
    try:
        if  os.path.exists(filename) and os.path.isfile(filename):
            timestamp = datetime.datetime.today().strftime('%d-%m-%Y %H.%M.%S')
            os.rename(f'{filename}', f'{filename}[{timestamp}].old')
        text = show_array(arr)
        f = open(filename, 'w+', newline='\n')
        f.write(text)
        f.close()
        print(f'Successfully saved to {filename}')
    except Exception:
        print('ERROR: Can not write file')


def read_from_file(filename):
    if os.path.exists(filename) and os.path.isfile(filename):
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            print('ERROR: Can not read file')
            exit(0)
        arr_raw = f.read().split('\n')[0].strip().split(' ')
        f.close()
        try:
            arr = list(map(lambda x: int(x), arr_raw))
            print(f'Successfully loaded from {filename}')
            return arr
        except ValueError:
            print('ERROR: Can not read data from file')
            exit(0)
    else:
        print(f'ERROR: File {filename} not exist')
        exit(0)
