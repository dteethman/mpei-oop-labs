from Cube import Cube


class ColoredCube(Cube):
    def __init__(self, side, color='Black'):
        Cube.__init__(self, side)
        self.color = color

    def __str__(self):
        return f'Side:      {self.side:.2f}\n' \
               f'Perimeter: {self.perimeter:.2f}\n' \
               f'Area:      {self.area:.2f}\n' \
               f'Volume:    {self.volume:.2f}\n' \
               f'Color:     {self.color}'

    def present_table(self, number, col_widths, show_color=True):
        columns = [self.side, self.perimeter, self.area, self.volume, self.color]
        res_str = ''.join(f'{number:<{col_widths[0]}.0f}')
        for index, param in enumerate(columns):
            if not show_color and index == 4:
                pass
            else:
                if type(param) is str:
                    res_str += f'{param:<{col_widths[index + 1]}}'
                else:
                    if param == int(param):
                        res_str += f'{param:<{col_widths[index + 1]}.0f}'
                    else:
                        res_str += f'{param:<{col_widths[index + 1]}.2f}'

        res_str += '\n'
        return res_str
