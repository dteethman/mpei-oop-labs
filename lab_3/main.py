from Cube import Cube
import os
from menu import Menu, MenuItem
import io_unit as iou


if __name__ == "__main__":
    filename = 'cubes.csv'
    cubes = iou.load_cubes_from_csv('cubes.csv')
    if cubes:
        text = (f'Loaded {len(cubes)} cubes from file {filename}')
    else:
        text = 'No one cube loaded'
    main_menu = Menu([
        MenuItem('Show сubes', iou.show_cubes, (cubes,)),
        MenuItem('Add cube', iou.add_cube, (cubes,)),
        MenuItem('Delete cube', iou.delete_cube, (cubes, )),
        MenuItem('Compare cubes', iou.compare_cubes, (cubes, )),
        MenuItem('Save changes', iou.save_to_csv, ('cubes.csv', cubes)),
        MenuItem('Exit', exit, (0,))
    ])
    main_menu.show(avoid_clr=True, info_msg=f'\n{text}')