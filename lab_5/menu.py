import os


class MenuItem:
    def __init__(self, text, func, params=None):
        self.text = text
        self.func = func
        self.params = params


class Menu:
    def __init__(self, items: [MenuItem]):
        self.items = items

    def show(self, text='', info_msg='', avoid_clr=False):
        act_n = 0
        while act_n == 0:
            os.system('clear')
            if text != '' and avoid_clr:
                print(text)
            for index, item in enumerate(self.items):
                print(f'{index + 1}: {item.text}')
            if info_msg == '':
                info_msg = '\n'
            print(info_msg)
            usr_inp = input("Type number of action and press return: ")
            try:
                act_n = int(usr_inp)
            except Exception:
                info_msg = f'\nERROR: {usr_inp} -- wrong input'
                act_n = 0

            if act_n > len(self.items) or act_n < 1:
                info_msg = f'\nERROR: {usr_inp} -- wrong input'
                act_n = 0
            else:
                if self.items[act_n - 1].params is not None:
                    act_n, info_msg = self.items[act_n - 1].func(*self.items[act_n - 1].params)
                else:
                    act_n, info_msg = self.items[act_n - 1].func()
        if act_n == -1:
            act_n = 0
        return act_n, info_msg
