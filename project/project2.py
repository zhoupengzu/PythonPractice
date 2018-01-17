'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''


class Door():
    BASE_WORD = 'WELCOME'
    BASW_LINE = '-'
    BASE_POINT_LINE = '·|·'

    def __init__(self, row=9):
        self.row = row
        self.col = row * 3

    def __get_center_str(self):
        return Door.BASE_WORD.center(self.col, Door.BASW_LINE)

    def __get_up_str(self):
        rows_str = ''
        top_lines = self.row // 2
        for num in range(top_lines):
            rows_str = rows_str + \
                (Door.BASE_POINT_LINE * (2 * num + 1)
                 ).center(self.col, Door.BASW_LINE)
            if num != top_lines - 1:
                rows_str = rows_str + '\n'
        return rows_str

    def all_str(self):
        up_str = self.__get_up_str()
        bottom_str = up_str[::-1]
        print(up_str + '\n' + self.__get_center_str() + '\n' + bottom_str)


door = Door(7)
door.all_str()
