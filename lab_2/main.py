from math import cos
from sys import argv
import math_unit as mu
import io_unit as iou

if __name__ == '__main__':
    try:
        filename = argv[1]
    except IndexError:
        filename = ''
    input_data = iou.load_from_file(filename)
    arguments = mu.get_agruments_array(*input_data)
    f1_values = mu.get_values_array(lambda x: x * x + 1, arguments)
    f2_values = mu.get_values_array(lambda x: cos(2.5 * x + 4), arguments)

    table_1_str = iou.show_arg_val_table([arguments, f1_values], ['x', 'x²+1'])
    table_2_str = iou.show_arg_val_table([arguments, f2_values], ['x', 'cos(2,5x + 4)'])
    table_3_str = iou.show_arg_val_table([arguments, f1_values, f2_values], ['x', 'x²+1', 'cos(2,5x + 4)'])
    out_str = '\n'.join([table_1_str, table_2_str, table_3_str]) + '\n'
    print('\n' + out_str)
    iou.save_to_file('out.txt', out_str)