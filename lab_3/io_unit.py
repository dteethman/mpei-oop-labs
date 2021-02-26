import csv
import os
from Cube import Cube
from menu import Menu, MenuItem


def load_cubes_from_csv(filename):
    cubes = []
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, encoding='utf-8') as r_file:
            try:
                file_reader = csv.reader(r_file, delimiter=",")
                for row in file_reader:
                    cube = Cube(float(row[0]))
                    cubes.append(cube)
            except Exception:
                pass
    return cubes


def save_to_csv(filename, cubes: [Cube]):
    with open(filename, mode='w', encoding='utf-8') as w_file:
        f_writer = csv.writer(w_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for cube in cubes:
            print(cube.side)
            f_writer.writerow([cube.side])
    return 0, f'\nSaved to {filename}'


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
            if table[i] == int(table[i]):
                res_str += f'{table[i]:<{col_width[index]}.0f}'
            else:
                res_str += f'{table[i]:<{col_width[index]}.2f}'
            if table[i] < 0:
                res_str += ' '
        res_str += '\n'
    return res_str


def get_max_value_length(table_data, annotations):
    n = [max(5, len(f'{a}  ')) for a in annotations]
    for i in range(len(table_data[0])):
        n = [max(n[index], len(f'{(abs(table[i])):.2f}  ')) for index, table in enumerate(table_data)]
    return n


def present_cubes(cubes: [Cube]):
    annotations = ['№', 'Side', 'Perimeter', 'Area', 'Volume']
    nums, sides, perimeters, areas, volumes = [], [], [], [], []
    for index, cube in enumerate(cubes):
        nums.append(index + 1)
        sides.append(cube.side)
        perimeters.append(cube.perimeter)
        areas.append(cube.area)
        volumes.append(cube.volume)
    table_data = [nums, sides, perimeters, areas, volumes]
    return show_arg_val_table(table_data, annotations)


def show_cubes(cubes: [Cube]):
    text = present_cubes(cubes)
    menu = Menu([
        MenuItem("Back", lambda x, y: (x, y), (-1, ''))
    ])
    return menu.show(avoid_clr=True, text=text)


def add_cube(cubes: [Cube]):
    os.system('clear')
    side = input('Type side of cube: ')
    try:
        side_f = float(side)
        if side_f > 0:
            cubes.append(Cube(side_f))
            msg = f'\nAdded cube with side {side}'
        else:
            msg = '\nERROR: can’t add cube, side must be > 0'
    except ValueError:
        msg = '\nERROR: can’t add cube, wrong input'
    return 0, msg


def delete_cube(cubes: [Cube]):
    os.system('clear')
    print(present_cubes(cubes))
    pos = input('Type № of cube to delete: ')
    try:
        index = int(pos)
        if index - 1 in range(len(cubes)):
            cubes.pop(index - 1)
            msg = f'\nDeleted cube at № {index}'
        else:
            msg = '\nERROR: can’t delete cube, wrong index'
    except ValueError:
        msg = '\nERROR: can’t delete cube, wrong input'
    return 0, msg


def compare_cubes(cubes: [Cube]):
    os.system('clear')
    print(present_cubes(cubes))
    pos = input('Type №№ of cubes to compare divided by space: ')
    str_arr = pos.strip().split(' ')
    try:
        index1, index2 = int(str_arr[0]), int(str_arr[1])
        if index1 - 1 in range(len(cubes)) and index2 - 1 in range(len(cubes)):
            cubes_to_compare = [cubes[index1 - 1], cubes[index2 - 1]]
            os.system('clear')
            menu = Menu([
                MenuItem("Back", lambda x, y: (x, y), (-1, ''))
            ])
            msg = (present_cubes(cubes_to_compare))
            if cubes_to_compare[0] < cubes_to_compare[1]:
                msg += f'\nCube №{index1} less than cube №{index2}'
            elif cubes_to_compare[0] > cubes_to_compare[1]:
                msg += f'\nCube №{index1} greater than cube №{index2}'
            else:
                msg += f'\nCube №{index1} equal cube №{index2}'
            return menu.show(avoid_clr=True, text=msg)
        else:
            msg = '\nERROR: can’t compare cubes, wrong index'
    except ValueError:
        msg = '\nERROR: can’t compare cubes, wrong input'
    return 0, msg