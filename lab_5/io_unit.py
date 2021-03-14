import csv
import os
from ColoredCube import ColoredCube
from menu import Menu, MenuItem


def load_cubes_from_csv(cubes: [ColoredCube]):
    filename = input('Type path to file, or press return: ')
    os.system('clear')
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, encoding='utf-8') as r_file:
            try:
                file_reader = csv.reader(r_file, delimiter=",")
                new_cubes = []
                for row in file_reader:
                    cube = ColoredCube(float(row[0]), row[1])
                    new_cubes.append(cube)
                if new_cubes:
                    msg = f'\nSuccessfully loaded {len(new_cubes)} cubes'
                else:
                    msg = 'No one cube loaded'
                del cubes[0:len(cubes)]
                cubes += new_cubes
                return 0, msg
            except Exception:
                msg = f'\nERROR: Can’t load cubes, file error'
                return 0, msg
    msg = f'\nERROR: Can’t load cubes, file not exist'
    return 0, msg


def save_to_csv(cubes: [ColoredCube]):
    filename = input('Type name of file: ')
    with open(filename, mode='w', encoding='utf-8') as w_file:
        f_writer = csv.writer(w_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for cube in cubes:
            f_writer.writerow([cube.side, cube.color])
    return 0, f'\nSaved to {filename}'


def get_max_value_length(cubes: [ColoredCube], annotations):
    nums, sides, perimeters, areas, volumes, colors = [], [], [], [], [], []
    for index, cube in enumerate(cubes):
        nums.append(index + 1)
        sides.append(cube.side)
        perimeters.append(cube.perimeter)
        areas.append(cube.area)
        volumes.append(cube.volume)
        colors.append(cube.color)
    table_data = [nums, sides, perimeters, areas, volumes, colors]

    n = [max(5, len(f'{a}  ')) for a in annotations]
    for index, table in enumerate(table_data):
        for item in table:
            if type(item) is str:
                n[index] = max(n[index], len(f'{item}  '))
            else:
                n[index] = max(n[index], len(f'{item:.2f}  '))
    return n


def present_cubes(cubes: [ColoredCube], show_colors=True):
    annotations = ['№', 'Side', 'Perimeter', 'Area', 'Volume', 'Colors']
    col_widths = get_max_value_length(cubes, annotations)
    if not show_colors:
        annotations.pop()
    res_str = ''.join(([f'{a:<{col_widths[index]}}' for index, a in enumerate(annotations)])) + '\n'
    res_str += '-' * len(res_str) + '\n'
    for index, cube in enumerate(cubes):
        res_str += cube.present_table(index + 1, col_widths, show_colors)
    return res_str


def show_cubes(cubes: [ColoredCube]):
    text = present_cubes(cubes)
    menu = Menu([
        MenuItem("Back", lambda x, y: (x, y), (-1, ''))
    ])
    return menu.show(avoid_clr=True, text=text)


def filter_cubes(cubes: [ColoredCube]):
    os.system('clear')
    color = input('Type color to filter: ')
    filtered_cubes = list(filter(lambda x: x.color == color,cubes))
    if filtered_cubes:
        text = f'{color} cubes: \n\n' + present_cubes(filtered_cubes, show_colors=False)
        menu = Menu([
            MenuItem("Back", lambda x, y: (x, y), (-1, ''))
        ])
        return menu.show(avoid_clr=True, text=text)
    else:
        os.system('clear')
        print(f'Array don’t have {color} cubes')
        input('Press return')
        msg = ''
        return 0, msg


def add_cubes(cubes: [ColoredCube]):
    os.system('clear')
    num = input('Type number of cubes to add: ')
    msg = ''
    bef_cubes_count = len(cubes)
    try:
        num = int(num)
    except ValueError:
        msg = '\nERROR: can’t add cubes, wrong input'
    for i in range(num):
        code, msg = add_cube(cubes, msg)
    cubes_added = len(cubes) - bef_cubes_count
    os.system('clear')
    print(present_cubes(cubes))
    input('Press return')
    msg = f'\nSuccessfully added {cubes_added} cubes'
    return 0, msg


def add_cube(cubes: [ColoredCube], msg=''):
    os.system('clear')
    print(present_cubes(cubes))
    if msg:
        print(msg)
    inp = input('Type side of cube and color divided by space: ')
    try:
        side, color = inp.strip().split(' ')
        side_f = float(side)
        if side_f > 0:
            cubes.append(ColoredCube(side_f, color))
            msg = f'\nAdded {color} cube with side {side}'
        else:
            msg = '\nERROR: can’t add cube, side must be > 0'
    except ValueError:
        msg = '\nERROR: can’t add cube, wrong input'
    return 0, msg


def edit_cube(cubes: [ColoredCube]):
    os.system('clear')
    print(present_cubes(cubes))
    pos = input('Type № of cube to edit: ')
    try:
        index = int(pos)
        if index - 1 in range(len(cubes)):
            side = input('Type side of cube: ')
            color = input('Type color of cube: ')
            try:
                side_f = float(side)
                if side_f > 0:
                    cubes[index - 1].side = side_f
                    cubes[index - 1].color = color
                    os.system('clear')
                    print(present_cubes(cubes))
                    msg = f'\nSuccessfully edited'
                    input('Press return')
                else:
                    msg = '\nERROR: can’t edit cube, side must be > 0'
            except ValueError:
                msg = '\nERROR: can’t edit cube, wrong input'
        else:
            msg = '\nERROR: can’t edit cube, wrong index'
    except ValueError:
        msg = '\nERROR: can’t edit cube, wrong input'
    return 0, msg


def delete_cube(cubes: [ColoredCube]):
    os.system('clear')
    print(present_cubes(cubes))
    pos = input('Type № of cube to delete: ')
    try:
        index = int(pos)
        if index - 1 in range(len(cubes)):
            cubes.pop(index - 1)
            os.system('clear')
            print(present_cubes(cubes))
            msg = f'\nSuccessfully deleted'
            input('Press return')
        else:
            msg = '\nERROR: can’t edit cube, wrong index'
    except ValueError:
        msg = '\nERROR: can’t edit cube, wrong input'
    return 0, msg


def compare_cubes(cubes: [ColoredCube]):
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