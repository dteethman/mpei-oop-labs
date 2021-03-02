from Cube import Cube
from menu import Menu, MenuItem
import io_unit as iou

if __name__ == "__main__":
    cubes: [Cube] = []
    msg = ''

    main_menu = Menu([
        MenuItem('Load cubes from file', iou.load_cubes_from_csv, (cubes, )),
        MenuItem('Show cubes', iou.show_cubes, (cubes,)),
        MenuItem('Add cubes', iou.add_cubes, (cubes,)),
        MenuItem('Edit cube', iou.edit_cube, (cubes, )),
        MenuItem('Delete cube', iou.delete_cube, (cubes,)),
        MenuItem('Compare cubes', iou.compare_cubes, (cubes,)),
        MenuItem('Save changes', iou.save_to_csv, (cubes, )),
        MenuItem('Exit', exit, (0,))
    ])
    main_menu.show(avoid_clr=True, info_msg=f'\n{msg}')