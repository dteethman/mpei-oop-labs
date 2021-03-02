class Cube:
    def __init__(self, side):
        self.side = abs(side)

    def __str__(self):
        return f'Side:      {self.side:.2f}\n' \
               f'Perimeter: {self.perimeter:.2f}\n' \
               f'Area:      {self.area:.2f}\n' \
               f'Volume:    {self.volume:.2f}\n'

    def __gt__(self, other):
        return self.side > other.side

    def __eq__(self, other):
        return self.side == other.side

    def __ge__(self, other):
        return self.side >= other.side

    perimeter = property()
    area = property()
    volume = property()

    @perimeter.getter
    def perimeter(self):
        return self.side * 12

    @perimeter.setter
    def perimeter(self, value):
        self.side = value / 12

    @area.getter
    def area(self):
        return self.side ** 2 * 6

    @area.setter
    def area(self, value):
        self.side = (value / 6) ** (1 / float(2))

    @volume.getter
    def volume(self):
        return self.side ** 3

    @volume.setter
    def volume(self, value):
        self.side = value ** (1 / float(3))

    @staticmethod
    def show_annotations(col_widths):
        annotations = ['№', 'Side', 'Perimeter', 'Area', 'Volume']
        return ''.join(([f'{a:<{col_widths[index]}}' for index, a in enumerate(annotations)])) + '\n'

    def present_table(self, number, col_widths):
        columns = [self.side, self.perimeter, self.area, self.volume]
        res_str = ''.join(f'{number:<{col_widths[0]}.0f}')
        for index, param in enumerate(columns):
            if param == int(param):
                res_str += f'{param:<{col_widths[index + 1]}.0f}'
            else:
                res_str += f'{param:<{col_widths[index + 1]}.2f}'
        res_str += '\n'
        return res_str
