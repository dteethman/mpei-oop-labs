import io_unit as iou


if __name__ == '__main__':
    n = iou.input_quantity()
    arr = []
    for i in range(n):
        arr.append(iou.generate_number())

    iou.save_to_file('arr.txt', arr)
    loaded_arr = iou.read_from_file('arr.txt')
    sum = sum(loaded_arr)
    print(f'Array: {iou.show_array(loaded_arr)}')
    print(f'Sum of elements: {sum}')